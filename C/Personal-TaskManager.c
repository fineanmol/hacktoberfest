/*
 * best_way.c
 * Simple single-file Personal Task Manager
 *
 * Compile:
 *   gcc -std=c11 -O2 best_way.c -o best_way
 *
 * Run:
 *   ./best_way
 *
 * Saves tasks to "tasks.db" in a simple line-based format.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

#define DB_FILE "tasks.db"
#define LINE_BUF 1024
#define DATE_LEN 11   /* YYYY-MM-DD + null */

typedef enum { LOW=1, MEDIUM=2, HIGH=3 } Priority;

typedef struct {
    int id;
    char title[128];
    char due[DATE_LEN];   /* "YYYY-MM-DD" or empty */
    Priority priority;
    int done;             /* 0 or 1 */
    char notes[512];
    time_t created;
} Task;

typedef struct {
    Task *items;
    size_t used;
    size_t cap;
    int next_id;
} TaskList;

/* ---------- Utility functions ---------- */

static void die(const char *msg) {
    perror(msg);
    exit(EXIT_FAILURE);
}

static void safe_getline(char *buf, size_t n) {
    if (!fgets(buf, (int)n, stdin)) {
        buf[0] = '\0';
        return;
    }
    size_t len = strlen(buf);
    if (len && buf[len-1] == '\n') buf[len-1] = '\0';
}

/* trim whitespace (in place) */
static void trim(char *s) {
    char *p = s;
    while (isspace((unsigned char)*p)) p++;
    if (p != s) memmove(s, p, strlen(p) + 1);
    char *end = s + strlen(s) - 1;
    while (end >= s && isspace((unsigned char)*end)) *end-- = '\0';
}

/* Validate a simple YYYY-MM-DD date (not fully strict) */
static int valid_date(const char *d) {
    if (!d || strlen(d) != 10) return 0;
    if (d[4] != '-' || d[7] != '-') return 0;
    for (int i = 0; i < 10; ++i) {
        if (i==4 || i==7) continue;
        if (!isdigit((unsigned char)d[i])) return 0;
    }
    return 1;
}

static const char* prio_name(Priority p) {
    switch (p) {
        case LOW: return "Low";
        case MEDIUM: return "Medium";
        case HIGH: return "High";
        default: return "Unknown";
    }
}

static char time_str(time_t t, char *buf, size_t n) {
    struct tm tm;
    localtime_r(&t, &tm);
    strftime(buf, n, "%Y-%m-%d %H:%M", &tm);
    return 0;
}

/* ---------- TaskList management ---------- */

static void tl_init(TaskList *tl) {
    tl->items = NULL;
    tl->used = 0;
    tl->cap = 0;
    tl->next_id = 1;
}

static void tl_free(TaskList *tl) {
    free(tl->items);
    tl->items = NULL;
    tl->used = tl->cap = 0;
}

static void tl_ensure(TaskList *tl, size_t n) {
    if (tl->cap >= n) return;
    size_t newcap = tl->cap ? tl->cap * 2 : 8;
    while (newcap < n) newcap *= 2;
    Task *tmp = realloc(tl->items, newcap * sizeof(Task));
    if (!tmp) die("realloc");
    tl->items = tmp;
    tl->cap = newcap;
}

static Task* tl_add(TaskList *tl, const Task *t) {
    tl_ensure(tl, tl->used + 1);
    tl->items[tl->used] = *t;
    tl->used += 1;
    if (t->id >= tl->next_id) tl->next_id = t->id + 1;
    return &tl->items[tl->used - 1];
}

static Task* tl_find_by_id(TaskList *tl, int id) {
    for (size_t i = 0; i < tl->used; ++i) {
        if (tl->items[i].id == id) return &tl->items[i];
    }
    return NULL;
}

static int tl_remove_by_id(TaskList *tl, int id) {
    for (size_t i = 0; i < tl->used; ++i) {
        if (tl->items[i].id == id) {
            /* swap with last */
            tl->items[i] = tl->items[tl->used - 1];
            tl->used -= 1;
            return 1;
        }
    }
    return 0;
}

/* ---------- Persistence ---------- */

/* Format per line:
   id|done|priority|created_epoch|due|title|notes
   Notes and title have '|' and '\n' replaced by spaces for simplicity.
*/
static void escape_field(char *dst, const char *src, size_t n) {
    size_t j = 0;
    for (size_t i = 0; src[i] && j + 1 < n; ++i) {
        char c = src[i];
        if (c == '\n' || c == '\r' || c == '|') c = ' ';
        dst[j++] = c;
    }
    dst[j] = '\0';
}

static void save_tasks(TaskList *tl) {
    FILE *f = fopen(DB_FILE, "w");
    if (!f) {
        perror("Warning: could not open tasks.db for saving");
        return;
    }
    char esc_title[256], esc_notes[1024];
    for (size_t i = 0; i < tl->used; ++i) {
        Task *t = &tl->items[i];
        escape_field(esc_title, t->title, sizeof(esc_title));
        escape_field(esc_notes, t->notes, sizeof(esc_notes));
        fprintf(f, "%d|%d|%d|%ld|%s|%s|%s\n",
                t->id, t->done, t->priority, (long)t->created,
                t->due[0] ? t->due : "-", esc_title, esc_notes);
    }
    fclose(f);
}

static void load_tasks(TaskList *tl) {
    FILE *f = fopen(DB_FILE, "r");
    if (!f) return; /* no file yet is fine */
    char line[LINE_BUF];
    while (fgets(line, sizeof(line), f)) {
        trim(line);
        if (line[0] == '\0') continue;
        Task t;
        char duebuf[DATE_LEN], titlebuf[256], notesbuf[1024];
        long created;
        int scanned = sscanf(line, "%d|%d|%d|%ld|%10[^|]|%255[^|]|%1023[^\n]",
                             &t.id, &t.done, (int*)&t.priority, &created,
                             duebuf, titlebuf, notesbuf);
        if (scanned >= 6) {
            t.created = (time_t)created;
            if (strcmp(duebuf, "-") == 0) t.due[0] = '\0';
            else strncpy(t.due, duebuf, DATE_LEN-1), t.due[DATE_LEN-1] = '\0';
            strncpy(t.title, titlebuf, sizeof(t.title)-1);
            t.title[sizeof(t.title)-1] = '\0';
            if (scanned == 7) {
                strncpy(t.notes, notesbuf, sizeof(t.notes)-1);
                t.notes[sizeof(t.notes)-1] = '\0';
            } else t.notes[0] = '\0';
            tl_add(tl, &t);
        }
    }
    fclose(f);
}

/* ---------- Display / Interaction ---------- */

static void print_task_short(const Task *t) {
    char timestr[64];
    time_str(t->created, timestr, sizeof(timestr));
    printf("[%d] %s%s (prio: %s, created: %s) %s\n",
           t->id, t->title, t->done ? " ✅" : "",
           prio_name(t->priority), timestr, t->due[0] ? t->due : "");
}

static void print_task_full(const Task *t) {
    char timestr[64];
    time_str(t->created, timestr, sizeof(timestr));
    printf("ID: %d\nTitle: %s\nStatus: %s\nPriority: %s\nCreated: %s\nDue: %s\nNotes:\n%s\n",
           t->id, t->title, t->done ? "Done" : "Pending",
           prio_name(t->priority), timestr, t->due[0] ? t->due : "None", t->notes);
}

static void list_tasks(TaskList *tl) {
    if (tl->used == 0) {
        puts("No tasks found.");
        return;
    }
    /* Simple sort: show HIGH first, then MEDIUM, LOW, then by created */
    Task *arr = malloc(tl->used * sizeof(Task));
    if (!arr) die("malloc");
    memcpy(arr, tl->items, tl->used * sizeof(Task));
    qsort(arr, tl->used, sizeof(Task), (int(*)(const void*,const void*)) (+
        [](const Task *a, const Task *b)->int {
            if (a->priority != b->priority) return b->priority - a->priority;
            if (a->done != b->done) return a->done - b->done; /* pending first */
            if (a->created < b->created) return -1;
            if (a->created > b->created) return 1;
            return 0;
        }
    ));
    for (size_t i = 0; i < tl->used; ++i) {
        print_task_short(&arr[i]);
    }
    free(arr);
}

static void add_task_interactive(TaskList *tl) {
    Task t;
    memset(&t, 0, sizeof(t));
    t.id = tl->next_id++;
    t.created = time(NULL);
    char buf[LINE_BUF];
    printf("Title: ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    if (buf[0] == '\0') {
        puts("Title is required. Aborting add.");
        return;
    }
    strncpy(t.title, buf, sizeof(t.title)-1);

    printf("Due date (YYYY-MM-DD) or leave empty: ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    if (buf[0] && !valid_date(buf)) {
        puts("Invalid date format. Leaving empty.");
        t.due[0] = '\0';
    } else if (buf[0]) {
        strncpy(t.due, buf, DATE_LEN-1);
        t.due[DATE_LEN-1] = '\0';
    } else t.due[0] = '\0';

    printf("Priority (1 low, 2 medium, 3 high) [2]: ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    int p = 2;
    if (buf[0]) p = atoi(buf);
    if (p < 1 || p > 3) p = 2;
    t.priority = (Priority)p;

    printf("Notes (single-line, optional): ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    strncpy(t.notes, buf, sizeof(t.notes)-1);

    t.done = 0;
    tl_add(tl, &t);
    save_tasks(tl);
    printf("Added task [%d] %s\n", t.id, t.title);
}

static void show_help(void) {
    puts("Commands:");
    puts("  add         Add a new task");
    puts("  list        List tasks (sorted by priority)");
    puts("  view <id>   View task details");
    puts("  edit <id>   Edit a task");
    puts("  done <id>   Mark task done");
    puts("  undone <id> Mark task not done");
    puts("  rm <id>     Remove a task");
    puts("  search <q>  Search title/notes");
    puts("  save        Save tasks");
    puts("  help        Show this help");
    puts("  quit        Exit");
}

/* Simple search over title and notes (case-insensitive substring) */
static void search_tasks(TaskList *tl, const char *q) {
    if (!q || !q[0]) { puts("Empty query."); return; }
    char qlow[256];
    strncpy(qlow, q, sizeof(qlow)-1); qlow[sizeof(qlow)-1]=0;
    for (char *p = qlow; *p; ++p) *p = (char)tolower((unsigned char)*p);
    int found = 0;
    for (size_t i = 0; i < tl->used; ++i) {
        char tmp[sizeof(tl->items[i].title) + sizeof(tl->items[i].notes) + 2];
        snprintf(tmp, sizeof(tmp), "%s %s", tl->items[i].title, tl->items[i].notes);
        for (char *p = tmp; *p; ++p) *p = (char)tolower((unsigned char)*p);
        if (strstr(tmp, qlow)) {
            print_task_short(&tl->items[i]);
            found = 1;
        }
    }
    if (!found) puts("No matching tasks.");
}

static void view_task(TaskList *tl, int id) {
    Task *t = tl_find_by_id(tl, id);
    if (!t) { printf("Task %d not found.\n", id); return; }
    print_task_full(t);
}

static void edit_task(TaskList *tl, int id) {
    Task *t = tl_find_by_id(tl, id);
    if (!t) { printf("Task %d not found.\n", id); return; }
    char buf[LINE_BUF];
    printf("Editing task [%d] %s\n", t->id, t->title);
    printf("New title (leave empty to keep): ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    if (buf[0]) strncpy(t->title, buf, sizeof(t->title)-1);

    printf("New due (YYYY-MM-DD) or empty to clear: ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    if (buf[0]) {
        if (valid_date(buf)) strncpy(t->due, buf, DATE_LEN-1);
        else puts("Invalid date; keeping old value.");
    } else t->due[0] = '\0';

    printf("New priority (1-3) or empty to keep [%s]: ", prio_name(t->priority));
    safe_getline(buf, sizeof(buf)); trim(buf);
    if (buf[0]) {
        int p = atoi(buf);
        if (p >= 1 && p <= 3) t->priority = (Priority)p;
        else puts("Invalid priority; keeping old.");
    }

    printf("Notes (leave empty to keep): ");
    safe_getline(buf, sizeof(buf)); trim(buf);
    if (buf[0]) strncpy(t->notes, buf, sizeof(t->notes)-1);
    save_tasks(tl);
    puts("Task updated.");
}

/* ---------- Main loop ---------- */

int main(void) {
    TaskList tl;
    tl_init(&tl);
    load_tasks(&tl);

    printf("best_way - Personal Task Manager\n");
    printf("Loaded %zu tasks. Type 'help' for commands.\n", tl.used);

    char line[LINE_BUF];
    while (1) {
        printf(">>> ");
        if (!fgets(line, sizeof(line), stdin)) {
            puts("");
            break;
        }
        trim(line);
        if (line[0] == '\0') continue;

        /* parse command and arg */
        char cmd[64], arg[LINE_BUF];
        cmd[0] = arg[0] = '\0';
        int n = sscanf(line, "%63s %[^\n]", cmd, arg);

        if (strcmp(cmd, "quit") == 0 || strcmp(cmd, "exit") == 0) break;
        else if (strcmp(cmd, "help") == 0) show_help();
        else if (strcmp(cmd, "add") == 0) add_task_interactive(&tl);
        else if (strcmp(cmd, "list") == 0) list_tasks(&tl);
        else if (strcmp(cmd, "save") == 0) { save_tasks(&tl); puts("Saved."); }
        else if (strcmp(cmd, "view") == 0) {
            if (n < 2) puts("Usage: view <id>");
            else view_task(&tl, atoi(arg));
        }
        else if (strcmp(cmd, "edit") == 0) {
            if (n < 2) puts("Usage: edit <id>");
            else edit_task(&tl, atoi(arg));
        }
        else if (strcmp(cmd, "done") == 0) {
            if (n < 2) puts("Usage: done <id>");
            else {
                Task *t = tl_find_by_id(&tl, atoi(arg));
                if (t) { t->done = 1; save_tasks(&tl); puts("Marked done."); }
                else puts("Not found.");
            }
        }
        else if (strcmp(cmd, "undone") == 0) {
            if (n < 2) puts("Usage: undone <id>");
            else {
                Task *t = tl_find_by_id(&tl, atoi(arg));
                if (t) { t->done = 0; save_tasks(&tl); puts("Marked not done."); }
                else puts("Not found.");
            }
        }
        else if (strcmp(cmd, "rm") == 0) {
            if (n < 2) puts("Usage: rm <id>");
            else {
                if (tl_remove_by_id(&tl, atoi(arg))) { save_tasks(&tl); puts("Removed."); }
                else puts("Not found.");
            }
        }
        else if (strcmp(cmd, "search") == 0) {
            if (n < 2) puts("Usage: search <query>");
            else search_tasks(&tl, arg);
        }
        else {
            printf("Unknown command: %s\n", cmd);
            puts("Type 'help' for commands.");
        }
    }

    save_tasks(&tl);
    tl_free(&tl);
    puts("Goodbye.");
    return 0;
}

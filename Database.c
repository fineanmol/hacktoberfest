/*EXPERIMENT : 03
Name : Shrusti Moon
Roll no : UEC2024145

Expt 03 : 3. 
Create a database of students using array of structures with attributes; roll no, name, program,
course, marks obtained for different subjects with their total and average. 
Implement the following operations on the database:
a) Display the database in a tabular form.
b) Modify (should be able to modify each field of the database)
c) Append (add a new record to the existing database)
d) Search for a particular record from the database.
e) Sort the records in the database.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Student {
    int roll_no;
    char name[20];
    int marks_SS, marks_DT, marks_DE;
    int total;
    float average;
} Student;

// Display function
void display(Student s[], int n) {
    printf("\nSTUDENT DATABASE\n");
    printf("Roll No\tName\t\tMarks_SS\tMarks_DT\tMarks_DE\tTotal\tAverage\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%s\t\t%d\t\t%d\t\t%d\t\t%d\t%.2f\n",
               s[i].roll_no, s[i].name, s[i].marks_SS,
               s[i].marks_DT, s[i].marks_DE, s[i].total, s[i].average);
    }
}

// Search by name
void search(Student s[], int n) {
    char search_name[20];
    int found = 0;
    printf("Enter name to search: ");
    scanf("%s", search_name);
    for (int i = 0; i < n; i++) {
        if (strcmp(s[i].name, search_name) == 0) {
            printf("Record found:\n");
            printf("%d\t%s\t\t%d\t\t%d\t\t%d\t\t%d\t%.2f\n",
                   s[i].roll_no, s[i].name, s[i].marks_SS,
                   s[i].marks_DT, s[i].marks_DE, s[i].total, s[i].average);
            found = 1;
            break;
        }
    }
    if (!found)
        printf("Record not found.\n");
}

// Modify student
void modify(Student s[], int n) {
    int roll, choice, found = 0;
    printf("Enter roll number to modify: ");
    scanf("%d", &roll);

    for (int i = 0; i < n; i++) {
        if (s[i].roll_no == roll) {
            found = 1;
            printf("What to modify?\n1. Name\n2. Marks SS\n3. Marks DT\n4. Marks DE\nChoice: ");
            scanf("%d", &choice);

            switch(choice) {
                case 1:
                    printf("Enter new name: ");
                    scanf("%s", s[i].name);
                    break;
                case 2:
                    printf("Enter new marks SS: ");
                    scanf("%d", &s[i].marks_SS);
                    break;
                case 3:
                    printf("Enter new marks DT: ");
                    scanf("%d", &s[i].marks_DT);
                    break;
                case 4:
                    printf("Enter new marks DE: ");
                    scanf("%d", &s[i].marks_DE);
                    break;
                default:
                    printf("Invalid choice!\n");
            }

            s[i].total = s[i].marks_SS + s[i].marks_DT + s[i].marks_DE;
            s[i].average = s[i].total / 3.0;

            printf("Record updated:\n");
            display(s, n);
            break;
        }
    }
    if (!found)
        printf("Roll number not found.\n");
}

// Sort by roll number
void sort(Student s[], int n) {
    Student temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (s[i].roll_no > s[j].roll_no) {
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    printf("Data sorted by roll number:\n");
    display(s, n);
}

// Append students
int append(Student s[], int n) {
    int m;
    printf("Enter number of students to append: ");
    scanf("%d", &m);

    Student temp[n + m];

    // Copy old students
    for (int i = 0; i < n; i++)
        temp[i] = s[i];

    // Input new students
    for (int i = n; i < n + m; i++) {
        printf("Enter Roll No: ");
        scanf("%d", &temp[i].roll_no);
        printf("Enter Name: ");
        scanf("%s", temp[i].name);
        printf("Marks SS: ");
        scanf("%d", &temp[i].marks_SS);
        printf("Marks DT: ");
        scanf("%d", &temp[i].marks_DT);
        printf("Marks DE: ");
        scanf("%d", &temp[i].marks_DE);

        temp[i].total = temp[i].marks_SS + temp[i].marks_DT + temp[i].marks_DE;
        temp[i].average = temp[i].total / 3.0;
    }

    // Copy back to original array
    for (int i = 0; i < n + m; i++)
        s[i] = temp[i];

    display(s, n + m);
    return n + m;
}

int main() {
    int n, choice;

    printf("Enter initial number of students: ");
    scanf("%d", &n);

    Student s[100]; // fixed array larger than initial n to allow appends

    // Input initial students
    for (int i = 0; i < n; i++) {
        printf("Enter Roll No: ");
        scanf("%d", &s[i].roll_no);
        printf("Enter Name: ");
        scanf("%s", s[i].name);
        printf("Marks SS: ");
        scanf("%d", &s[i].marks_SS);
        printf("Marks DT: ");
        scanf("%d", &s[i].marks_DT);
        printf("Marks DE: ");
        scanf("%d", &s[i].marks_DE);

        s[i].total = s[i].marks_SS + s[i].marks_DT + s[i].marks_DE;
        s[i].average = s[i].total / 3.0;
    }

    display(s, n);

    // Menu loop
    while (1) {
        printf("\nMenu:\n1. Display\n2. Modify\n3. Append\n4. Search\n5. Sort\n6. Exit\nChoice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                display(s, n);
                break;
            case 2:
                modify(s, n);
                break;
            case 3:
                n = append(s, n);
                break;
            case 4:
                search(s, n);
                break;
            case 5:
                sort(s, n);
                break;
            case 6:
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }

    return 0;
}

/* OUTPUT :

Enter initial number of students: 5
Enter Roll No: 01
Enter Name: Saniya
Marks SS: 23
Marks DT: 24
Marks DE: 11
Enter Roll No: 02
Enter Name: Ananya
Marks SS: 25
Marks DT: 12
Marks DE: 15
Enter Roll No: 03
Enter Name: Tanusha
Marks SS: 12
Marks DT: 24
Marks DE: 22
Enter Roll No: 04
Enter Name: Veena
Marks SS: 23
Marks DT: 24
Marks DE: 12
Enter Roll No: 05
Enter Name: Anita
Marks SS: 22
Marks DT: 25
Marks DE: 12

STUDENT DATABASE
Roll No Name            Marks_SS        Marks_DT        Marks_DE        Total   Average
1       Saniya          23              24              11              58      19.33
2       Ananya          25              12              15              52      17.33
3       Tanusha         12              24              22              58      19.33
4       Veena           23              24              12              59      19.67
5       Anita           22              25              12              59      19.67

Menu:
1. Display
2. Modify
3. Append
4. Search
5. Sort
6. Exit
Choice: 1

STUDENT DATABASE
Roll No Name            Marks_SS        Marks_DT        Marks_DE        Total   Average
1       Saniya          23              24              11              58      19.33
2       Ananya          25              12              15              52      17.33
3       Tanusha         12              24              22              58      19.33
4       Veena           23              24              12              59      19.67
5       Anita           22              25              12              59      19.67

Menu:
1. Display
2. Modify
3. Append
4. Search
5. Sort
6. Exit
Choice: 2
Enter roll number to modify: 2
What to modify?
1. Name
2. Marks SS
3. Marks DT
4. Marks DE
Choice: 3
Enter new marks DT: 23
Record updated:

STUDENT DATABASE
Roll No Name            Marks_SS        Marks_DT        Marks_DE        Total   Average
1       Saniya          23              24              11              58      19.33
2       Ananya          25              23              15              63      21.00
3       Tanusha         12              24              22              58      19.33
4       Veena           23              24              12              59      19.67
5       Anita           22              25              12              59      19.67

Menu:
1. Display
2. Modify
3. Append
4. Search
5. Sort
6. Exit
Choice: 3
Enter number of students to append: 2
Enter Roll No: 07
Enter Name: Elisha
Marks SS: 22
Marks DT: 25
Marks DE: 14
Enter Roll No: 06
Enter Name: Tina
Marks SS: 22
Marks DT: 12
Marks DE: 21

STUDENT DATABASE
Roll No Name            Marks_SS        Marks_DT        Marks_DE        Total   Average
1       Saniya          23              24              11              58      19.33
2       Ananya          25              23              15              63      21.00
3       Tanusha         12              24              22              58      19.33
4       Veena           23              24              12              59      19.67
5       Anita           22              25              12              59      19.67
7       Elisha          22              25              14              61      20.33
6       Tina            22              12              21              55      18.33

Menu:
1. Display
2. Modify
3. Append
4. Search
5. Sort
6. Exit
Choice: 4
Enter name to search: Tina
Record found:
6       Tina            22              12              21              55      18.33

Menu:
1. Display
2. Modify
3. Append
4. Search
5. Sort
6. Exit
Choice: 5
Data sorted by roll number:

STUDENT DATABASE
Roll No Name            Marks_SS        Marks_DT        Marks_DE        Total   Average
1       Saniya          23              24              11              58      19.33
2       Ananya          25              23              15              63      21.00
3       Tanusha         12              24              22              58      19.33
4       Veena           23              24              12              59      19.67
5       Anita           22              25              12              59      19.67
6       Tina            22              12              21              55      18.33
7       Elisha          22              25              14              61      20.33

Menu:
1. Display
2. Modify
3. Append
4. Search
5. Sort
6. Exit
Choice: 6

*/
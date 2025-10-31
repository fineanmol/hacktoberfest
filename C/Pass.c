#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generatePassword(int length) {
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?";
    int charsetSize = sizeof(charset) - 1;  // exclude '\0'

    char password[length + 1];
    srand(time(NULL));  // seed random number

    for (int i = 0; i < length; i++) {
        int key = rand() % charsetSize;
        password[i] = charset[key];
    }

    password[length] = '\0';  // null terminate string

    printf("🔐 Generated Password: %s\n", password);
}

int main() {
    int length;

    printf("Enter desired password length: ");
    scanf("%d", &length);

    if (length < 4) {
        printf("Password length should be at least 4 characters!\n");
        return 1;
    }

    generatePassword(length);

    return 0;
}

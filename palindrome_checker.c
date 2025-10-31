#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char str[]) {
    int left = 0;
    int right = strlen(str) - 1;

    while (left < right) {
        // Ignore non-alphanumeric characters and case
        while (left < right && !isalnum(str[left])) left++;
        while (left < right && !isalnum(str[right])) right--;

        if (tolower(str[left]) != tolower(str[right]))
            return 0;
        left++;
        right--;
    }
    return 1;
}

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0'; // remove newline

    if (isPalindrome(str))
        printf("The given string is a palindrome.\n");
    else
        printf("The given string is not a palindrome.\n");

    return 0;
}

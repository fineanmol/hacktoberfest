import java.util.Scanner;

public class Longest_palindrome {
    private int start = 0, maxLength = 0;

    public String longestPalindrome(String s) {
        int n = s.length();
        if (n < 2) {
            return s;
        }

        for (int i = 0; i < n - 1; i++) {
            expandAroundCenter(s, i, i);       // Odd length palindrome
            expandAroundCenter(s, i, i + 1);   // Even length palindrome
        }

        return s.substring(start, start + maxLength);
    }

    private void expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        int length = right - left - 1;
        if (length > maxLength) {
            start = left + 1;
            maxLength = length;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        Longest_palindrome lp = new Longest_palindrome();
        String result = lp.longestPalindrome(input);

        System.out.println("Longest Palindromic Substring: " + result);
        sc.close();
    }
}
/*Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
  */
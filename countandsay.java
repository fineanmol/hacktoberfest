import java.util.HashMap;
import java.util.Map;

public class Solution{

    public static String build(String str) {
        Map<Character, Integer> fq = new HashMap<>();
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < str.length() - 1; i++) {
            char num = str.charAt(i);

            if (str.charAt(i) == str.charAt(i + 1)) {
                fq.put(num, fq.getOrDefault(num, 0) + 1);
            } else {
                ans.append((char) ('0' + fq.getOrDefault(str.charAt(i), 0) + 1));
                ans.append(str.charAt(i));
                fq.put(str.charAt(i), 0);
            }
        }

        int n = str.length() - 1;

        ans.append((char) ('0' + fq.getOrDefault(str.charAt(n), 0) + 1));
        ans.append(str.charAt(n));

        return ans.toString();
    }

    public static String writeAsYouSpeak(int n) {
        StringBuilder initial = new StringBuilder("1");

        if (n == 1) {
            return "1";
        }

        for (int i = 1; i < n; i++) {
            initial = new StringBuilder(build(initial.toString()));
        }

        return initial.toString();
    }

    public static void main(String[] args) {
        // Example usage:
        System.out.println(writeAsYouSpeak(5));
    }
}

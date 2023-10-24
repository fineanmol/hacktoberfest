// LANGUAGE: Java
// AUTHOR: Shlok Chaitanya
// GITHUB: https://github.com/shlokchaitaya

public class Main {
    public static void main(String[] args) {
        String h = "hello world";
        String abc = "abcdefghijklmnopqrstuvwxyz";
        String s = "";
        for (int i = 0; i < h.length(); i++) {
            for (int j = 0; j <= abc.length(); j++) {
                if (h.charAt(i) == ' ') {
                    System.out.print(" ");
                    s = s + " ";
                    break;
                }
                if (abc.charAt(j) == h.charAt(i) || abc.charAt(j) != h.charAt(i)) {
                    System.out.println(s + abc.charAt(j));
                    if (abc.charAt(j) == h.charAt(i)) {
                        s = s + abc.charAt(j);
                        break;
                    }
                }
            }
        }
    }
}

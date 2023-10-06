public class HelloWorld {
    public static void main(String[] a) {
        String s = "";for(int i= ((int) 'H' / 3 * 3); i <= 'W' * 2; i+=3){s+=(char)i;if(i== ((int) 'd' / 2 * 2)){i+=((int)' '/2*2);}}for(int i=('o'*2); i<=('d'*3);i+=((int)' '/2*2)){s+=(char)i;}for(int i=('W'*2);i<=('l'*5);i+=((int)' '/2*2)){s+=(char)i;}System.out.println(s+(char)('d'*2-' '));}}

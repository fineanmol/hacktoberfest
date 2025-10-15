import java.util.*;

public class BubbleSortInput {
    public static void bubbleSort(int[] a, boolean ascending) {
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                boolean outOfOrder = ascending ? a[j] > a[j + 1] : a[j] < a[j + 1];
                if (outOfOrder) {
                    int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter count n: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        System.out.print("Choose order (1=Ascending, 2=Descending): ");
        int choice = sc.nextInt();
        boolean ascending = choice != 2; // default to ascending on invalid choice

        bubbleSort(arr, ascending);

        System.out.println((ascending ? "Sorted (asc): " : "Sorted (desc): ") + Arrays.toString(arr));
        sc.close();
    }
}

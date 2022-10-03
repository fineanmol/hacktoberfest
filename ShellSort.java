public class ShellSort
{
    public static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
  
    public int sort(int arr[])
    {
        int n = arr.length;
        for (int k = n/2; k > 0; k /= 2)
        {
            for (int i = k; i < n; i += 1)
            {
                int temp = arr[i];
                int j;
                for (j = i; j >= k && arr[j - k] > temp; j -= k)
                    arr[j] = arr[j - k];

                arr[j] = temp;
            }
        }
        return 0;
    }

    public static void main(String args[])
    {
        int arr[] = {12, 34, 54, 2, 3};
        System.out.println("Array before sorting");
        printArray(arr);
  
        ShellSort ob = new ShellSort();
        ob.sort(arr);
  
        System.out.println("Array after sorting");
        printArray(arr);
    }
} 

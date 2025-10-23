import java.util.Scanner;

public class twoSum
{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    System.out.println("Enter size of array: ");
    int n = sc.nextInt();
    int arr[] = new int[n];
    
    System.out.println("Enter elements of array: ");
    for(int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    
    System.out.println("Enter target sum: ");
    int target = sc.nextInt();
    
    int index1 = -1, index2 = -1;
    
    // Find two numbers that add up to target
    for(int i = 0; i < n; i++) {
      for(int j = i + 1; j < n; j++) {
        if(arr[i] + arr[j] == target) {
          index1 = i;
          index2 = j;
          break;
        }
      }
      if(index1 != -1) break;
    }
    
    if(index1 != -1)
      System.out.println("Indices: " + index1 + " and " + index2);
    else
      System.out.println("No two numbers add up to target.");
  }
}


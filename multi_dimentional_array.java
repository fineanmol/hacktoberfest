package Array;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class multi_dimentional_array {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        /*
        1 2 3
        4 5 6
        7 8 9
         */
        //int []  means 1 d array
        //int[][] means 2 d array
        //int[][] = new int[1][] adding rows value is important
        //adding value of colum in not mandatory


//        int[][] arr= new int[3][];

//        int[][] arr = {
//                {1 ,2 ,3}, // 0  index
//                {4, 5, 6}, // 1  index
//                {7, 8, 9}  // 2  index
//        };
        // imagine it as array of arrays
        //print output arr[1] = [4 , 5 , 6]
        //print output arr[1][0] = [4]

        int[][] arr2D = {
                {1 ,2 ,3}, // 0  index
                {4, 5},    // 1  index
                {6, 7, 8, 9}  // 2  index
        };

        int[][] arr = new int[3][3];
        //taking input in 2d array
        for (int row = 0; row < arr.length; row++) {

            for (int col = 0; col < arr[row].length; col++) {

                arr[row][col] = in.nextInt();
            }

        }

        //output
//        for (int row = 0; row < arr.length; row++) {
//
//            for (int col = 0; col < arr[row].length; col++) {
//
//                System.out.print(arr[row][col] + " ");
//            }
//            System.out.println();
//        }

        //output enhanced
        for (int row = 0; row < arr.length; row++) {

            System.out.println(Arrays.toString(arr[row]));
        }
    }
}

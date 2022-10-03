package Array;

import java.util.Arrays;
import java.util.Scanner;

public class arrays {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        //syntax
        //datatype[] variable name = new datatype [size]
        //store 5 roll numbers :
//        int[] rnos = new int[5];
//        //or directly can write
//        int[] rons2 = {1,2,3,4,5,6,7};

//        int[] ros; //decleration of array is getting defined in the stack.
//        ros = new int[5];//initialisation: here objects is being created in the heap.
//        System.out.println(ros[3]);
//
//        String[] arr = new String[5];
//        System.out.println(arr[4]);


        //input in array
       // int[] arr = new int[5];
//        arr[0] = 22;
//        arr[1] = 2;
//        arr[2] = 27;
//        arr[3] = 7;
//        arr[4] = 92;
//        //[22,2,27,7,92]
//        System.out.println(arr[3]);


        //input in array in for loop
//        int[] arr = new int[5];
//        for (int i =0; i<arr.length; i++){
//            arr[i] = in.nextInt();
//
//        }
//        for (int i =0; i<arr.length; i++){
//            System.out.print(arr[i] + " ");
//
//        }
//        System.out.println(Arrays.toString(arr));





        //array of objects

        String[] str = new String[4];
        for (int i = 0; i< str.length; i++){
            str[i] = in.next();
        }
        System.out.println(Arrays.toString(str));


        //modify
        str[0] = "Anoop";
        System.out.println(Arrays.toString(str));


    }
}

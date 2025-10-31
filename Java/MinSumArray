public class MinSumArray {

    public static int minSumArray(int arr[]) {


        int res=arr[0];
        int minValue=arr[0];

        for (int i = 1; i < arr.length; i++) {

            minValue=Math.min(minValue+arr[i], arr[i]);


            res=Math.min(minValue, res);



        }


        return res;
    }

    public static void main(String[] args) {

        int arr[]= {2, 3, 5, -2, -7, 4,-8};

        System.out.println(minSumArray(arr));

    }
}

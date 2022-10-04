import java.util.Scanner
import java.lang.*

object MergeSort {
    @JvmStatic
    fun main(args: Array<String>) {
        val sc = Scanner(System.`in`)
        println("Enter the size of array")
        val n = sc.nextInt()
        val arr = IntArray(n)
        println("Enter the elements of array to be sorted")
        for (i in 0 until n) {
            arr[i] = sc.nextInt()
        }

        mergeSort(arr, 0, arr.size - 1)
        println("Sorted array is ")
        for (`val` in arr) {
            println("$`val` ")
        }

    }

    private fun mergeSort(arr: IntArray, left: Int, right: Int) {

        if (left < right) {
            val m = (left + right) / 2
            mergeSort(arr, left, m)
            mergeSort(arr, m + 1, right)
            merge(arr, left, right, m)
        }
    }

    private fun merge(arr: IntArray, left: Int, right: Int, m: Int) {

        val n1 = m - left + 1
        val n2 = right - m

        val L = IntArray(n1)
        val R = IntArray(n2)

        for (i in 0 until n1) {
            L[i] = arr[i + left]
        }
        for (j in 0 until n2) {
            R[j] = arr[m + 1 + j]
        }

        var i = 0
        var j = 0
        var k = left
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i]
                i++
            } else {
                arr[k] = R[j]
                j++
            }
            k++
        }

        while (i < n1) {
            arr[k] = L[i]
            i++
            k++
        }
        while (j < n2) {
            arr[k] = R[j]
            j++
            k++
        }
    }
}
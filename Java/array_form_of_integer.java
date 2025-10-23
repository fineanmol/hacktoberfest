// leetcode 989. Add to Array-Form of Integer
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
class array_form_of_integer {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> result = new ArrayList<>();
        int i = num.length - 1;

        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i];  // add current digit to k
                i--;
            }
            result.add(k % 10);  // take last digit
            k /= 10;             // move to next
        }

        Collections.reverse(result);
        return result;
    }
}
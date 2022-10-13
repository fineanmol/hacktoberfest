/*
Following function is a simple binary serach algorithm to find/serach for value from a list.
Time complexity:  O(log n). If the input halves at each step, its likely O(LogN) or O(NlogN)
Worst case scenario: When value is not in array and we have to itereate through it over and over again. 
*/

function bs_list(haystack: number[], needle: number): boolean {
    // lowest value is always inclusive
    let low = 0;
    // highest value is always exclusive
    let high = haystack.length;

    // Following block of code goes from low to high and find the middle point
    do {
        const midpoint = Math.floor(low + (high - low) / 2);
        const value = haystack[midpoint];

        if (value === needle) {
            return true;
        } else if (value > needle) {
            high = midpoint;
            // low = midpoint + 1;
        }
        else {
            low = midpoint + 1;
            // high = midpoint;
        }

    } while (low < high);

    return false;
}
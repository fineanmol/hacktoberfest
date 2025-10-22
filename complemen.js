function twoSum(arr, target) {

    // Create a Set to store the elements
    let set = new Set();

    for (let num of arr) {
    
        // Calculate the complement that added to
        // num, equals the target
        let complement = target - num;

        // Check if the complement exists in the set
        if (set.has(complement)) {
            return true;
        }

        // Add the current element to the set
        set.add(num);
    }
    // If no pair is found
    return false;
}

// Driver Code
let arr = [0, -1, 2, -3, 1];
let target = -2;

if (twoSum(arr, target))
    console.log("true");
else 
    console.log("false");

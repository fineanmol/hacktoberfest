/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function (arr, n) {
    // Base case: if n = 0, return arr as is
    if (n === 0) return arr;

    let result = [];

    for (let element of arr) {
        if (Array.isArray(element) && n > 0) {
            // Recursively flatten the sub-array with depth reduced by 1
            result.push(...flat(element, n - 1));
        } else {
            result.push(element);
        }
    }

    return result;
};

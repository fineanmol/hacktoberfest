<script>
/*package whatever //do not write package name here */
function solveWordWrap(nums , k) {
		var memo = Array(nums.length).fill().map(()=>Array(k + 1).fill(-1));
		return solveWordWrapUsingMemo(nums, nums.length, k, 0, k, memo);
	}

	function solveWordWrap1(words , n , length , wordIndex , remLength, memo) {

		// base case for last word
		if (wordIndex == n - 1) {
			memo[wordIndex][remLength] = words[wordIndex] < remLength ? 0 : square(remLength);
			return memo[wordIndex][remLength];
		}

		var currWord = words[wordIndex];
		// if word can fit in the remaining line
		if (currWord < remLength) {
			return Math.min(
					// if word is kept on same line
					solveWordWrapUsingMemo(words, n, length, wordIndex + 1,
							remLength == length ? remLength - currWord : remLength - currWord - 1, memo),
					// if word is kept on next line
					square(remLength)
							+ solveWordWrapUsingMemo(words, n, length, wordIndex + 1, length - currWord, memo));
		} else {
			// if word is kept on next line
			return square(remLength) + solveWordWrapUsingMemo(words, n, length, wordIndex + 1, length - currWord, memo);
		}
	}

	function solveWordWrapUsingMemo(words , n , length , wordIndex , remLength, memo) {
		//if (memo[wordIndex][remLength] != -1) {
		// return memo[wordIndex][remLength];
		//}

		memo[wordIndex][remLength] = solveWordWrap1(words, n, length, wordIndex, remLength, memo);
		return memo[wordIndex][remLength];
	}

	function square(n) {
		return n * n;
	}

	var arr = [ 3, 2, 2, 5 ];
		document.write(solveWordWrap(arr, 6));

// This code is contributed by gauravrajput1 
</script>

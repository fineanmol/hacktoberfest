<script>

// Javascript program to print
// matrix in snake order
let M = 4;
let N = 4;

function print(mat)
{
	
	// Traverse through all rows
	for(let i = 0; i < M; i++) 
	{
		
		// If current row is even, print from
		// left to right
		if (i % 2 == 0) 
		{
			for(let j = 0; j < N; j++)
				document.write(mat[i][j] + " ");

		// If current row is odd, print from
		// right to left
		} 
		else
		{
			for(let j = N - 1; j >= 0; j--)
				document.write(mat[i][j] + " ");
		}
	}
}

// Driver code
let mat = [ [ 10, 20, 30, 40 ],
			[ 15, 25, 35, 45 ],
			[ 27, 29, 37, 48 ],
			[ 32, 33, 39, 50 ] ];

print(mat);

// This code is contributed by rameshtravel07
</script>

public class cells_with_odd_values_in_matrix {
      public int oddCells(int m, int n, int[][] indices) {
        int[][] matrix = new int[m][n];

        // Apply all operations
        for (int i = 0; i < indices.length; i++) {
            int r = indices[i][0];
            int c = indices[i][1];

            // Increment row r
            for (int j = 0; j < n; j++) {
                matrix[r][j]++;
            }

            // Increment column c
            for (int row = 0; row < m; row++) {
                matrix[row][c]++;
            }
        }

        // Count odd numbers
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] % 2 != 0) {
                    result++;
                }
            }
        }

        return result;
    }
	
}

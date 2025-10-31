public class SudokuSolver {
    public static boolean solve(int[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    for (int num = 1; num <= 9; num++) {
                        if (isSafe(board, i, j, num)) {
                            board[i][j] = num;
                            if (solve(board))
                                return true;
                            board[i][j] = 0; // backtrack
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isSafe(int[][] board, int row, int col, int num) {
        for (int k = 0; k < 9; k++)
            if (board[row][k] == num || board[k][col] == num)
                return false;

        int sr = row - row % 3, sc = col - col % 3;
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                if (board[sr + r][sc + c] == num)
                    return false;

        return true;
    }

    public static void main(String[] args) {
        int[][] board = {
            {5,3,0,0,7,0,0,0,0},
            {6,0,0,1,9,5,0,0,0},
            {0,9,8,0,0,0,0,6,0},
            {8,0,0,0,6,0,0,0,3},
            {4,0,0,8,0,3,0,0,1},
            {7,0,0,0,2,0,0,0,6},
            {0,6,0,0,0,0,2,8,0},
            {0,0,0,4,1,9,0,0,5},
            {0,0,0,0,8,0,0,7,9}
        };
        solve(board);
        for (int[] row : board) {
            for (int num : row) System.out.print(num + " ");
            System.out.println();
        }
    }
}

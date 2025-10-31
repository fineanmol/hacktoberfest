import java.util.*;

public class NQueens {
    public static void solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] row : board)
            Arrays.fill(row, '.'); 
        
        List<List<String>> solutions = new ArrayList<>();
        placeQueens(board, 0, solutions);
        
        for (List<String> sol : solutions) {
            for (String row : sol)
                System.out.println(row);
            System.out.println();
        }
    }

    private static void placeQueens(char[][] board, int row, List<List<String>> solutions) {
        int n = board.length;
        if (row == n) {
            solutions.add(construct(board));
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                placeQueens(board, row + 1, solutions);
                board[row][col] = '.'; // backtrack
            }
        }
    }

    private static boolean isSafe(char[][] board, int row, int col) {
        int n = board.length;

        
        for (int i = 0; i < row; i++)
            if (board[i][col] == 'Q') return false;

    
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 'Q') return false;


        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
            if (board[i][j] == 'Q') return false;

        return true;
    }

    private static List<String> construct(char[][] board) {
        List<String> res = new ArrayList<>();
        for (char[] row : board)
            res.add(new String(row));
        return res;
    }

    public static void main(String[] args) {
        int n = 4; // Change this to test with different board sizes
        solveNQueens(n);
    }
}

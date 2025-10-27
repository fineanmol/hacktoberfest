public class WordSearch {
    public static boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                if (dfs(board, i, j, word, 0))
                    return true;
        return false;
    }

    private static boolean dfs(char[][] board, int i, int j, String word, int idx) {
        if (idx == word.length()) return true;
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || board[i][j] != word.charAt(idx))
            return false;

        char temp = board[i][j];
        board[i][j] = '#'; // mark visited
        boolean found = dfs(board, i + 1, j, word, idx + 1) ||
                        dfs(board, i - 1, j, word, idx + 1) ||
                        dfs(board, i, j + 1, word, idx + 1) ||
                        dfs(board, i, j - 1, word, idx + 1);
        board[i][j] = temp; // backtrack
        return found;
    }

    public static void main(String[] args) {
        char[][] board = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        System.out.println(exist(board, "ABCCED")); // true
        System.out.println(exist(board, "SEE"));    // true
        System.out.println(exist(board, "ABCB"));   // false
    }
}

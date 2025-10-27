import java.util.*;

public class RatInMaze {
    static void solve(int[][] maze, int n) {
        int[][] path = new int[n][n];
        backtrack(maze, 0, 0, n, path);
    }

    static void backtrack(int[][] maze, int i, int j, int n, int[][] path) {
        if (i < 0 || j < 0 || i >= n || j >= n || maze[i][j] == 0 || path[i][j] == 1)
            return;

        if (i == n - 1 && j == n - 1) {
            path[i][j] = 1;
            printPath(path);
            path[i][j] = 0;
            return;
        }

        path[i][j] = 1;
        backtrack(maze, i + 1, j, n, path); // down
        backtrack(maze, i - 1, j, n, path); // up
        backtrack(maze, i, j + 1, n, path); // right
        backtrack(maze, i, j - 1, n, path); // left
        path[i][j] = 0;
    }

    static void printPath(int[][] path) {
        for (int[] row : path) {
            for (int val : row)
                System.out.print(val + " ");
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[][] maze = {{1, 0, 0}, {1, 1, 0}, {0, 1, 1}};
        solve(maze, 3);
    }
}

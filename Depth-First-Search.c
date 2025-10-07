#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int adj[MAX][MAX];
int visited[MAX];
int n;

void DFS(int v) {
    visited[v] = 1;
    printf("%d ", v);
    for(int i=0; i<n; i++) {
        if(adj[v][i] && !visited[i]) DFS(i);
    }
}

int main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter adjacency matrix:\n");
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            scanf("%d", &adj[i][j]);

    for(int i=0; i<n; i++) visited[i] = 0;
    printf("DFS starting from vertex 0: ");
    DFS(0);
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

struct node
{
    int data;
    struct node *left, *right;
};

vector<vector<int>> findVertical(node *root)
{
    map<int, map<int, multiset<int>>> nodes;
    queue<pair<node *, pair<int, int>>> todo;
    todo.push({root,
               {0,
                0}}); // initial vertical and level
    while (!todo.empty())
    {
        auto p = todo.front();
        todo.pop();
        node *temp = p.first;

        // x -> vertical , y->level
        int x = p.second.first, y = p.second.second;
        nodes[x][y].insert(temp->data); // inserting to multiset

        if (temp->left)
        {
            todo.push({temp->left,
                       {x - 1,
                        y + 1}});
        }
        if (temp->right)
        {
            todo.push({temp->right,
                       {x + 1,
                        y + 1}});
        }
    }
    vector<vector<int>> ans;
    for (auto p : nodes)
    {
        vector<int> col;
        for (auto q : p.second)
        {
            col.insert(col.end(), q.second.begin(), q.second.end());
        }
        ans.push_back(col);
    }
    return ans;
}

struct node *newNode(int data)
{
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return (node);
}

int main()
{

    struct node *root = newNode(1);
    root->left = newNode(2);
    root->left->left = newNode(4);
    root->left->right = newNode(10);
    root->left->left->right = newNode(5);
    root->left->left->right->right = newNode(6);
    root->right = newNode(3);
    root->right->left = newNode(9);
    root->right->right = newNode(10);

    vector<vector<int>> verticalTraversal;
    verticalTraversal = findVertical(root);

    cout << "The Vertical Traversal is : " << endl;
    for (auto vertical : verticalTraversal)
    {
        for (auto nodeVal : vertical)
        {
            cout << nodeVal << " ";
        }
        cout << endl;
    }
    return 0;
}

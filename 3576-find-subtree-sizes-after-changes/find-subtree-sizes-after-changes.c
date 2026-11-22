/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSubtreeSizes(int* parent, int parentSize, char* s, int* returnSize) {
    int* adj_size = (int*)calloc(parentSize, sizeof(int));
    for (int i = 1; i < parentSize; i++) {
        adj_size[parent[i]]++;
    }
    
    int** adj = (int**)malloc(parentSize * sizeof(int*));
    int* current_idx = (int*)calloc(parentSize, sizeof(int));
    for (int i = 0; i < parentSize; i++) {
        adj[i] = (int*)malloc(adj_size[i] * sizeof(int));
    }
    for (int i = 1; i < parentSize; i++) {
        int u = parent[i];
        int v = i;
        adj[u][current_idx[u]++] = v;
    }
    
    int* new_parent = (int*)malloc(parentSize * sizeof(int));
    for (int i = 0; i < parentSize; i++) {
        new_parent[i] = parent[i];
    }
    
    int* char_ancestor = (int*)malloc(26 * sizeof(int));
    for (int i = 0; i < 26; i++) {
        char_ancestor[i] = -1;
    }
    
    void dfs1(int u) {
        int c = s[u] - 'a';
        int prev = char_ancestor[c];
        if (prev != -1) {
            new_parent[u] = prev;
        }
        char_ancestor[c] = u;
        
        for (int i = 0; i < adj_size[u]; i++) {
            dfs1(adj[u][i]);
        }
        
        char_ancestor[c] = prev;
    }
    
    dfs1(0);
    
    for (int i = 0; i < parentSize; i++) {
        adj_size[i] = 0;
        free(adj[i]);
    }
    free(adj);
    free(current_idx);
    
    for (int i = 1; i < parentSize; i++) {
        adj_size[new_parent[i]]++;
    }
    
    adj = (int**)malloc(parentSize * sizeof(int*));
    current_idx = (int*)calloc(parentSize, sizeof(int));
    for (int i = 0; i < parentSize; i++) {
        adj[i] = (int*)malloc(adj_size[i] * sizeof(int));
    }
    for (int i = 1; i < parentSize; i++) {
        int u = new_parent[i];
        int v = i;
        adj[u][current_idx[u]++] = v;
    }
    
    int* subtree_size = (int*)malloc(parentSize * sizeof(int));
    
    int dfs2(int u) {
        int sz = 1;
        for (int i = 0; i < adj_size[u]; i++) {
            sz += dfs2(adj[u][i]);
        }
        subtree_size[u] = sz;
        return sz;
    }
    
    dfs2(0);
    
    *returnSize = parentSize;
    
    for (int i = 0; i < parentSize; i++) {
        free(adj[i]);
    }
    free(adj);
    free(adj_size);
    free(current_idx);
    free(new_parent);
    free(char_ancestor);
    
    return subtree_size;
}
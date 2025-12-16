class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        // build tree
        vector<vector<int>> g(n + 1);
        for (auto &e : hierarchy) {
            g[e[0]].push_back(e[1]);
        }
        
        function<vector<array<int,2>>(int)> dfs = [&](int u) {
            // nxt[b][pre]: best profit from children with b budget,
            // pre = 0 (parent didn't buy) or 1 (parent did buy → discount possible)
            vector<array<int,2>> nxt(budget + 1, {0, 0});
            
            // combine children DP into nxt
            for (int v : g[u]) {
                auto fv = dfs(v);
                // merge knapsack
                for (int j = budget; j >= 0; j--) {
                    array<int,2> old = nxt[j];
                    for (int jv = 0; jv <= j; jv++) {
                        for (int pre = 0; pre < 2; pre++) {
                            int cand = nxt[j - jv][pre] + fv[jv][pre];
                            nxt[j][pre] = max(nxt[j][pre], cand);
                        }
                    }
                }
            }
            
            // now consider buying u with/without discount
            vector<array<int,2>> f(budget + 1, {0, 0});
            int price = future[u - 1];
            for (int j = 0; j <= budget; j++) {
                for (int pre = 0; pre < 2; pre++) {
                    int cost = present[u - 1] / (pre + 1);
                    if (j >= cost) {
                        // either skip buying u: nxt[j][0]
                        // or buy u: nxt[j-cost][1] + profit (future - cost)
                        f[j][pre] = max(nxt[j][0], nxt[j - cost][1] + (price - cost));
                    } else {
                        f[j][pre] = nxt[j][0];
                    }
                }
            }
            
            return f;
        };
        
        // start at root 1 with full budget and no parent discount
        return dfs(1)[budget][0];
    }
};

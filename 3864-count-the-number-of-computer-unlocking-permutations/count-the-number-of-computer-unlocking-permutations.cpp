class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        const long long MOD = 1000000007;
        int n = complexity.size();

        // Check if every complexity[i] > complexity[0] for i >= 1
        for (int i = 1; i < n; i++) {
            if (complexity[i] <= complexity[0]) return 0;
        }

        // Compute (n-1)! % MOD
        long long ans = 1;
        for (int i = 1; i < n; i++) {
            ans = (ans * i) % MOD;
        }

        return ans;
    }
};

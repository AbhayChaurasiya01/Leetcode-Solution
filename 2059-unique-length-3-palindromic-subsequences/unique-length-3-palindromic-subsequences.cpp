class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<int> first(26, -1), last(26, -1);

        // Store first & last occurrence of each character
        for (int i = 0; i < s.size(); i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        int ans = 0;

        // For each character, count unique middle characters
        for (int c = 0; c < 26; c++) {
            if (first[c] != -1 && last[c] > first[c]) {
                unordered_set<char> st;
                for (int i = first[c] + 1; i < last[c]; i++) {
                    st.insert(s[i]);
                }
                ans += st.size();
            }
        }
        return ans;
    }
};

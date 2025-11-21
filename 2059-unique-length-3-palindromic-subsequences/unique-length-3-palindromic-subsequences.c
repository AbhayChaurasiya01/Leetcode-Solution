int countPalindromicSubsequence(char * s) {
    int result = 0;
    for (char c = 'a'; c <= 'z'; c++) {
        int left = -1, right = -1;
        for (int i = 0; s[i]; i++) {
            if (s[i] == c) {
                if (left == -1) left = i;
                right = i;
            }
        }
        if (left != -1 && left < right) {
            int seen[26] = {0};
            for (int i = left + 1; i < right; i++) {
                seen[s[i] - 'a'] = 1;
            }
            for (int i = 0; i < 26; i++) {
                result += seen[i];
            }
        }
    }
    return result;
}
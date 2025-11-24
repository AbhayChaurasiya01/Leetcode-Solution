class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> ans;
        int curr = 0;  // will store prefix value modulo 5
        
        for (int bit : nums) {
            curr = (curr * 2 + bit) % 5;
            ans.push_back(curr == 0);
        }
        
        return ans;
    }
};

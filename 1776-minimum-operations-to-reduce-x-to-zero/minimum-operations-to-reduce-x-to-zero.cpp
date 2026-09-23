class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int total =0;
        for (int n : nums) total += n;
        int target = total - x;

        if (target < 0) return -1;
        int n = nums.size();
        int maxLen = -1;
        int left = 0, sum =0;
        for (int right = 0; right < n; right++){
            sum += nums[right];
            while (sum>target){
                sum-=nums[left];
                left++;
            }
            if (sum==target){
                maxLen = max(maxLen, right - left + 1);
            }
        }
        return maxLen == -1 ? -1 : n - maxLen;
    }
};

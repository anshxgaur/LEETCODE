class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int maxLeft = nums[0];
        int currentMax = nums[0];
        int partitionIdx = 0;

        for (int i = 1; i < nums.size(); ++i) {
            currentMax = max(currentMax, nums[i]);
            if (nums[i] < maxLeft) {
                maxLeft = currentMax;
                partitionIdx = i;
            }
        }

        return partitionIdx + 1;
    }
};

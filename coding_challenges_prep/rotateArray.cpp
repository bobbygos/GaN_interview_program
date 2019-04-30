//Problem found at https://leetcode.com/problems/rotate-array/

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if(k<=0)
            return;
        int rotate = k % nums.size();
        vector<int> temp (nums.size());
        for(int i=0; i<nums.size();i++)
        {
            if(i+rotate>=nums.size())
                temp[i+rotate-nums.size()]=nums[i];
            else
                temp[i+rotate]=nums[i];
        }
        nums.swap(temp);
    }
};
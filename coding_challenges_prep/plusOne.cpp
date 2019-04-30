//Problem found at https://leetcode.com/problems/plus-one/

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> plusUno;
        bool ninePlusOne = false;
        int lcd = digits.size()-1;
        digits[lcd] = ++digits.back();
        for(int i = lcd; i>=1; i--)
        {
            if(digits[i]==10)
            {
                digits[i] = 0;
                ninePlusOne = true;
            }
            if(ninePlusOne)
            {
                digits[i-1] = digits[i-1]+1;
                ninePlusOne = false;
            }
        }
        if(digits[0] == 10)
        {
            plusUno.resize(digits.size()+1);
            plusUno[0] = 1;
            digits[0] = 0;
            for(int i = 1; i <plusUno.size(); i++)
            {
                plusUno[i]=digits[i-1];
            }
            return plusUno;
        }
            
        return digits;
    }
};
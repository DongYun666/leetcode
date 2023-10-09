#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        int lower = *min_element(nums.begin(), nums.end());
        int upper = *max_element(nums.begin(), nums.end());
        while(lower < upper) {
            int mid = lower + (upper - lower) / 2;
            int count = 0;
            bool visted = false;
            for(int num:nums){
                if(num <= mid && !visted){
                    count++;
                    visted = true;
                }else{
                    visted = false;
                }
            }
            if (count >= k) {
                upper = mid;
            } else {
                lower = mid + 1;
            }
        }
        return lower;
    }
};

int main(){
    Solution s;
    vector<int> nums = {2,7,9,3,1};
    int k = 2;
    int res = s.minCapability(nums,k);
    cout<< res <<endl;
    return 0;
}
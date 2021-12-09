class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int , int> mp;
        vector<int> v;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]]=i;
        }

        for(int i=0;i<nums.size();i++){
            if(mp[(target)-nums[i]]&&mp[(target)-nums[i]]!=i){
                v.push_back(i);
                v.push_back(mp[target-nums[i]]);
                break;
            }
        }

        return v;
    }
};
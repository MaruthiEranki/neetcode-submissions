class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // var existingNumbers = new Map();
        let existingNumbers = new Object();
        for (let i =0; i < nums.length; i++) {
            let eachNum = nums[i];
            console.log(existingNumbers[eachNum]);
            if (existingNumbers[eachNum]) {
                return true;
            } else {
                existingNumbers[eachNum] = true;
                console.log(existingNumbers)
            }
        };
        return false;
    }
}

// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let count = {}
    let freq = Array.from({length : nums.length + 1}, () => []);

    for(const n of nums){
        count[n] = (count[n] || 0) + 1;
    }
    for(const n in count){
        freq[count[n]].push(parseInt(n));
    }

    let res = []
    for(let i = freq.length -1; i > 0; i--){
        for(const n of freq[i]){
            res.push(n) 
            if(res.length === k){
                return res; 
            }
        }
    }
};


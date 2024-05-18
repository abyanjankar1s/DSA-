// Given an array of integers nums and an integer target, return indices 
// of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    for(let index=0; index<nums.length; index++){
        const num = nums[index];
        const complement = target - num; 
        const sumIndex = map.get(complement);

        const isEqual = map.has(complement);
        if(isEqual) return [index, sumIndex];

        map.set(num, index); 
    }
}

/**
 * first we create a hashmap where key=num[i] and value= [i]. 
 * with loop we go through the array and add them in the map. 
 * but before adding we make sure to check if we have a complement inside the map already. 
 * if we do have a complement inside the map we return the index of array and the value of 
 * that has the complement. 
 * if not we keep adding the num inside the map until we get the answer. 
 */

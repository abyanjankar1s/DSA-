

// Given an integer array nums, return true if any value appears at least 
// twice in the array, and return false if every element is distinct.

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const newNums = new Set(nums)
    const isEqual = nums.length === newNums.size

    return !isEqual; 
}

/**
 * here we use set to determine if the array contains duplicate.
 * first, we create a new hashset called newNums and move the elements of nums array into the set.
 * since, set's cannot contain duplicates it will only copy elements that are different.
 * so, if the array nums does contain duplicate it length will be longer than that of the set newNums.
 * hence, !isEqual will negate the isEqual value and return the answer to us.  
 */
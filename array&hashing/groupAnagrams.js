// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]



/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    if(!strs.length) return []; 

    const map = new Map(); 

    groupWords(strs, map);
    return [...map.values()]; 
};

const groupWords = (strs, map) => {
    for(const original of strs){
        const hash = gethash(original);
        const values = map.get(hash) || []

        values.push(original);
        map.set(hash, values)
    }
}

const gethash = (word) => {
    const frequency = new Array(26).fill(0); 
    for(const char of word){
        const charCode = getCode(char);

        frequency[charCode]++
    }
    return buildHash(frequency);
}

const getCode = (char) => char.charCodeAt(0) - 'a'.charCodeAt(0); 
const buildHash = (frequency) => frequency.toString(); 

/**
 * used hashmap to solve this problem. 
 * first with groupWords function we map key and values of the map. 
 * for key we get fill an empty array with number of times the char shows up in the words,
 * and return a string value of the array.
 * for value in the map, we check if it matches with the hash we add it to it other we 
 * create a newhash and add the values to it. 
 */


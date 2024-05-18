

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different 
// word or phrase, typically using all the original letters exactly once.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true

// Example 2:
// Input: s = "rat", t = "car"
// Output: false

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const isEqual = s.length === t.length;
    if(!isEqual) return false;

    addFrequency(s, map);
    subFrequency(t, map);
    return checkFrequency(map);
}
const addFrequency = (str, map) => {
    for(const char of str){
        const count = 1 + (map.get(char) || 0)
        map.set(char, count)
    }
}
const subFrequency = (str, map) => {
    for(const char of str){
        if(!map.has(char)) continue;
        const count = map.get(char) - 1 
        map.set(char, count)
    }
}
const checkFrequency = (map) => {
    for(const [char, count] of map){
        const isEqual = count === 0 
        if(!isEqual) return false; 
    }
    return true;
}

/**
 * first we make sure the lenght of s and t are equal because 
 * if the lenght dont match it cannot be a valid anagram.
 * then we create function addFrequency,sub and check. 
 * for addF we add the values of s into a map and set map[char, count], 
 * where count will add num of times a char shows up in the string str. 
 * Similary for subF we sub the count for num of times the char showup in the string.
 * And for chechF, we make sure the map[char,count], count/value is empty. 
 * Because inorder for s and t to be a anagram the char in s has to cancel out the char
 * in t in the map and hence return count value as 0. 
 */
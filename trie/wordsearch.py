# Design Word Search Data Structure
# Design a data structure that supports adding new words and searching for existing words.

# Implement the WordDictionary class:

# void addWord(word) Adds word to the data structure.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# Example 1:

# Input:
# ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

# Output:
# [null, null, null, null, false, true, true, true]

# Explanation:
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("day");
# wordDictionary.addWord("bay");
# wordDictionary.addWord("may");
# wordDictionary.search("say"); // return false
# wordDictionary.search("day"); // return true
# wordDictionary.search(".ay"); // return true
# wordDictionary.search("b.."); // return true 

class TrieNode:
    def __init__(self):
        self.children = {} 
        self.end = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        curr = self.root 
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() 
            curr = curr.children[c] 
        curr.end = True 

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root 

            for i in range(j, len(word)):
                c = word[i] 
                if c == ".":
                    for child in self.children:
                        dfs(j+1, child)  
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c] 
            return curr.end 
        
        return dfs(0, self.root)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(word, cur):
            if not word:
                return cur.endOfWord
            
            if word[0] == ".":
                toCheck = []
                for c in cur.children:
                    newCur = cur.children[c]
                    toCheck.append(dfs(word[1:], newCur))
                return any(toCheck)
            
            elif word[0] not in cur.children:          
                return False

            else:
                cur = cur.children[word[0]]
                return dfs(word[1:], cur)
            
        return dfs(word, self.root)
        
        


        
            

        
        

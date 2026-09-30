class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        # initialize a root TrieNode        
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i) -> bool:
            if i==len(word):
                return node.is_end
            elif word[i]==".":
                return any([dfs(node, i+1) for node in node.children.values()])
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i+1)
        return dfs(self.root, 0)


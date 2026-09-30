class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            curr = curr.setdefault(ch, {})
        curr["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node:dict, i:int) -> bool:
            if i == len(word):
                return "#" in node
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i+1) for k, child in node.items() if k != "#")
            if ch not in node:
                return False
            return dfs(node[ch], i+1)
        
        return dfs(self.root, 0)

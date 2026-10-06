class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # from comparing curr with next, we can get a list of a < b
        adj = {char: set() for word in words for char in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(char: str) -> bool:
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
            
            visited[char] = False
            res.append(char)
            return False
        
        for char in adj:
            if dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie using words
        # for each (r,c) in board:
        #   results.extends(match(r,c))
        root = {}
        for w in words:
            curr = root
            for ch in w:
                curr = curr.setdefault(ch, {})
            curr["$"] = w
        
        rows, cols = len(board), len(board[0])
        res = []
        def dfs(r:int, c:int, parent:dict):
            ch = board[r][c]
            curr = parent[ch]

            if "$" in curr:
                res.append(curr.pop("$"))
            
            board[r][c] = "#"

            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] in curr:
                    dfs(nr, nc, curr)
            
            board[r][c] = ch
            if not curr:
                del parent[ch]
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
                    
        return res
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        
        queue = deque([(beginWord, 1)])
        words.discard(beginWord)

        letters = "abcdefghijklmnopqrstuvwxyz"
        word_len = len(beginWord)

        while queue:
            word, length = queue.popleft()
            for i in range(word_len):
                prefix = word[:i]
                suffix = word[i+1:]

                for ch in letters:
                    if ch == word[i]:
                        continue

                    next_word = prefix + ch + suffix
                    if next_word == endWord:
                        return length + 1
                    
                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, length+1))
        return 0
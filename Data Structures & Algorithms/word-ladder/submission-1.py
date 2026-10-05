class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
 
        beginSet = {beginWord}
        endSet = {endWord}
        words.discard(beginWord)
        words.discard(endWord)

        letters = "abcdefghijklmnopqrstuvwxyz"
        length = 1

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            nextLevel = set()
            for word in beginSet:
                for i in range(len(word)):
                    prefix, suffix = word[:i], word[i+1:]
                    for ch in letters:
                        candidate = prefix+ch+suffix
                        if candidate in endSet:
                            return length + 1
                        if candidate in words:
                            nextLevel.add(candidate)
                            words.remove(candidate)
            beginSet = nextLevel
            length += 1
        return 0
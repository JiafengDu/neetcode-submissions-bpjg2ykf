class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            keyArr = [0]*26
            for c in s:
                keyArr[ord(c)-ord('a')] += 1
            key = tuple(keyArr)
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        return list(groups.values())
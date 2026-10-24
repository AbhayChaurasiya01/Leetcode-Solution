class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        total = len(words[0]) * len(words)
        res = []

        for i in range(len(s) - total + 1):
            sub = []
            ele = s[i:i + total]

            for j in range(0, len(ele), len(words[0])):
                sub.append(ele[j:j + len(words[0])])

            if sorted(sub) == sorted(words):
                res.append(i)

        return res
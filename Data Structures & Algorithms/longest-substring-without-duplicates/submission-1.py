class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #charSet = set()
        mp = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

        #while s[r] in charSet:
        #        charSet.remove(s[l])
        #        l += 1
        #    charSet.add(s[r])
        #    res = max(res, r - l + 1)
        #return res
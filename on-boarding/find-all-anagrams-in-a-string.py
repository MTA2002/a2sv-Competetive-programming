class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = Counter(p)
        s_dict = Counter()
        ans = []
        k = len(p)
        for i in range(len(s)):
            s_dict[s[i]] += 1
            if i + 1 >= k:
                if  s_dict == p_dict:
                    ans.append(i - (k-1))
                s_dict[s[i-(k-1)]] -= 1
                
        return ans

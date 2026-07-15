class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])
            # Add s[right] to the window
            while (right - left + 1) - max_freq > k:
        # Remove s[left] from the window
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            
        return longest
                

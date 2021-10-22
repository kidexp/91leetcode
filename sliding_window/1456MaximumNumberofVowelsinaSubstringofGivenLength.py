

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_set = {"a", "e", "i", "o", "u"}
        start = 0
        vowel_count = max_vowel_count = 0
        for i in range(len(s)):
            if s[i] in vowels_set:
                vowel_count += 1
            while i - start == k:
                if s[start] in vowels_set:
                    vowel_count -= 1
                start += 1
            max_vowel_count = max(max_vowel_count, vowel_count)
        return max_vowel_count


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels(s="abciiidef", k=3))
    print(solution.maxVowels(s="aeiou", k=2))
    print(solution.maxVowels(s="leetcode", k=3))
    print(solution.maxVowels(s="rhythms", k=4))
    print(solution.maxVowels(s="tryhard", k=4))

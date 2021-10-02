from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        brute force
        """
        word_count_dict = Counter(words)
        word_length = len(words[0])
        word_num = len(words)
        result = []
        for i in range(0, len(s) - word_length * word_num + 1):
            actual_word_count = defaultdict(int)
            end = i
            find_word_num = 0
            while end < len(s):
                word = s[end : end + word_length]
                if (
                    word in word_count_dict
                    and actual_word_count[word] < word_count_dict[word]
                    and find_word_num < word_num
                ):
                    actual_word_count[word] += 1
                    find_word_num += 1
                else:
                    break
                end += word_length
            if find_word_num == word_num:
                result.append(i)
        return result

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        two pointers
        """
        word_count_dict = Counter(words)
        word_length = len(words[0])
        word_num = len(words)
        result = []
        for i in range(word_length):
            start, end = i, i
            actual_word_count = defaultdict(int)
            while end < len(s):
                word = s[end : end + word_length]
                while (
                    word in word_count_dict
                    and word_count_dict[word] <= actual_word_count[word]
                ):
                    actual_word_count[s[start : start + word_length]] -= 1
                    start += word_length
                if (
                    word in word_count_dict
                    and actual_word_count[word] < word_count_dict[word]
                ):
                    actual_word_count[word] += 1
                elif word not in word_count_dict:
                    start = end + word_length
                    actual_word_count = defaultdict(int)
                end += word_length
                if end - start == word_num * word_length:
                    result.append(start)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
    print(
        solution.findSubstring(
            s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]
        )
    )
    print(
        solution.findSubstring(
            s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]
        )
    )
    print(
        solution.findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
        )
    )

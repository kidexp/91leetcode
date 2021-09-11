from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        chars_row_list = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        char_row_dict = {}
        for i in range(3):
            for char in chars_row_list[i]:
                char_row_dict[char] = i
        return [
            word
            for word in words
            if len(word) == 1
            or all(
                (
                    char_row_dict[word[i].lower()] == char_row_dict[word[0].lower()]
                    for i in range(1, len(word))
                )
            )
        ]


if __name__ == "__main__":
    solution = Solution()
    print(solution.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
    print(solution.findWords(words=["omk"]))
    print(solution.findWords(words=["adsdf", "sfd"]))

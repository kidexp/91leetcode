from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour_bit_list = [1, 2, 4, 8]
        minute_bit_list = [1, 2, 4, 8, 16, 32]
        result = []

        def dfs(
            iterate_list,
            iterate_index,
            value,
            max_value,
            remaining_count,
            need_down_to_zero,
            result_list,
        ):
            if need_down_to_zero:
                if remaining_count == 0:
                    result_list.append((value, remaining_count))
            else:
                result_list.append((value, remaining_count))
            if remaining_count > 0:
                for i in range(iterate_index, len(iterate_list)):
                    new_value = value + iterate_list[i]
                    if new_value < max_value:
                        dfs(
                            iterate_list,
                            i + 1,
                            new_value,
                            max_value,
                            remaining_count - 1,
                            need_down_to_zero,
                            result_list,
                        )

        hour_list = []
        dfs(hour_bit_list, 0, 0, 12, turnedOn, False, hour_list)
        for hour, remaining_count in hour_list:
            minute_list = []
            dfs(minute_bit_list, 0, 0, 60, remaining_count, True, minute_list)
            for minute, _ in minute_list:
                result.append(
                    str(hour)
                    + ":"
                    + (str(minute) if minute > 9 else ("0" + str(minute)))
                )
        return result

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        """
        bit manipulation
        """
        result = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    result.append(
                        str(hour)
                        + ":"
                        + (str(minute) if minute > 9 else ("0" + str(minute)))
                    )
        return result


if __name__ == "__main__":
    solution = Solution()
    # for i in range(5):
    #     print(i, solution.readBinaryWatch(i))
    # print(9, solution.readBinaryWatch(9))
    print(1, solution.readBinaryWatch(1))
    print(2, solution.readBinaryWatch(2))
    print(3, solution.readBinaryWatch(3))
    print(len(solution.readBinaryWatch(3)), len(set(solution.readBinaryWatch(3))))
    print(len(solution.readBinaryWatch(4)), len(set(solution.readBinaryWatch(4))))
    print(9, solution.readBinaryWatch(9))

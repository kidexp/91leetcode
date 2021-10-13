def normalize(start_time, end_time):
    end_hour, end_minutes = int(end_time[0:2]), int(end_time[3:])
    start_hour, start_minuts = int(start_time[0:2]), int(start_time[3:])
    if end_hour < start_hour:
        end_hour += 24
    elif end_hour == start_hour and end_minutes < start_minuts:
        end_hour += 24
    return start_hour, start_minuts, end_hour, end_minutes


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        start_hour, start_minutes, end_hour, end_minutes = normalize(
            startTime, finishTime
        )
        total_game = (
            (end_hour - start_hour) * 4
            - start_minutes // 15
            - (1 if start_minutes % 15 > 0 else 0)
            + end_minutes // 15
        )
        return max(total_game, 0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfRounds(startTime="12:01", finishTime="12:44"))
    print(solution.numberOfRounds(startTime="20:00", finishTime="06:00"))
    print(solution.numberOfRounds(startTime="00:00", finishTime="23:59"))
    print(solution.numberOfRounds(startTime="20:00", finishTime="06:01"))
    print(solution.numberOfRounds(startTime="20:01", finishTime="06:01"))
    print(solution.numberOfRounds(startTime="00:01", finishTime="00:02"))

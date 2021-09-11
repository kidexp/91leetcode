from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = defaultdict(int)
        for domain_count_tuple in cpdomains:
            count, domain = domain_count_tuple.split()
            count = int(count)
            domain_name_list = domain.split(".")
            for i in range(len(domain_name_list)):
                result[".".join(domain_name_list[i:])] += count
        return [f"{count} {domain}" for domain, count in result.items()]


if __name__ == "__main__":
    solution = Solution()
    print(solution.subdomainVisits(cpdomains=["9001 discuss.leetcode.com"]))
    print(
        solution.subdomainVisits(
            cpdomains=[
                "900 google.mail.com",
                "50 yahoo.com",
                "1 intel.mail.com",
                "5 wiki.org",
            ]
        )
    )

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        avg = sum(salary[1:-1]) / (len(salary)-2)
        return avg

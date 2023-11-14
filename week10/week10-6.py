class Solution:
    def average(self, salary: List[int]) -> float:
        total=sum(salary)-max(salary)-min(salary)
        n=len(salary)-2
        return total / n
        #return ()sum(salarry)-max(salary)-min(salary))/()len(salary)-2)
# Problem: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Note: 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        days = len(temperatures)
        res = [0] * days

        for i in range(days-1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            
            res[i] = st[-1] - i if st else 0
            st.append(i)
            
        return res

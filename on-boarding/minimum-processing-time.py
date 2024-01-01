class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        count = 0
        idx = 0

        for i in range(len(tasks)-1,-1,-1):
            tasks[i] += processorTime[idx]
            count += 1

            if count == 4:
                count = 0
                idx += 1

        return max(tasks)
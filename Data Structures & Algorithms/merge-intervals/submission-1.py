class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        intervals.sort()

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
                continue

            merge.append([start1, end1])
            start1 = start2
            end1 = end2

        merge.append([start1, end1])
        return merge


        
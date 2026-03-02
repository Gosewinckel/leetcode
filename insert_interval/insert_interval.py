class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flat = []
        for i in intervals:
            flat.append(i[0])
            flat.append(i[1])
        mid = 1 + (len(intervals)//2)
        idx = [mid, mid]
        for i in range(len(idx)):
            left = 0
            right = len(flat) - 1
            mid = idx[i]
            while left <= right:
                if newInterval[i] < flat[mid]:
                    if mid - 1 >= 0 and newInterval[i] > flat[mid - 1]:
                        idx[i] = mid
                        break
                    right = mid - 1
                    mid = ((right - left)//2) + left
                else:
                    if mid + 1 < len(flat) and newInterval[i] < flat[mid + 1]:
                        idx[i] = mid + 1
                        break
                    left = mid + 1
                    mid = ((right - left)//2) + left
        
        # account for idx 2 being pushed 1 over by idx1
        idx[1] += 1

        # fill new array with intervals
        result = []
        interval = []
        pos = 0
        while pos < len(flat):
            #once first position is reached
            if pos == idx[0]:
                # case where pos1 sits between interval
                if pos % 2 != 0:
                    pos = idx[1] - 1
                    # pos2 sits between interval
                    if pos % 2 != 0:
                        interval.append(flat[pos])
                    # pos2 does not sit between interval
                    else:
                        pos -= 1
                        interval.append(newInterval[1])
                # case where pos1 starts new interval
                else:
                    # add pos1 value
                    interval.append(newInterval[0])
                    pos = idx[1] - 1
                    # pos2 sits between interval
                    if pos % 2 != 0:
                        interval.append(flat[pos])
                    else:
                        pos -= 1
                        interval.append(newInterval[1])
            else:
                interval.append(flat[pos])
            if len(interval) == 2:
                result.append(interval)
                interval = []
            pos += 1

        return result


if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4, 8]
    sol = Solution()
    res = sol.insert(intervals, newInterval)
    print(res)

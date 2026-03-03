class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        idx = start
        tank = 0
        found = False
        while not found:
            tank += gas[idx] - cost[idx]
            idx += 1
            if idx == len(gas):
                idx = 0
            if tank < 0:
                # no path found
                if idx <= start:
                    return -1
                tank = 0
                start = idx
                continue
            if idx == start:
                found = True
        return idx


if __name__ == "__main__":
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    sol = Solution()
    res = sol.canCompleteCircuit(gas, cost)
    print(res)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        visited = set()

        for i, last_temp in enumerate(reversed(temperatures)):
            print('comparing {} to {}'.format(last_temp, visited))
            if any (x > last_temp for x in visited):
                for j, e in enumerate(temperatures[len(temperatures)-i:]):
                    print('checking {} for a higher temp'.format(temperatures[len(temperatures)-i:]))
                    if e > last_temp:
                        result[len(temperatures)-i-1] = j + 1
                        break
            visited.add(last_temp)
        return result

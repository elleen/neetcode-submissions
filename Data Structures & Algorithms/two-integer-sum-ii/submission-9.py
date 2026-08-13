class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        no_match = set()

        i1, i2 = 0, 1
        while i1 < len(numbers)-1:
            n1 = numbers[i1]
            if n1 not in no_match:

                rest = set(numbers[i1+1:])
                if target-n1 in rest:
                    print("{} is in rest".format(target-n1))
                    while i2 < len(numbers):
                        n2 = numbers[i2]
                        # print('n1, n2 = {}, {}'.format(n1, n2))
                        if n1+n2 == target:
                            # print('target found at i1={}, i2={}'.format(i1,i2))
                            return list([i1+1, i2+1])
                        i2 += 1
                else:
                    no_match.add(n1)
            i1 += 1
            i2 = i1+1
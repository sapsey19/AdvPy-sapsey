import sys
from sys import stdin
def answer(nums):
    del nums[0]
    nums.sort()
    ans = []
    ans.append(str(nums[0]))
    ans.append(str(nums[-1]))
    ans.append(str(nums[-1] - nums[0]))
    return ans
    
def solve():
    i = 1
    x = 0
    for line in stdin:
        nums = line.strip('\n').split(' ')  
        while x < len(nums):       
            nums[x] = int(nums[x])
            x += 1         
        print('Case {}:'.format(i), ' '.join(answer(nums)))
        i += 1
        x = 0
def test():
    assert(answer([3, 20, 20, 20]) == ['20', '20', '0'])
    assert(answer([1, 0]) == ['0', '0', '0'])  
    assert(answer([3, -1000000, 1000000, 35]) == ['-1000000', '1000000', '2000000'])    
    assert(answer([11, 33, 28, 532, 10, -1023, -10, 403, 20, 55, 412, -9]) == ['-1023', '532', '1555'])
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
import sys
import math

def answer(n, k):
    if math.log2(n) <= k:
        return 'Your wish is granted!'
    else:
        return 'You will become a flying monkey!'

def solve():
    temp = input().split(' ')
    n = int(temp[0])
    k = int(temp[1])
    print(answer(n, k))

def test():
    assert(answer(1000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000)
     == 'Your wish is granted!')
    assert(answer(4, 1) == 'You will become a flying monkey!')
    assert(answer(9999999999999, 42) == 'You will become a flying monkey!')
    assert(answer(123456789, 27) == 'Your wish is granted!')
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
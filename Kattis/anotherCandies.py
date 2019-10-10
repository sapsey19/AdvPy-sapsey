import sys

def answer(candies):
    n = len(candies)
    numCandies = 0
    for i in range(0, len(candies)):
        numCandies += candies[i]
        if numCandies > n:
            numCandies = numCandies % n
    if numCandies == 0 or numCandies == n:
        return 'YES'
    else:
        return 'NO'

def solve():
    t = int(input())
    candies = []
    for i in range(0, t):
        temp = input()
        n = int(input())       
        for j in range(0, n):
            temp = int(input())
            candies.append(temp)
        print(answer(candies))
        candies.clear()        

def test():
    assert(answer([1, 2, 3]) == 'YES')
    assert(answer([1, 2, 3, 4]) == 'NO')
    assert(answer([350266329, 404652733, 83317342, 648326556, 667178683, 
    630563849, 667816293, 189838785, 714805318, 133289603, 151020189, 971511141,
    887355247, 498802924, 812189941, 414983667, 401196951, 971177252, 119769112, 722967398]) == 'NO')
    assert(answer([100000000000000000000, 10000000000000000000000000000]) == 'YES')
    print('All test cases passed!')  

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
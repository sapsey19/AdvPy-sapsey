import sys

def answer(n, a, ships):
    ships.sort()
    counter = 0 
    # for i in range (0, n):
    #     if ships[i] < a:
    #         counter += 1
    #         a -= ships[i] + 1
    # while i < n:
    #     if ships[i] < a:
    #         counter += 1
    #         a -= ships[i] + 1
    #     i += 1
    for x in ships:
        if x < a:
            counter += 1
            a = a - (x + 1)
    return counter

def solve():
    ships = list()
    temp = input().split(' ')
    n = int(temp[0])
    a = int(temp[1])
    ships = input().split(' ')
    ships = [int(i) for i in ships]
    print(answer(n, a, ships))

def test():
    x = 1
    for i in range(0, 10000000):
        x += 1
    print(x)
    assert(answer(1, 0, [10000000000]) == 0)
    assert(answer(3, 6, [1, 2, 3]) == 2)
    #assert(answer(1000000))
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
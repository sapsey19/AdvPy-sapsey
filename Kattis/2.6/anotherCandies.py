import sys


def solve():
    t = int(input())
    temp = input()
    candies = []
    total = 0
    answers = []
    for i in range(0, t):
        if i == 0:
            n = int(input())
        else:
            temp = input()
            n = int(input())       
        for j in range(0, n):
            temp = int(input())
            candies.append(temp)
        for c in candies:
            total += c
        if total % n == 0:
            answers.append('YES')
        else:
            answers.append('NO')     
        candies.clear()

    for a in answers:
        print(a)

def test():
    assert(1 == 1)       


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
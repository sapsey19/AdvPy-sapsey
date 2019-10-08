import sys

def answer(n, m, taskLengths, quietLengths):
    taskLengths.sort()
    quietLengths.sort()
    print(taskLengths)
    print(quietLengths)
    count = 0
    i = 0
    while i < m:
        if(taskLengths[i] <= quietLengths[i]):
            count += 1
        i += 1
    return count
def solve():
    temp = input().split(' ') #ignore
    n = int(temp[0])
    m  = int(temp[1])
    temp = input()
    taskLengths = [int(i) for i in temp.split(' ')]
    temp = input()
    quietLengths = [int(i) for i in temp.split(' ')]
    
    
    print(answer(n, m, taskLengths, quietLengths))
    

def test():
    assert(answer() == '' )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
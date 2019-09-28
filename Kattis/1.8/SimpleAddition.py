import sys

def answer(arr):    
    sum = 0   
    for n in arr:
        sum += int(n)
    return sum
    
def solve():
    arr = []
    temp = input()
    arr.append(temp) 
    temp = input()    
    arr.append(temp)  
    print(answer(arr))

def test():
    assert(answer([0, 0]) == 0)
    assert(answer([9999999999999, 9999999999999]) == 19999999999998)
    assert(answer([19999999999998, 19999999999998]) == 39999999999996)
    assert(answer([1, 1000000000000000000000000000000000000000000000000000000000000000000000000]) == 1000000000000000000000000000000000000000000000000000000000000000000000001)
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
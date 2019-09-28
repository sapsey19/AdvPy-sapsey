import sys
from collections import Counter

def answer(arr):
    occurences = Counter(arr)
    if(occurences.most_common(2)[0][1] == occurences.most_common(2)[1][1]):        
        return 'Runoff!'
    else:
        return occurences.most_common(1)[0][0]
def solve():
    line = ''
    arr = []
    while line != '***':
        line = input()
        arr.append(line)
    print(answer(arr))

def test():
    assert(answer(['Will Smith', 'Harrison Ford', 'Angelina Jolie', 'Morgan Freeman', 'Harrison Ford']) == 'Harrison Ford')
    assert(answer(['Tom Hanks', 'Tom Cruise']) == 'Runoff!')
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
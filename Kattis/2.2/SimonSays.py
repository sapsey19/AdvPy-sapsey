import sys
def answer(line):   
    if 'simon says' in line:
        phrase = line[11:]       
        return phrase
    else:
        return ''
def solve():
    n = int(input())
    for i in range(0, n):
        line = input()
        print(answer(line))

def test():
    assert(answer('simon says do a backflip') == 'do a backflip')
    assert(answer('simon shouts do your homework') == '')
    print('All test cases passed!')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
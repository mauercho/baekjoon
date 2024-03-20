import sys

input = sys.stdin.readline

M = int(input())
s = set()
lst = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
for _ in range(M):
    string = input().rstrip().split()
    if string[0] == 'add':
        s.add(string[1])
    elif string[0] == 'check':
        if string[1] in s:
            print(1)
        else:
            print(0)
    elif string[0] == 'remove':
        if string[1] in s:
            s.remove(string[1])
        else:
            pass
    elif string[0] == 'toggle':
        if string[1] in s:
            s.remove(string[1])
        else:
            s.add(string[1])
    elif string[0] == 'all':
        s = set(lst)
    else:
        s.clear()


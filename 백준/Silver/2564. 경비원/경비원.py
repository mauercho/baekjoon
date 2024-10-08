def is_opposite(direc1, direc2):
    if direc2 < direc1: # direc1이 더 크면
        pass
    else:
        direc1, direc2 = direc2, direc1
    if direc1 - 1 == direc2 and direc1 != 3:
        return True
    else:
        return False

def same_direc(direc1, direc2):
    if direc1 == direc2:
        return True
    else:
        return False

w, h = map(int,input().split())
N = int(input())
temp_lst = []
for _ in range(N):
    direc, pos = map(int, input().split())
    temp_lst.append((direc, pos))

real_direc, real_pos = map(int, input().split())
sum_val = 0
for mem in temp_lst:
    if same_direc(real_direc, mem[0]):
        temp_sum = abs(real_pos - mem[1])
    else:
        if is_opposite(real_direc, mem[0]):
            if real_direc == 3 or real_direc == 4:
                temp_sum = min(real_pos + w + mem[1], w + h - real_pos + h - mem[1])
            else:
                temp_sum = min(real_pos + mem[1] + h, h + w -real_pos + w - mem[1])
        else:
            if real_direc == 1 and mem[0] == 3:
                temp_sum = mem[1] + real_pos
            elif real_direc == 1 and mem[0] == 4:
                temp_sum = w - real_pos + mem[1]
            elif real_direc == 2 and mem[0] == 3:
                temp_sum = h - mem[1] + real_pos
            elif real_direc == 2 and mem[0] == 4:
                temp_sum = w - real_pos + h - mem[1]
            elif real_direc == 3 and mem[0] == 1:
                temp_sum = mem[1] + real_pos
            elif real_direc == 3 and mem[0] == 2:
                temp_sum = h - real_pos + mem[1]
            elif real_direc == 4 and mem[0] == 1:
                temp_sum = w - mem[1] + real_pos
            elif real_direc == 4 and mem[0] == 2:
                temp_sum = w - mem[1] + h - real_pos
    sum_val += temp_sum
print(sum_val)

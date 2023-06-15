inlist = input().split(',')

for i in range(len(inlist)):
    inlist[i] = int(inlist[i])

# 要找連續上升k天的區段
days = int(input())
if days < 3:
    days = 3


def mono_inc(inlist, k):
    consecutive_days = 0
    max_days = -1000000000000
    start = 0
    end = 0
    max_days_start = 0
    max_days_end = 0

    for m in range(len(inlist)):
        if m == 0:
            start = 0
        else:
            if inlist[m] > inlist[m-1]:
                consecutive_days += 1
                end = m
                start = m - consecutive_days
                if consecutive_days > max_days:  # 最長的連續增加的天數
                    max_days = consecutive_days
                    max_days_start = start
                    max_days_end = end
                else:
                    continue
            elif inlist[m] <= inlist[m-1]:
                consecutive_days = 0
            else:
                continue

    if max_days >= k:
        answer = str(max_days_start) + "\n" + str(max_days_end)
        return answer
    elif max_days < k:
        return None

print(mono_inc(inlist, k=days))

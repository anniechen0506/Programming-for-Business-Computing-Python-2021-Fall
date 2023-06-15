input_list = input().split(',')

for i in range(len(input_list)):
    input_list[i] = int(input_list[i])

days = int(input())  # 要找連續上升k天的區段
if days < 3:
    days = 3


def mono_inc_plus(input_list, k):
    diff_list = []
    start_end_list = []
    consecutive_days = 0
    consecutive = False

    for m in range(len(input_list)):
        if m == 0:
            start = 0
        else:
            if input_list[m] > input_list[m-1]:
                consecutive_days += 1
                end = m
                # 當連續數字大於等於k，且已經跑到最後一個數字，進入內圈if
                if consecutive_days >= k and m == (len(input_list)-1):
                    consecutive = True
                    # end = m
                    start = m - consecutive_days
                    start_end_list = [start, end]
                    diff_list.append(start_end_list)  # 整串都是正確的
            elif input_list[m] <= input_list[m-1]:  # 如果當中有遇到確診數變少或相等的情況
                if consecutive_days >= k:
                    consecutive = True
                    # end = m-1
                    # start = (m-1) - consecutive_days
                    start_end_list = [start, end]
                    diff_list.append(start_end_list)
                start = m  # 重新將index歸到目前跑到的數
                consecutive_days = 0

    if consecutive is True:
        return diff_list
    elif consecutive is False:
        return "None"

if mono_inc_plus(input_list, days) == "None":
    print("None")
else:
    answer = mono_inc_plus(input_list, days)
    for l in range(len(answer)):
        final_answer = str(answer[l][0]) + " " + str(answer[l][1])
        print(final_answer)

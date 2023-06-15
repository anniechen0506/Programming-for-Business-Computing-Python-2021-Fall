ylist = input().split(',')
for f in range(len(ylist)):
    ylist[f] = float(ylist[f])

htype = input()


def my_hhi(ylist, htype):
    if htype == "Original":
        htype = "Original"
    else:
        htype = "Normalized"

    hhi_original = 0.0
    hhi_normalized = 0.0
    market = 0
    occupation_rate = 0
    occupate_list = []

    if htype == "Original":
        for y in range(len(ylist)):
            market += abs(ylist[y])  # 市場佔有率的分母
        for s in range(len(ylist)):
            occupation_rate = ylist[s] / market  # 市場佔有率
            occupate_list.append(occupation_rate)
            hhi_original += (occupate_list[s] ** 2)
        return hhi_original
    elif htype == "Normalized":
        for y in range(len(ylist)):
            market += abs(ylist[y])  # 市場佔有率的分母
        for s in range(len(ylist)):
            occupation_rate = ylist[s] / market  # 市場佔有率
            occupate_list.append(occupation_rate)
            hhi_original += (occupate_list[s] ** 2)
        hhi_normalized = (hhi_original - 1 / len(ylist)) / (1 - 1 / len(ylist))
        return hhi_normalized

value = my_hhi(ylist, htype)


def printresult(value):
    return(f"{value:.4f}")

print(printresult(value))

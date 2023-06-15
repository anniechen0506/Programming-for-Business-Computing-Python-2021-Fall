input_list = []

for a in range(1000):
    inlist = input()
    if inlist == "RECORDSTOP":
        break

    else:
        inlist = inlist.split("_")
        inlist[1] = float(inlist[1])
        inlist[2] = float(inlist[2])
        input_list.append(inlist)

# input_list.copy()
new_list = []
for i in range(len(input_list)):
    new_list.append([])
    for element in input_list[i]:
        new_list[i].append(element)


def apply_discount(new_list):
    discount_amount = 0.0
    total_amount = 0.0
    after_discount = 0.0
    for i in range(len(new_list)):
        if new_list[i][2] < 0:
            discount_amount += new_list[i][2]
            # new_list[i][2] = "need_remove"
        elif new_list[i][2] >= 0:
            total_amount += new_list[i][2]

    for m in range(len(new_list)):
        if float(new_list[m][2]) >= 0:
            after_discount = new_list[m][2] + \
                           (discount_amount * (new_list[m][2] / total_amount))
            new_list[m][2] = after_discount
        else:
        	new_list[m] = "need_remove"

    new_list = [m for m in new_list if m != "need_remove"]
    return new_list


def printrec(records):
    for arec in records:
        # 避免浮點數誤差
        if abs(arec[2]) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{arec[1]:.2f}_{arec[2]:.2f}")

printrec(apply_discount(new_list))
print("---Original---")
printrec(input_list)

# version 1
# 輸入
number = int(input())
target = input()
customPunctuation = '。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&\'()*+,-./:;<=>?@[\]^_`{¦}~'

# 將字串切割


def ngram(target, number, customPunctuation):
    # 如果 n 小於2回傳題目需求
    if number < 2:
        return ['ILLEGAL_N']
    # 用空白取代標點符號
    for i in target:
        if i in customPunctuation:
            target = target.replace(i, ' ')

    tmp = target.split(' ')
    target = []
    # 丟棄空字串
    for i in tmp:
        if i != '':
            target.append(i)

    answer = []
    # 擷取需要的長度
    for i in target:
        for j in range(len(i)-number+1):
            answer.append(i[j:j+number])

    return answer


answer = ngram(target, number, customPunctuation)

for i in answer:
    print(i)
    
    
# version 2
continue_len = int(input())
sentence = str(input())

punctuation_list = ['。', '，', '、', '；', '：', '「', '」', '『', '』', '（',
                    '）', '─', '？', '！', '─', '…', '﹏', '《', '》', '〈',
                    '〉', '．', '～', '　', '.', ';', "'", '!', '"', '#', '$',
                    '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<',
                    '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '¦', '}',
                    '~', ' ', ",", '']
'''
# 將標點符號轉為ASCII code
# punct_num = 0
# punct_num_list = []

# for i in range(len(punctuation_list)):
    # punct_num = ord(punctuation_list[i])
    # punct_num_list.append(punct_num)

# print(punct_num_list) 測試標點符號陣列是否轉為ASCII code

# if continue_len < 2:
    # print("ILLEGAL_N")

# 將輸入的字串轉為ASCII code
# sentence_num = 0
# sentence_num_list = []

# for s in range(len(sentence)):
    # sentence_num = ord(sentence[s])
    # sentence_num_list.append(sentence_num)'''

# 比對字串與標點符號的list
'''for i in range(len(sentence)):
    for k in range(len(punct_num_list)):
        if sentence[i] == punct_num_list[k]:
            have_punct = True
    # print(sentence[i : (i + continue_len)])

for i in range(len(sentence)):
    if continue_len <= len(sentence):
        if i <= (len(sentence) - continue_len):
            for j in sentence[i: (i + continue_len)]:
                punct = False
                if j in punctuation_list:
                    punct = True
                    break
            if punct == False:
                print(sentence[i: (i + continue_len)])

if continue_len > len(sentence):
    print(sentence)'''

if continue_len <= len(sentence):
    if continue_len < 2:
        print("ILLEGAL_N")
    else:
        for i in range(len(sentence)):
            if i <= (len(sentence) - continue_len):
                for j in sentence[i: (i + continue_len)]:
                    punct = False
                    if j in punctuation_list:
                        punct = True
                        break
                if punct is False:
                	print(sentence[i: (i + continue_len)])
elif continue_len > len(sentence):
    if continue_len < 2:
        print("ILLEGAL_N")
    else:
        print(sentence)

# /Users/anniechen/Desktop

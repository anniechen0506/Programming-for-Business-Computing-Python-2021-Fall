# version 1

# 將字串切割
def ngram(target, number, customPunctuation):
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


# 輸入
number = int(input())
target = input()
source = input()
customPunctuation = '。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&\'()*+,-./:;<=>?@[\]^_`{¦}~'

# target 的結果
targetResult = ngram(target, number, customPunctuation)
# source 的結果
sourceResult = ngram(source, number, customPunctuation)
sameResult = []

# 蒐集一樣的部分
for i in targetResult:
    for j in sourceResult:
        if i == j:
            sameResult.append(i)


print("LEN=" + str(len(targetResult)))
print("MATCH_COUNT="+str(len(sameResult)))
print("SIMILARITY=%.4f" % (round(len(sameResult)/len(targetResult), 4)))
print("MATCHED SEGMENTS:")
for i in sameResult:
    print(i)
    
    
# version 2
n = int(input())  # 要檢查的連續詞長度
target = str(input())
source = str(input())

punctuation_list = ['。', '，', '、', '；', '：', '「', '」', '『', '』', '（',
                    '）', '─', '？', '！', '─', '…', '﹏', '《', '》', '〈',
                    '〉', '．', '～', '　', '.', ';', "'", '!', '"', '#', '$',
                    '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<',
                    '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '¦', '}',
                    '~', ' ', ",", '']

# 計算target的連續詞數量
target_cont_list = []
target_cont_num = 0  # target的連續詞數量

if n <= len(target):
    for i in range(len(target)):
        if i <= (len(target) - n):
            for j in target[i: (i + n)]:
                punct = False
                if j in punctuation_list:
                    punct = True
                    break
            if punct is False:
                target_cont = target[i: (i + n)]
                target_cont_list.append(target_cont)
                target_cont_num = len(target_cont_list)
elif n > len(target):
    target_cont = target
    target_cont_list.append(target_cont)
    target_cont_num = len(target_cont_list)

# print(target_cont_list)
# print(target_cont_num)

# 計算source的連續詞數量
source_cont_list = []
source_cont_num = 0  # source的連續詞數量

if n <= len(source):
    for x in range(len(source)):
        if x <= (len(source) - n):
            for y in source[x: (x + n)]:
                punct = False
                if y in punctuation_list:
                    punct = True
                    break
            if punct is False:
                source_cont = source[x: (x + n)]
                source_cont_list.append(source_cont)
                source_cont_num = len(source_cont_list)
elif n > len(source):
    source_cont = source
    source_cont_list.append(source_cont)
    source_cont_num = len(source_cont_list)

# 比對target跟source的連續詞
same_cont_num = 0
matched_segments_list = []
for t in target_cont_list:
    if t in source_cont_list:
        same_cont_num += source_cont_list.count(t)
        for s in range(1, source_cont_list.count(t) + 1):
            matched_segments_list.append(t)

# 計算相似度
similarity = same_cont_num / target_cont_num

print("LEN=" + str(target_cont_num))
print("MATCH_COUNT=" + str(same_cont_num))
print("SIMILARITY=" + str(f'{similarity:.4f}'))  # 輸出到小數點後四位
print("MATCHED SEGMENTS:")
for m in matched_segments_list:
	print(m)

# /Users/anniechen/Desktop

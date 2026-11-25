# def 函数  (先定义后调用)

# case1:三角形面积
def triangle_area(b,h):
    return b * h / 2

# case2:统计元音字母aeiou
def count_aeiou(s):
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num

# case3:找出传入的数据的最高 最低 平均分
def calc(score):
    max_s = max(score)
    min_s = min(score)
    avg_s = round(sum(score)/len(score),1)
    return max_s,min_s,avg_s

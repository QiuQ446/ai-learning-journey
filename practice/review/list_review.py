# 题目：有一组成绩数据 [85, 92, 78, 95, 88, 72, 90, 83]

# 不用查资料，用Python写代码完成：
# 1. 找出最高分和最低分
# 2. 计算平均分
# 3. 找出及格（≥60）的人数
# 4. 将成绩从高到低排序
# 5. 找出高于平均分的学生成绩
# 6. 给每个成绩评级（≥90优秀、≥80良好、≥70中等、≥60及格、<60不及格），存成字典

scores = [85,92,78,95,88,72,90,83]

1.
maxscore = max(scores)  #最大值

minscore = min(scores)  #最小值

2.
avg = sum(scores) / len(scores) #平均数

3.
count = 0
for i in scores:
    if i >= 60:
        count += 1
print(f"及格人数:{count}")

4.
scores.sort()

5.
for j in scores:
    if j > avg:
        print(j,end=" ")
print()

6.
grades = {}

for score in scores:
    if score >= 90:
        grades[score] = '优秀'
    elif score >= 80:
        grades[score] = '良好'
    elif score >= 70:
        grades[score] = '中等'
    elif score >= 60:
        grades[score] = '及格'
    else:
        grades[score] = '不及格'
print(grades)
    

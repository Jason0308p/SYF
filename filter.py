# 原始数据
raw_data = """
250207210005602690113098927368516475930EX05221085000000000105100000000051
250207210005607473113098927368516821094DE52191652000000000076100000000041
250207210005602777113098927368599141896EV45933822000000000932100000000471
"""

# generator expression

A = [ line.strip() for line in raw_data.strip().split('\n')]
# B = [len(line) for line in A]

# A[] 列表中，直接操作函數
# 以line遍歷
# 值為raw_data.strip().split('\n')
# 即當line 作為 raw_data.strip().split('\n') 遍歷
#  raw_data.strip().split('\n') 原始值先進行 .strip() 去除前後空白  再進行 split("\n")  依指定分隔號分段
#  raw_data.strip().split('\n') 結果為  ["250207210005602690113098927368516475930EX05221085000000000105100000000051",
#  "250207210005607473113098927368516821094DE52191652000000000076100000000041","250207210005602777113098927368599141896EV45933822000000000932100000000471"]

#  再來line開始遍歷 raw_data.strip().split('\n')中的數值，共遍歷3次
#  遍歷3伺候，line的值為 ["250207210005602690113098927368516475930EX05221085000000000105100000000051",
#  "250207210005607473113098927368516821094DE52191652000000000076100000000041","250207210005602777113098927368599141896EV45933822000000000932100000000471"]
#   然後再執行3次 line.strip()，並當作A列表的新元素












#    filter()
#    filter， lambda 是一个用于创建匿名函数的关键字。它允许你定义一个小型的、一次性的函数，而不需要使用 def 关键字来定义一个正式的函数。
#    lambda 会将序列中的每个元素传递给指定的函数，如果函数返回 True，则该元素会被保留；如果返回 False，则该元素会被丢弃。
### 過濾長度不為73的字串符
non_73len = filter(lambda line: len(line) != 73, A )


# any() any函數，檢查可迭代對象中，是否有一元素滿足條件為True，則函數就會返回True

if any(len(line) != 73 for line in A):
    for line in non_73len :
        print(line)
else:
    print("全部字串符合73長度")





#
# # 处理原始数据
# A = [line.strip() for line in raw_data.strip().split('\n')]
#
# # 格式化为带双引号的字符串
# #formatted_str = ',\n'.join(f'"{item}"' for item in A)
#
# # 打印结果
# print(A)
# #print(formatted_str)





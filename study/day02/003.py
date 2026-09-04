# dictionary 键值对
dict = {
    "YYDS": "永远的神",
    "YS": "原神",
    "LOL": "英雄联盟",
}
dict["mrfz"] = "明日方舟"  # 添加键值对
dict["LOL"] = "League of Legends"  # 修改键值对

x = input("请输入缩写：")
if x in dict:
    print(dict[x])
else:
    print("没有这个缩写")
    print("当前已有" + str(len(dict)) + "个缩写")
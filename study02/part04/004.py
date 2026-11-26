# def 不定长参数 
# 位置传递  (被封装到元组中)
def calc_data_1(*args):        #*a *b 都可以
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    return min_data,max_data,round(avg_data,1) 

print(calc_data_1(10,35,35,22,0,12,1,9))

# 关键字传递   (被封装到字典中)
def calc_data_2(*args,**kwargs):        #*a *b 都可以
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值:{min_data} 最大值:{max_data} 平均:{avg_data}")

    return min_data,max_data,avg_data


print(calc_data_2(10,35,35,22,0,round = 3,print = True))
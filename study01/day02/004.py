# for 增强
x_dict = {"1":36,"2":37,"3":38,"4":39,"5":40}

for a in x_dict.items(): #x_tuple是一个元组 可以任意取名
    x1 = a[0]
    x2 = a[1]
    if x2 >= 38:
        print(x1)
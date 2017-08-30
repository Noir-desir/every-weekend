def cal(i,j,l):
    """计算小于1000的立方和"""
    sum = i**3+j**3+l**3
    if sum <1000:
        return str(sum)

def screen(c,i,j,l):
    """选出阿姆斯特朗数"""
    b = str(i)+str(j)+str(l) #转换为字符串
    if c == b:
        print(c,"=",i,j,l)

def start():
    """制造循环函数，并运行"""
    for i in range(10):
        for j in range(10):
            for l in range(10):  #循环叠加，生成三位数
                c=cal(i,j,l)
                screen(c,i,j,l) 
start()
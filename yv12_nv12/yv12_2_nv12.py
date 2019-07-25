import numpy as np

def yv12_nv12_function_3(yv12_list,height=6,width=10):

    count=height*width*3//2  # 总的元素数
    nv12_list=[]             # 构造一个列表，用于存储转换之后的元素
    nv12_list.extend(yv12_list[0:height*width:1])

    for index in range(0,height//2,1):
        begin=width*height+width*index
        center=begin+width//2
        end=begin+width

        u=yv12_list[begin:center:1]
        v=yv12_list[center:end:1]
        tmp=insert_b_to_a(u,v)

        nv12_list.extend(tmp)

    return nv12_list

# 定义一个函数，将一个列表b插孔到另外一个列表a中，返回插空之后的列表
def insert_b_to_a(a,b):
    assert len(a)==len(b)
    tmp=[]
    for i in range(len(a)):
        tmp.append(a[i])
        tmp.append(b[i])

    return tmp

if __name__ == '__main__':
    # 假设用1表示Y，2表示U，3表示V,假设有一张（10,6）的 yuv 图片，则原始的 yv12 存储格式如下：

    # x=[1,1,1,1,1,1,1,1,1,1,
    #    1,1,1,1,1,1,1,1,1,1,
    #    1,1,1,1,1,1,1,1,1,1,
    #    1,1,1,1,1,1,1,1,1,1,
    #    1,1,1,1,1,1,1,1,1,1,
    #    1,1,1,1,1,1,1,1,1,1,
    #    2,2,2,2,2,3,3,3,3,3,
    #    2,2,2,2,2,3,3,3,3,3,
    #    2,2,2,2,2,3,3,3,3,3]
    
    x=np.random.randint(low=1,high=100,size=(90,))
    x=list(x)
    # print(x)
    y=yv12_nv12_function_3(x)
    # print(y)

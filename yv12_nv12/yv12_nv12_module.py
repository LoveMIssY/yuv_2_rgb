# file：yv12_nv12_module.py
# author：滕健
# 本模块 实现从 yv12 到 nv12 格式的转化，一共实现了两个方法，即
# yv12_nv12_function_1和yv12_nv12_function_2，均已验证
import cv2
import numpy as np

from get_yuv import yuv_from_picture # 导入自定义模块

def yv12_nv12_function_1(filename=None,height=240,width=320):

    img_yv12=yuv_from_picture(filename,height,width)
    
    uv_heigt=height//2
    uv_width=width//2
    img_yv12=np.array(img_yv12)

    for i in range(height,height+uv_heigt,1):
        for j in range(1,uv_width,2):
            img_yv12[i,j],img_yv12[i,j+(uv_width-1)]=img_yv12[i,j+(uv_width-1)],img_yv12[i,j]

    return img_yv12  # 返回 yv12经过变换之后的 nv12格式

def yv12_nv12_function_2(filename=None,height=240,width=320):
   
    img_yv12=yuv_from_picture(filename,height,width)
    uv_heigt=height//2
    uv_width=width//2

    img_yv12=np.array(img_yv12)
    img_nv12=np.copy(img_yv12)  # 新建一个和yv12 一样大小的 nv12
   
    index_u=np.arange(1,uv_width,2)
    index_v=np.arange(uv_width,width,2)

    for i in range(height,height+uv_heigt,1):
        img_nv12[i,index_u]=img_yv12[i,index_v]
        img_nv12[i,index_v]=img_yv12[i,index_u]

    return img_nv12

if __name__ == '__main__':
    img_nv12=yv12_nv12_function_2("./yuv_files/img_320x240.yuv",240,320)
    print(np.shape(img_nv12)) # (360,320)

    bgr_img = cv2.cvtColor(img_nv12, cv2.COLOR_YUV2BGR_NV12) 
    cv2.imshow("img_nv12",bgr_img)
    cv2.waitKey()

# file：get_yuv.py
# author：滕健
# 由于 YUV文件都是原生的 raw 数据，所以是没有办法获得长和宽的，只有事先认为指定，
# 我可以任意更改长和宽，但是很有可能显示出来就是一个乱七八糟的东西
# 本模块实现了两个方法，yuv_from_vedio是从一个yuv视频中提取每一帧，yuv_from_picture是获取一张单独的yuv图像

import cv2
import numpy as np

def yuv_from_vedio(filename, height, width, startframe):
    """
    param:
        filename: 待处理 YUV 视频的名字
        height: YUV 视频中图像的高
        width: YUV 视频中图像的宽
        startframe: 起始帧
    return: 
        None
    """
    fp = open(filename, 'rb')

    framesize = height * width * 3 // 2  # 一帧图像所含的像素个数
    uv_height = height // 2
    uv_width = width // 2

    fp.seek(0, 2)   # 设置文件指针到文件流的尾部
    ps = fp.tell()  # 当前文件指针位置
    numfrm = ps // framesize  # 计算输出帧数
    print(f"该YUV视频一共有 {numfrm} 帧")

    fp.seek(framesize * startframe, 0)

    for i in range(numfrm - startframe):
        Yt = np.zeros(shape=(height, width), dtype='uint8', order='C')
        Ut = np.zeros(shape=(uv_height, uv_width), dtype='uint8', order='C')
        Vt = np.zeros(shape=(uv_height, uv_width), dtype='uint8', order='C')

        for m in range(height):
            for n in range(width):
                Yt[m, n] = ord(fp.read(1))
        for m in range(uv_height):
            for n in range(uv_width):
                Ut[m, n] = ord(fp.read(1))
        for m in range(uv_height):
            for n in range(uv_width):
                Vt[m, n] = ord(fp.read(1))

        UV_cat = np.concatenate((Ut,Vt),axis=1)
        img = np.concatenate((Yt,UV_cat),axis=0)  # YUV 的存储格式为：YV12（YYYY UUVV）
       
        bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_NV12)  # 注意 YUV 的存储格式
        cv2.imwrite(f'./pictures/yuv2bgr_{i+1}.jpg', bgr_img)
        print(f"Extract frame {i+1} ")
        
    fp.close()
    print("视频帧提取完成!")
    return None

def yuv_from_picture(filename, height, width):
    """
    param:
        filename: 待处理 YUV 图片的名字
        param height: YUV 图片的高
        param width: YUV图片的宽

    return: 
        img: 返回yv12 的数据格式
    """
    fp = open(filename, 'rb')  

    framesize = height * width * 3 // 2  # 一帧图像所含的像素个数
    uv_height = height // 2
    uv_width = width // 2

    Yt = np.zeros(shape=(height, width), dtype='uint8', order='C')
    Ut = np.zeros(shape=(uv_height, uv_width), dtype='uint8', order='C')
    Vt = np.zeros(shape=(uv_height, uv_width), dtype='uint8', order='C')

    for m in range(height):
        for n in range(width):
            Yt[m, n] = ord(fp.read(1))
    for m in range(uv_height):
        for n in range(uv_width):
            Ut[m, n] = ord(fp.read(1))
    for m in range(uv_height):
        for n in range(uv_width):
            Vt[m, n] = ord(fp.read(1))

    UV_cat = np.concatenate((Ut,Vt),axis=1)
    img = np.concatenate((Yt,UV_cat),axis=0)  # YUV 的存储格式为：YV12（YYYY UUVV）
       
    bgr_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR_YV12)  # opencv不能直接读取YUV文件，需要转化注意 YUV 的存储格式
    cv2.imwrite(f'./yuv2bgr.jpg', bgr_img)
      
    fp.close()
    return img

if __name__ == '__main__':
    pass
    #yuv_from_vedio(filename='./yuv_files/akiyo_cif.yuv', height=288, width=352, startframe=0)
    #yuv_from_picture(filename='./yuv_files/img_320x240.yuv', height=240, width=320)

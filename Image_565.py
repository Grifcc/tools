import cv2  #opencv-python

def rgb888tobgr565(img):  #cv2读入文件为GBR
    r=img[0]
    g=img[1]
    b=img[2]
    r=bin(r>>3)[2:]       #取高位
    g=bin(g>>2)[2:]
    b=bin(b>>3)[2:]
    r5=r.zfill(5)          #填充
    g5=g.zfill(6)
    b5=b.zfill(5)
    result=hex(int(b5+g5+r5,2))
    return result



try:
    path=input('输入图片路径：(正斜杠/路径)')
    size=input('输入取模分辨率：')

    name=path.split('/')[-1].split('.')[0]
    width=int(size.split('*')[0])
    height=int(size.split('*')[1])

    with open('./'+name+'.c',mode='a') as cf:

        cf.write('const uint16_t {}[{}] PROGMEM='.format(name,eval(size)))
        cf.write('{\n')

        img= cv2.imread(path)
        img = cv2.resize(img, (width,height))   #调整分辨率

        m=0
        for x_index, x in enumerate(img):
            for y in x:
                m+=1
                res=rgb888tobgr565(y)
                cf.write(res.ljust(6,'0')+',')         #填充对齐
                if(m%16==0):                           #换行写入
                    cf.write('\n')

        cf.write('\n };')
except Exception as e:
    print(e)

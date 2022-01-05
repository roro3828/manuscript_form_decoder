import cv2

def to_bin(x):
    if x<128:
        x=1
    else:
        x=0
    return x

def get_corner(img):
    height,width=img.shape[:2]
    sy=0
    while(128<=img[sy,round(width/2)]):
        sy+=1
    sx=0
    while(128<=img[round(height/2),sx]):
        sx+=1
    ey=height-1
    while(128<=img[ey,round(width/2)]):
        ey-=1
    ex=width-1
    while(128<=img[round(height/2),ex]):
        ex-=1
    return [(sy,sx),(ey,ex)]

path_list=[
    #画像のパス
    ]
codes=[]
for index in range(len(path_list)):
    img=cv2.cvtColor(cv2.imread(path_list[index]),cv2.COLOR_BGR2GRAY)
    pos=get_corner(img)
    h=(pos[1][0]-pos[0][0])/20
    if index==0:
        w=(pos[1][1]-pos[0][1])/22
    else:
        w=(pos[1][1]-pos[0][1])/21
    offset=tuple(map(round,(pos[0][0]+h*1.5,pos[0][1]+w*0.35)))

    r=list(range(20,-1,-1))
    if index==0:
        r.remove(20)
    r.remove(10)
    c=list(range(18))
    c.remove(8)
    c.remove(9)
    x=0
    for i in r:
        for j in c:
            pos=tuple(map(round,(offset[0]+h*j,offset[1]+w*i)))
            x=(x<<1)+to_bin(img[pos])
            if j==7 or j==17:
                codes.append(x)
                x=0
            #cv2.circle(img,(pos[1],pos[0]),5,127,-1)
    #cv2.imshow('pic',img)
    #cv2.waitKey(0)

print(bytes(codes).decode())

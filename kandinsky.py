from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=321, height=223, background='#fff')
canvas.pack()
colors=[[(255, 255, 255) for i in range(223)] for i in range(321)]

def color(a,b,c):
    if a<10:
        va='0'+str(a)
    else:
        va=hex(a%256).replace('0x','')
    if b<10:
        vb='0'+str(b)
    else:
        vb=hex(b%256).replace('0x','')
    if c<10:
        vc='0'+str(c)
    else:
        vc=hex(c%256).replace('0x','')
    return '#%s'%(va+vb+vc)

def colr(lis):
    a=lis[0]
    b=lis[1]
    c=lis[2]
    if a%256<10:
        va='0'+str(a%256)
    else:
        va=hex(a%256).replace('0x','')
    if b%256<10:
        vb='0'+str(b%256)
    else:
        vb=hex(b%256).replace('0x','')
    if c%256<10:
        vc='0'+str(c%256)
    else:
        vc=hex(c%256).replace('0x','')
    return '#%s'%(va+vb+vc)

def fill_rect(a,b,c,d,e):
    if type(e)==str:
        canvas.create_rectangle(a+2,b+2,c+a+2,d+b+2,fill=e,outline='')
    else:
        canvas.create_rectangle(a+2,b+2,c+a+2,d+b+2,fill=colr(e),outline='')
    #modifie la valeur de la couleur au pixel x,y
    for x in range(c):
        for y in range(d):
            if (a+x)>=0 and (a+x)<=320 and (b+y)>=0 and (b+y)<=222:
                colors[a+x][b+y]=e
def set_pixel(a,b,e):
    fill_rect(a,b,1,1,e)

def get_pixel(x,y):
    if x>=0 and x<=320 and y>=0 and y<=222:
        return colors[x][y]
    else:
        return (0,0,0)
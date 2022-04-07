def interp(x,x1,x2,y1,y2):
    y = y1 + (x-x1)*(y2-y1)/(x2-x1)
    print(y)


interp(152,150,155,66.1,66)
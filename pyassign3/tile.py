schemes = []
def main():
    '''有一面墙, 规格为 长 m 宽 n 的长方形,
    现在要把规格为 长 a 宽 b 的 长方形瓷砖铺满该墙面,
    输出所有的铺法, 用户可以选定某种铺法, 输出对应的turtle图形进行可视化。
    墙的位置的编号：把墙分割为1*1的正方形，左下角的正方形编号为0.
                    往右依次为1,2,3，...，m-1.
                    0上面的正方形是m,往右依次为m+1,m+2,...,2m-1.
                    墙用列表表示，位置i空着时，列表的i号元素为0，否则为1.
    瓷砖位置的表示方法：用元组表示出瓷砖占有的墙的位置编号。
                        判断能否填入时，start表示把瓷砖分割成1*1的正方形，
                        当左下角填入start位置时，能否整个填入。'''
    def can_add(m,n,a,b,start,wall): 
        '''Find the first location which can add a horizontal tile to.'''
        boo = True  #记录结果，经过下面的过程后，boo为True表示能填入，False表示不能填入。
        boo = boo and start // m <= (n - b) #起始位置不能太靠上。
        boo = boo and start % m <= (m - a)  #起始位置不能太靠右。
        for j in range(b):   #要求填入前，瓷砖将要占有的位置必须是空的。
            for k in range (start,start + a):
                boo = boo and wall[k + m * j] == 0
        return boo

    def added_wall(m,n,a,b,start,wall):
        '''Add a tile to the wall and return the new wall.'''
        for j in range(b):  #把瓷砖填进去，其实就是将墙上对应部分修改为1.
            for k in range(start,start + a):
                wall[k + j * m] = 1
        return wall

    def added_scheme(m,n,a,b,start,scheme):
        '''Add a tile to the scheme and return the new scheme'''
        tile = []
        for j in range(b): #找出新添的瓷砖所有占位编号。
            for k in range(start,start + a):
                tile = tile + [k + j * m]
        tile = tuple(tile)
        scheme = scheme + [tile] 
        return scheme

    def all_schemes1(m,n,a,b,wall,scheme):
        '''Return the results if a != b.'''
        if 0 not in wall:  #此时证明墙已填满，说明方案成功，把方案加入方案集合。
            global schemes       #此处声明schemes是全局变量。
            schemes = schemes + [scheme]  
        else:#此处需要递归，原来的总方案=横着填后的总方案+竖着填后的总方案
            scheme1 = scheme[:] #备份方案，一个用于横着一个用于竖着。
            scheme2 = scheme[:]
            wall1 = wall[:]
            wall2 = wall[:]
            start = -1 #保证start是有意义的，防止使用前未定义。
            for i in range(m * n): #找出第一个能填的位置（不管横着还是竖着）
                if can_add(m,n,a,b,i,wall1) == True or can_add(m,n,b,a,i,wall1) == True:
                    start = i
                    break
            if start != -1:#表示找到了能填的位置。
                if can_add(m,n,a,b,start,wall) == True:#横着填
                    wall1 = added_wall(m,n,a,b,start,wall1)
                    scheme1 = added_scheme(m,n,a,b,start,scheme1)
                    all_schemes1(m,n,a,b,wall1,scheme1)
                if can_add(m,n,b,a,start,wall) == True:#竖着填
                    wall2 = added_wall(m,n,b,a,start,wall2)
                    scheme2 = added_scheme(m,n,b,a,start,scheme2)
                    all_schemes1(m,n,a,b,wall2,scheme2)

    def all_schemes2(m,n,a,b,wall,scheme):
        '''Return the results if a == b'''
        if 0 not in wall:  #此时证明墙已填满，说明方案成功，把方案加入方案集合。
            global schemes       #此处声明schemes是全局变量。
            schemes = schemes + [scheme]  
        else:#此处需要递归.
            start = -1 #保证start是有意义的，防止使用前未定义。
            for i in range(m * n): #找出第一个能填的位置.
                if can_add(m,n,a,b,i,wall) == True or can_add(m,n,b,a,i,wall) == True:
                    start = i
                    break
            if start != -1:#表示找到了能填的位置。
                if can_add(m,n,a,b,start,wall) == True:
                    wall = added_wall(m,n,a,b,start,wall)
                    scheme = added_scheme(m,n,a,b,start,scheme)
                    all_schemes2(m,n,a,b,wall,scheme)
            
    m = int(input('Please input the length of the wall.'))
    n = int(input('Please input the width of the wall.'))
    a = int(input('Please input the length of the tile.'))
    b = int(input('Please input the width of the tile.'))
    
    wall = [0] * m * n #记录初始状态
    scheme = []
    if a != b:
        all_schemes1(m,n,a,b,wall,scheme) #此函数将结果记录在全局变量schemes中。
    else:
        all_schemes2(m,n,a,b,wall,scheme) #此函数将结果记录在全局变量schemes中。
    for s in schemes:
        print(s)

    import turtle
    num = int(input('Please input the scheme.'))
    chosen = schemes[num]
    bob = turtle.Turtle()
    bob.up()
    x0 = -m * 50 / 2 #设置原点坐标使得图形在正中央，令小正方形边长为50.
    y0 = -n * 50 / 2
    bob.setx(x0)
    bob.sety(y0)
    bob.down()
    def coordinate(m,num):
        '''Return the coordinate of the lower-left corner
           of a loacation of the square.''' 
        x = x0 + 50 * (num % m)
        y = y0 + 50 * (num // m)
        return (x,y)
    def tile1(tile):
        '''Draw the tile which has been just added.'''
        co1 = coordinate(m,tile[0])         #瓷砖左下角的坐标。
        co2 = coordinate(m,tile[a * b - 1]) #瓷砖右上角的坐标。
        bob.up()
        bob.goto(co1)                       #确定初始位置。
        bob.down()
        bob.goto(co2[0] + 50,co1[1])        #画出这个瓷砖。
        bob.goto(co2[0] + 50,co2[1] + 50)
        bob.goto(co1[0],co2[1] + 50)
        bob.goto(co1)
    for tile in chosen:
        tile1(tile)
    
                 
if __name__ == '__main__':
    main()

##input x and y
x,y=input().split(" ")
##typecast x and y
x=int(x)
y=float(y)
requiredBalance=x+0.50
if y>=requiredBalance and x%5==0 :
    balance=y-requiredBalance
    print('%.2f' % balance)
else:
    print('%.2f' % y)


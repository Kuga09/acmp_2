input_data = open('input.txt','r') # Открываем для чтения файл
data = input_data.readlines() # Читаем в другую переменную содержимое всего файла
a=str(data[0])
d=str(data[1])
a=a.split()
d=d.split()
x1=float(a[0])
y1=float(a[1])
x2=float(a[2])
y2=float(a[3])
xA=float(d[0])
yA=float(d[1])
if x1==x2:
    xB=2*x1-xA
    yB=yA
if y1==y2:
    xB=xA
    yB=2*y1-yA
output_data = open('output.txt','w')
output_data.write(str(int(xB)))
output_data.write(" ")
output_data.write(str(int(yB)))
input_data.close()
output_data.close()

'''if x1!=x2 and y1!=y2:
    k1=(y2-y1)/(x2-x1)
    k2=1/k1*-1
    b1=y1-k1*x1
    b2=yA-k2*xA
    x=(b2-b1)/(k1-k2)
    y=k1*x+b1
    xB=2*x-xA
    yB=2*y-yA''' #решение для любой прямой
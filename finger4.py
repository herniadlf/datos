import sys
a=int(sys.argv[1]);b=2
while b<a:
    if a%b==0:break
    b+=1
print int(b==a)

import random
codes=["+91"]

pl=int(input("Pass length(6-11): "))
for i in range(10000):
    x=""
    while len(x)!=8:
      x=str(random.randint(00000000,99999999))
      

    num=str(random.choice(codes))+x
    pw=num[-pl:]
    print (num,pw)

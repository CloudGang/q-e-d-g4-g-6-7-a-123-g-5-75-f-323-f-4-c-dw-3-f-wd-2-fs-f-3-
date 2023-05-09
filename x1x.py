def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();print(D)
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)
x1x()

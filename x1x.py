import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!");st.write(f":orange[Black-Key Code: ]:green[{D}]")
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)
x = st.button('Get Black-Key: ')
if x:
  x(disabled=True)
  x1x()

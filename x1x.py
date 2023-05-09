import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!")
  with col2
    st.write(f":orange[Black-Key Code: ]:green[{D}]")
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)

col1,col2 = st.columns(1)
with col1:
  x=st.button('Get Black-Key: ')
  if x:
    del col1
    x1x()

  

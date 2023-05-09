import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!")
  with col2:
    st.write(f":orange[Black-Key Code: ]:green[{D}]")
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)
cust = ["@","#"]
ID = st.text_input("Transaction ID")
col1,col2 = st.columns(2)
with col1:
  placeholder = st.empty()
  if cust in ID:
    isclick = placeholder.button('Get Black-Key Code')
    if isclick:
        placeholder.empty()
        x1x()

  

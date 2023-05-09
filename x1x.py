import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!");st.write(":green[If you see Brackets :orange[[ ]], Your code is :orange['['] BETWEEN :orange[']'] the brackets.]")
  with col2:
    st.write(f":orange[Black-Key Code: ]:green[{D}]")
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)
cust = ["BBW6843311"]
ID = st.text_input("Enter your Paypal Item ID#","ie: BB3871")
col1,col2 = st.columns(2)
with col1:
  placeholder = st.empty()
  if ID in cust:
    isclick = placeholder.button('Get Black-Key Code')
    if isclick:
        placeholder.empty()
        x1x()

  

import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!");st.write("If you see Brackets :orange[[ ]], Your code is :orange[ [:green[BETWEEN] ]] the brackets.")
  with col2:
    html_string = f'<a href="mailto:{em}?subject=Black-Key Code{D}&body={D}">Get Key</a>'
    st.markdown(html_string, unsafe_allow_html=True)
    st.write(f":orange[Black-Key Code: ]:green[{D}]")
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)

cust = ["BBW6843311"]
ID = st.text_input("Enter your Paypal Item ID#","ie: BB3871")
em = st.text_input("Enter your Email to reieve Key")

col1,col2 = st.columns(2)
with col1:
  placeholder = st.empty()
  if ID in cust:
    isclick = placeholder.button('Check ID')
    if isclick:
        placeholder.empty()
        x1x()



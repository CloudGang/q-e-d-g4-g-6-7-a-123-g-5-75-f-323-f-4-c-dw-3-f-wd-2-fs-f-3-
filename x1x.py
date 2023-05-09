import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!");st.write("If you see Brackets :red[[ ]], Your code is :red[ [:green[BETWEEN] ]] the brackets.")
  with col2:
    st.write(f":orange[Black-Key Code: ]:green[{D}]")
  with col3:
    em = st.text_input("Enter your Email to reieve Key")
    html_string = f'<a href="mailto:{em}?subject=Black-Key Code{D}&body={D}">Click to send Email</a>'
    st.markdown(html_string, unsafe_allow_html=True)
  with open(B,'r')as A:
    E=A.readlines()
    with open(B,'w')as A:
      for F in E[1:]:A.write(F)

cust = ["BBW6843311"]
ID = st.text_input("Enter your Paypal Item ID#","ie: BB3871")

col1,col2,col3 = st.columns(3)
with col1:
  placeholder = st.empty()
  if ID in cust:
    isclick = placeholder.button('Check ID')
    if isclick:
        placeholder.empty()
        if "!NO" in D:
          st.write('No Key, Contact Site Admin')
        else:
          x1x()



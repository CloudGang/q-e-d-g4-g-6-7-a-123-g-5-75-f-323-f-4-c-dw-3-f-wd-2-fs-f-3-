import streamlit as st

def x1x():
  B='o.txt';C=open(B,'r');D=C.readline();st.write("Save Your Key!");st.write("If you see Brackets :orange[[ ]], Your code is :orange[ [:green[BETWEEN] ]] the brackets.")
  with col2:
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
    isclick = placeholder.button('Get Black-Key Code')
    if isclick:
        placeholder.empty()
        x1x()

html_string = f"""
<p><input id="subject" type="text" placeholder="type your subject here" 
    class="form-control"></p>
<p><input id="message" type="text" placeholder="type your message here" 
    class="form-control"></p>
<p><a id="mail-link" class="btn btn-primary">Create email</a></p>
JavaScript (with jQuery):

<script type="text/javascript">
    function loadEvents() {
        var mailString;
        function updateMailString() {
            mailString = '?subject=' + encodeURIComponent($('#subject').val())
                + '&body=' + encodeURIComponent($('#message').val());
            $('#mail-link').attr('href',  'mailto:person@email.com' + mailString);
        }
        $( "#subject" ).focusout(function() { updateMailString(); });
        $( "#message" ).focusout(function() { updateMailString(); });
        updateMailString();
    }
</script>
"""
st.markdown(html_string, unsafe_allow_html=True)

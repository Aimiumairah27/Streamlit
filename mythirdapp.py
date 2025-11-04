#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Page Setup
st.set_page_config(page_title='Colors and Layout')

st.title("Colors , Layout & Charts")
st.write("Let's Make Our App Beautiful and Organized")

st.markdown("""
<div style="background-color:#E3E3A6;padding:20px;border-radius:10px;">
<h3 style="color:#451108">HTML Style Using Markdown</h3>
<p>This is HTML Paragraph Tag</p>
</div>
""",unsafe_allow_html=True)

# markdown
st.markdown("\n")
# display text in bold and italic
st.markdown("**Streamlit** is python library for creating interactive *web apps*")
# links
st.markdown("Visit For More Info : (htpps://streamlit.io) *To Learn* **Streamlit**")

# code()
code1 = '''def hello():
     print('Hi i am python function')'''

st.code(code1,language="python")

# Latex()
st.latex('''
(a+b)^2= a^2 + b^2 + 2*a*b
''')

st.markdown("\n")
st.markdown("**Sigmoid Function**")
st.latex(r'''
\frac {1}(1+e^-score)
''')


# Layouts
         


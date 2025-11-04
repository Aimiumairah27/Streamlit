#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title("😎 Exploring Streamlit Widgets")
 
st.header("Text and Title")
st.write("This is **bold text.** This is *italic text*")
 
st.header("Using Slider")
age = st.slider("Select Your Age",1,100,24)
st.write("Your Age Is 👨‍🦳 : ",age)
 
st.header("Taking User Input")
name = st.text_input("What's Your Name ?")
if name:
    st.success(f"Nice To Meet You {name}! 👏")
 
st.header("Button Example")
if st.button("Click Me!"):
    st.balloons()  # pops balloon animation


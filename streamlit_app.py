import streamlit as st
import pandas as pd


st.title("Balloon counter")

if 'counter' not in st.session_state.keys():
    st.session_state['counter'] = 0

if st.button("Click if you want to see balloons"):
    st.balloons()
    st.session_state['counter'] += 1

st.write(f"you've hit the button {st.session_state['counter']} times")



my_title = st.empty()

user_choice = st.radio("Which is best?", options = ['Cats', 'Dogs'])

my_title.title(f"You've picked {user_choice}")



sweets = st.slider("Number of sweets you eat in one day:", 0, 100, step=5)

if sweets < 10:
    st.write("Good")
elif sweets < 50:
    st.write("Not so good")
else:
    st.write("Are you OK?")

col1,col2,col3 = st.columns(3)
col1.write("COL1")
col2.write("COL2")
col3.write("COL3")
with col1:
    st.write("iuusfiudsf")
    st.write("oiseofusaidfu")
import streamlit as st

st.header("Hi, You")
st.subheader("May I know your name?")

user_input = st.text_input("Enter your name here:")

name = ["Januar Santoso", "januar santoso", "anu", "janu", "jan", "santoso", "nuar", "Januar", "januar"]

if user_input.lower() in name:
    st.write("Hii", user_input.upper(), "or may I call you Anu?")
    st.write("I hope you are very well today")
    st.write("This is your favorite music right?")
    st.video("https://www.youtube.com/watch?v=_G0WKkjgNU4")

    st.write("Are you happy? hehehe i hope so")
    st.image("https://www.sweasy26.com/emoticons/images/happy-2.png")

if user_input.lower() not in name and user_input.strip() != "":
    st.write("Lie, please give me your real name")
    st.image("https://www.sweasy26.com/emoticons/images/sad-2.png")
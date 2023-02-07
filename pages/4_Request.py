import streamlit as st
import smtplib

sender  = 'streamlit2fnhe@gmail.com'
password = 'vvljquqzjrqleduy' 
receiver = 'lalalaxf93@gmail.com'



with st.form('PDX data request'):
    ids = st.text_area("Enter the PDX IDs you intereted")

    col1, col2 = st.columns(2)
    with col1:
        fn = st.text_input("First Name")
    with col2:
        ln = st.text_input("Last Name")

    col1, col2, col3 = st.columns(3)
    with col2:
        ins = st.text_input("Institution")
    with col3:
        country = st.text_input("Country")
    with col1:
        pos = st.selectbox("Your position", ['', 'Researcher','Professor','Student','Other'])


    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email") 
    with col2:
        phone = st.text_input("Phone number")
    other = st.text_area("Other")
    submit_info = st.form_submit_button(label = 'Submit', on_click=print,)

    if submit_info:
        if email and ids and ins and fn:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, 'vvljquqzjrqleduy')
            st.success('Thank you for your inquiry! The email have been sented!')
            
            message = submit_info
            server.sendmail(sender, receiver, message)
        else:
            st.warning('Please fill PDX IDs, Email, Institute and Name')

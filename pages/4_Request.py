import streamlit as st
import smtplib

sender  = 'streamlit2fnhe@gmail.com'
password = 'vvljquqzjrqleduy' 
receiver = 'lalalaxf93@gmail.com'



form = st.form('PDX data request'):
ids = form.text_area("Enter the PDX IDs you intereted")
col1, col2 = form.columns(2)
with col1:
    fn = form.text_input("First Name")
with col2:
    ln = form.text_input("Last Name")
col1, col2, col3 = form.columns(3)
with col2:
    ins = form.text_input("Institution")
with col3:
    country = form.text_input("Country")
with col1:
    pos = form.selectbox("Your position", ['', 'Researcher','Professor','Student','Other'])
col1, col2 = form.columns(2)
with col1:
    email = form.text_input("Email") 
with col2:
    phone = form.text_input("Phone number")
other = form.text_area("Other")
form.form_submit_button(label = 'Submit')

if form:
    if email and ids and ins and fn:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, 'vvljquqzjrqleduy')
        st.success('Thank you for your inquiry! The email have been sented!')
        
        message = submit_info
        server.sendmail(sender, receiver, message)
    else:
        st.warning('Please fill PDX IDs, Email, Institute and Name')

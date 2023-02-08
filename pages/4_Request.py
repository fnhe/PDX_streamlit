import streamlit as st
import smtplib

sender  = 'streamlit2fnhe@gmail.com'
password = 'vvljquqzjrqleduy' 
receiver = 'lalalaxf93@gmail.com'

def send_email(to, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail('sender_email_address@gmail.com', to, message)
        server.quit()
        st.success("Email sent successfully!")
    except Exception as e:
        st.error("Failed to send email: " + str(e))

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
    res = st.form_submit_button(label = 'Submit')

if res:
    if email and ids and ins and fn and phone and country:
        #server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.starttls()
        #server.login(sender, 'vvljquqzjrqleduy')
        st.success('Thank you for your inquiry!')
        
        subject = 'PDX data request (streamlit)' 
        basic_info = """
        --------------------------------\n
        Subject: {}\n
        Email: {}\n
        Full Name: {} {} \n 
        Phone: {}\n
        Institute: {}, {} \n        
        --------------------------------\n\n""".format(subject, email, fn, ln, phone, ins, country)
        id_info = """
        ID Request:\n
        {}\n
        --------------------------------\n\n""".format(ids)
        message = basic_info + id_info 
        if other:
            other_info = """Other info: {}\n""".format(other)
            message = message + other_info
        send_email(receiver, subject, message)
    else:
        st.warning('Please fill PDX IDs, Email, Name, Phone, Institute and Country')

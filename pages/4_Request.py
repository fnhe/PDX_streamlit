import streamlit as st
import email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication

def send_email(sender, password, receiver, smtp_server, smtp_port, email_message, subject = 'Data request from streamlit'):
    message =  MIMEMultipart()
    message['To'] = Header(receiver)
    message['From'] = Header(sender)
    message['Subject'] = Header(subject)
    message.attach(MIMEText(email_message, 'plain', 'utf-8'))

    server = smtplit.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    text = message.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

with st.form('PDX data request'):
	ids = st.text_area("Enter the PDX IDs you intereted")
	#ids = st.file_uploader('Attachment')

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
	submit_info = st.form_submit_button(label = 'Submit')

	if submit_info:
		if email and ids and ins and fn:
			st.success('Thank you for your inquiry! The email have been sented!')
			message = submit_info
			#send_email(sender = 'lalalaxf93@gmail.com', password='hfl_1993', receiver='lalalaxf93@gmail.com', smtp_server = 'smtp.gmail.com', smtp_port = 587, email_message = message)
		else:
			st.warning('Please fill PDX IDs, Email, Institute and Name')

st.help(st.form)
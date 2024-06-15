"""
https://mailtrap.io/home 으로 이메일 테스트 서비스를 사용함
"""
import os
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No JSON data received"}), 400

    to_email = data.get('to_email')
    subject = data.get('subject')
    message = data.get('message')
    from_email = os.getenv('MAILTRAP_USER') 

    try:
        send_email_smtp(from_email, to_email, subject, message)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def send_email_smtp(from_email, to_email, subject, message):
    smtp_server = 'sandbox.smtp.mailtrap.io'
    smtp_port = 2525
    smtp_user = os.getenv('USER')
    smtp_password = os.getenv('PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

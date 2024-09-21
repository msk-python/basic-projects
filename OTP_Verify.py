import random
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta

# Configuration
# OTP_EXPIRATION_TIME = timedelta(minutes=5)  # OTP valid for 5 minutes
OTP_EXPIRATION_TIME = timedelta(seconds=30)  # OTP valid for 30 Seconds

# Read credentials
try:
    with open('private/gmail_server_account/gmail.txt', 'r') as file:
        my_gmail = file.read().strip()
except FileNotFoundError:
    my_gmail = None
    print("Your gmail file not found")

try:
    with open('private/gmail_server_account/password.txt', 'r') as file:
        my_password = file.read().strip()
except FileNotFoundError: 
    my_password = None
    print("Your password file not found")    

# Users data
users = {
    'sumit8393': 'iamtrynow@gmail.com',
}

# OTP storage
otp_data = {}

def create_OTP():
    return random.randrange(111111, 999999)

def send_gmail(receiver_gmail: str, subject: str, message: str):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_gmail, my_password)
        email = EmailMessage()
        email['From'] = "MSK Institute"
        email['To'] = receiver_gmail
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        print(f"OTP sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()

def generate_and_send_otp(user_name):
    otp = create_OTP()
    expiration_time = datetime.now() + OTP_EXPIRATION_TIME
    receiver_gmail = users[user_name]
    subject = "OTP for login form python program."
    message = (
        f"Please do not share OTP with anyone.\n\n"
        f"Your OTP: {otp}\n"
        f"This OTP is valid until: {expiration_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"If you did not request this OTP, please ignore this message."
    )
    send_gmail(receiver_gmail, subject, message)
    otp_data[user_name] = {
        'otp': otp,
        'timestamp': datetime.now()
    }
    print("OTP sent to your Gmail.")
    return otp

def verify():
    while True:
        os.system('cls')
        user_name = input('Enter username: ')
        if user_name in users.keys():
            otp = generate_and_send_otp(user_name)
            while True:
                user_otp = input('Enter OTP: ')
                current_time = datetime.now()
                if user_otp == str(otp):
                    otp_info = otp_data[user_name]
                    if current_time - otp_info['timestamp'] <= OTP_EXPIRATION_TIME:
                        print("Login Successful!")
                        del otp_data[user_name]  # Clear OTP after successful login
                        return
                    else:
                        print("OTP expired. Please request a new OTP.")
                        del otp_data[user_name]  # Clear expired OTP
                        break
                else:
                    print("Invalid OTP. Please try again.")
        else:
            print("User not found. Please create a new account.")

def log_In():
    verify()

log_In()

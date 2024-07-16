# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import pandas as pd
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "swets3.it@gmail.com"
email_password = "xhpl jedd risd twof"

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = email_address
msg['To'] = "isitswet@gmail.com"
msg.set_content("This is email message")


sheet_id='1jeCvpLOfHAD95QHsegAYCWrGVpjWXNs_cXn7TifZJaQ'

df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

#print(df)


for index, row in df.iterrows():
    email = row['Email']
    interest = row['Interest']
    topic = row['Topic']
    print(email,interest,topic)

    if interest == 'Teach':
        # Iterate through the data again to find 'Learn' matches with matching topics
        for index,row1 in df.iterrows():
            other_email = row1['Email']
            other_interest = row1['Interest']
            other_topic = row1['Topic']
            #print(other_email,other_interest,other_topic)
            # Check if the other entry has an interest in 'Learn'
            if other_interest == 'Learn':
                # Check if the topics match
                if topic.lower() == other_topic.lower():
                    # Send email to 'email' and 'other_email'
                    # You can add your email sending logic here
                    #print(f"Send email to {email} and {other_email} for matching topic: {topic}")
                    msg = EmailMessage()
                    msg['Subject'] = (f"STU {other_interest}")
                    msg['From'] = email_address
                    msg['To'] = other_email
                    msg.set_content(f"Learn from {email}")
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(email_address, email_password)
                        smtp.send_message(msg)
                    
                    msg = EmailMessage()
                    msg['Subject'] = "STU"
                    msg['From'] = email_address
                    msg['To'] = email
                    msg.set_content(f"Teach to {other_email}")
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(email_address, email_password)
                        smtp.send_message(msg)



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
    
    
    
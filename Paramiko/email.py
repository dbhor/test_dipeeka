# Import smtplib for the actual sending function
import smtplib

# Define email sender and receiver
source = 'dbhormason@gmail.com'
destination = 'dbhor@juniper.net'
# Create message
from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()
# Craft email
msg['Subject'] = 'test'
msg['From'] = source
msg['To'] = destination
# Send the message
server = smtplib.SMTP('smtp.gmail.com', 587)
server.sendmail(source, [destination], msg.as_string())
server.quit()




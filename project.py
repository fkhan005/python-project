import smtplib
import string
import traceback
import sys
import argparse
import re
from email.mime.text import MIMEText


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fromaddr", help="From address", default="FROM_EMAIL_ADDR")

parser.add_argument("-t", "--toaddr", help="To address(es) - multiple split by comma", default="TO_EMAIL_ADDRESS")
parser.add_argument("-u", "--subject", help="Message Body", default="SUBJECT")
parser.add_argument("-m", "--message", help="Message Body", default="BODY")
parser.add_argument("-o", "--msgfile", help="Message Body", default="")
parser.add_argument("-s", "--server", help="SMTP Server", default="SMTP_SERVER")

parser.add_argument("-xu", "--user", help="Username", default="USERNAME")
parser.add_argument("-xp", "--password", help="Password", default="PASSWORD")
parser.add_argument("-p", "--port", help="SMTP Server Port", default=25)

args = parser.parse_args()


fromaddr = args.fromaddr
toaddrs = args.toaddr
subject = args.subject
message = args.message
message_file = args.msgfile
server_smtp = args.server
user = args.user
password = args.password
port_smtp = args.port

mssg = """ Subject: SMTP e-mail test

hi! this is our python project.
"""
sendto=input("Enter reciever's email address!")


if message_file != "":
    with open(message_file) as fp:
        message = str(MIMEText(fp.read()))

        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?][ -\/][@-~]')
        message = ansi_escape.sub('', message)


if ',' in toaddrs:
    toaddrs = toaddrs.split(",")

string = ""
BODY = string.join((
    "Subject:" + subject + "\n",
    "\n",
    message + "\n"
))

try:
    server = smtplib.SMTP(host="smtp-mail.outlook.com", port="587")
    server.starttls()
    server.set_debuglevel(True)
    server.esmtp_features['auth'] = 'STARTTLS'
    server.login("fkhan005@outlook.com", "Fkhan@1234")
    server.sendmail("fkhan005@outlook.com",sendto, mssg)
    server.quit()

except smtplib.SMTPServerDisconnected:
    print("smtplib.SMTPServerDisconnected")
except smtplib.SMTPResponseException as e:
    print("smtplib.SMTPResponseException: " + str(e.smtp_code) + " " + str(e.smtp_error))
except smtplib.SMTPSenderRefused:
    print("smtplib.SMTPSenderRefused")
except smtplib.SMTPRecipientsRefused:
    print("smtplib.SMTPRecipientsRefused")
except smtplib.SMTPDataError:
    print("smtplib.SMTPDataError")
except smtplib.SMTPConnectError:
    print("smtplib.SMTPConnectError")
except smtplib.SMTPHeloError:
    print("smtplib.SMTPHeloError")
except smtplib.SMTPAuthenticationError:
    print("smtplib.SMTPAuthenticationError")
except Exception as e:
    print("Exception", e)
    print(traceback.format_exc())
    print(sys.exc_info()[0])
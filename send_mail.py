import smtplib, ssl, email
from smtplib import SMTPResponseException
# from email import encoders
# from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config
from IPython.display import HTML


# load ENV variables
sender_email = config('SENDER_EMAIL')
receiver_email = config('RECEIVER_EMAIL')

# For multiple recipients
# recipients = ['john.otis@example.com', 'joan.mtu@example.co.ke']

password = config('PASSWORD')

# Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "Tech Jobs Notification"
msg["From"] = sender_email
msg["To"] = receiver_email

# For multiple recipients use join as shown below
# msg['To'] = ", ".join(recipients)


def compose_mail(df):
    # HTML Message Part
    jobs_table= HTML(df.to_html(classes='table table-stripped')).data
    html = """\
    <html>
      <body>
        <p><b>Brighter Monday Tech jobs</b>
        <br>
           Kindly find sample jobs as shown below.<br>
         {jobs_table}
        </p>
        
      </body>
    </html>
    """ .format(jobs_table=jobs_table)
    # print(html)

    part = MIMEText(html, "html")
    msg.attach(part)
    #
    # # Add Attachment
    # with open(filename, "rb") as attachment:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())
    #
    # encoders.encode_base64(part)

    # Set mail headers
    # part.add_header(
    #     "Content-Disposition"
    #     "attachment", filename=filename
    # )
    # msg.attach(part)

    # Create secure SMTP connection and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, msg.as_string()
            )
            print('mail sent successfully!')
        except SMTPResponseException as e:
            print(str(e))

# if __name__ == '__main__':
#     compose_mail()

import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path("data.html").read_text())
with open("emails.txt","r") as email_list:
    email_lists = email_list.readlines()

    for i in email_lists:
        email = EmailMessage()
        email["subject"] = "congra"
        current_email= i.split("\n")
        first_name = current_email[0].split(".")
        last_name = first_name[1].split("@")
        email.set_content(html.substitute({'name':f"{first_name[0]} {last_name[0]}"}),'html')
        smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login("temesgen.taye15@gmail.com" , "35583377")
        email["from"] = f"{first_name[0]}{last_name[0]}"
        email["to"] = current_email[0]
        smtp.send_message(email)
        print("done")


from datetime import datetime, timedelta, date
import os
import reports
import sys
import emails

dir = r"/home/student-00-0a14b23100e4/supplier-data/descriptions/"
list_dir = os.listdir(dir)
day = str(datetime.today().strftime('%m/%d/%y'))


def build_body(location, list):
  #Gathers descriptions frome source directory, and generates email content
  body = []
  for dp in list:
    if ".txt" in dp:
      with open(dir + dp, "r" ) as f:
        lines = f.readlines()
        body.append("name: " + lines[0])
        body.append("weight: " +  lines[1])
        body.append("\n")
    else:
      pass
  email_body = "<br/>".join(body)
  return email_body

def main(argv):
  #Using reports.py module, generates report PDF and configures email settings
  data = build_body(dir, list_dir)
  reports.generate_report("/tmp/processed.pdf", "Processed Update on " + day + "<br/>", data)
  sender = "automation@example.com"
  reciever = "student-00-0a14b23100e4@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, reciever, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
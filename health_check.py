#!/usr/bin/env python3

import psutil, shutil
import socket
import emails
import os, sys

def cpu_check():
  #checks CPU usage
  cpu_usage = psutil.cpu_percent(1)
  return not cpu_usage > 80

def disc_space_check():
  #checks disc space
  disk_usage = shutil.disk_usage("/")
  disk_total = disk_usage.total
  disk_free = disk_usage.used
  threshold = disk_free / disk_total * 100
  return threshold > 20

def available_memory_check():
  #checks available memory
  available = psutil.virtual_memory().available
  available_in_MB = available / 1024 ** 2
  return available_in_MB > 500

def hostname_check():
  #checks host ip
  local_host_ip = socket.gethostbyname('localhost')
  return local_host_ip == "127.0.0.1"

def email_warning(error):
  #configures email settings 
  sender = "automation@example.com"
  receiver = "student-00-0a14b23100e4@example.com"
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.send_email(message)

def general_check():
  #Does checks and defines email alert depending
  if not cpu_check():
    subject = "Error - CPU usage is over 80%"
    email_warning(subject)

  if not disc_space_check():
    subject = "Error - Available disk space is less than 20%"
    email_warning(subject)

  if not available_memory_check():
    subject = "Error - Available memory is less than 500MB"
    email_warning(subject)

  if not hostname_check():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    email_warning(subject)

def main(argv):
  general_check()

if __name__ == "__main__":
  main(sys.argv)
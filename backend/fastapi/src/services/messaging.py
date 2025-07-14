from abc import ABC, abstractmethod
import smtplib
import re

class MessageSender(ABC):
  @abstractmethod
  def send(self, to: str, content: str) -> bool:
    pass

class EmailSender(MessageSender):
  def send(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    
    # Replace with SendGrid, Mailgun, or your SMTP config
    log.info(f"[Email] Sending to {to}: subject:{subject} body:{body_plaintext}")
    return True

  def smtp2go(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    post_headers = {
      "Content-Type":'application/json',
      "X-Smtp2go-Api-Key":'api-7B3D74DDB6B0477EAE78FBA90BA1ADC3',
      "accept":'application/json'
      }  
    recipient_list = [to]
    payload = {
      'sender':'docker-errors@absurditiesmedia.com', 
      'to':recipient_list, 
      'subject':subject, 
      'body':body_html,
      'text_body':body_plaintext
      }
    url='https://api.smtp2go.com/v3/email/send'
    reponse = requests.post(url,headers=post_headers,json=payload)
    return response.ok

class SMSSender(MessageSender):
  def send(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    message="subject:"+subject+"\n"
    message+=body_plaintext

    # Replace with Twilio, Vonage, etc.
    log.info(f"[SMS] Sending to {to}: {message}")
    return True

class MessageDispatcher:
  def __init__(self):
    self.email_sender = EmailSender()
    self.sms_sender = SMSSender()
  def send_message(self, contact: str, contact_type: str, subject: str, body_plaintext: str, body_html: str):
    if contact_type is 'email':
      return self.email_sender.send(contact, subject, body_plaintext, body_html)
    else if contact_type is 'phone':
      return self.sms_sender.send(contact, subject, body_plaintext, body_html)

                  
  def send_message_detect_contact_type(self, contact: str, subject: str, body_plaintext: str, body_html: str):
    if re.match(r"^\+?\d{10,15}$", contact):
      return self.sms_sender.send(contact, subject, body_plaintext, body_html)
    elif re.match(r"[^@]+@[^@]+\.[^@]+", contact):
      return self.email_sender.send(contact, subject, body_plaintext, body_html)
    else:
      raise ValueError("Invalid contact format")
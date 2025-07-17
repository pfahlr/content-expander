from abc import ABC, abstractmethod
from fastapi import Cookie
import smtplib
import re 
import requests
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException
from utils.logging import log
from globals import WEBSITE_NAME, WEBSITE_PHONE, WEBSITE_EMAIL

class MessageSender(ABC):
  @abstractmethod
  def send(self, to: str, content: str) -> bool:
    pass

class EmailSender(MessageSender):
  def send(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    log.info('EmailSender::send()')
    self.smtp2go(to,subject,body_plaintext,body_html)
    log.info(f"[Email] Sending to {to}: subject:{subject} body:{body_plaintext}")
    return True

  def smtp2go(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    log.info('EmailSender::smtp2go()')
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
    response = requests.post(url,headers=post_headers,json=payload)
    log.info(response.ok)
    log.info(response.content)
    return response.ok

class SMSSender(MessageSender):
  def send(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    log.info('SMSSender::send()')
    message="subject:"+subject+"\n"
    message+=body_plaintext
    return self.eztexting_send_sms(to, subject, body_plaintext, body_html)
    #log.info(f"[SMS] Sending to {to}: {message}")
  
  def clicksend_send_sms(self, to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    log.info('SMSSender::clicksend_send_sms() to:'+to)
    
    configuration = clicksend_client.Configuration()
    configuration.username = 'contact@absurditiesmedia.com'  # Replace with your ClickSend username
    configuration.password = '8A390D5A-46F0-7A8B-663E-0BC6DA8A4EB9'  # Replace with your ClickSend API Key
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

    # Configure your message
    sms_message = SmsMessage(
      source="Content Expander",  # Replace with your desired source name or leave empty for default
      body=body_plaintext,  # Your message content
      to="+1"+to # Recipient's phone number in E.164 format (e.g., +1234567890)
    )

    #sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
    messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

    try:
      # Send an SMS message(s)
      log.info('SMSSendser::clicksend_send_sms()::try')
      log.info(sms_message)
      api_response = api_instance.sms_send_post(messages)
      log.info(api_response)
      return True
    except ApiException as e:
      log.info("log.info('SMSSendser::clicksend_send_sms()::Exception when calling SMSApi->sms_send_post: %s\n" % e)
      return False

  def eztexting_send_sms(self,to: str, subject: str, body_plaintext: str, body_html: str) -> bool:
    log.info('SMSSender::eztexting_send_sms() to:'+to)
    url = "https://a.eztexting.com/v1/messages"
    payload = {
        "message": body_plaintext,
        "companyName": WEBSITE_NAME,
        #"sendAt": "2025-07-15T01:49:02.463Z",
        #"mediaFileId": "string",
        #"mediaUrl": "string",
        #"messageTemplateId": "string",
        "fromNumber": WEBSITE_PHONE,
        "toNumbers": [to],
        #"groupIds": ["string"],
        "strictValidation": True
    }
    log.info("payload:")
    log.info(payload)
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "authorization": "Basic Y29udGFjdEBhYnN1cmRpdGllc21lZGlhLmNvbTpVP0VdM0Y8czo9VTlLLSVBV1U="
    }
    log.info("headers:")
    log.info(headers)
    response = requests.post(url, json=payload, headers=headers)
    log.info("response:")
    log.info(response.text)
    log.info("response.ok")
    log.info(response.ok)
    return response.ok

class MessageDispatcher:
  def __init__(self):
    self.email_sender = EmailSender()
    self.sms_sender = SMSSender()

  def send_message(self, contact: str, contact_type: str, subject: str, body_plaintext: str, body_html: str):
    log.info('MessageDispatcher::send_message():contact_type'+contact_type)
    if contact_type == "email":
      if not self.email_sender.send(contact, subject, body_plaintext, body_html): 
        raise Exception("email failed to send!")
    elif contact_type == "phone":
      if not self.sms_sender.send(contact, subject, body_plaintext, body_html):
        raise Exception("SMS failed to send!")
    else:
      raise ValueError("Invalid contact format")        
            
  def send_message_detect_contact_type(self, contact: str, subject: str, body_plaintext: str, body_html: str):
    log.info('MessageDispatcher::send_message_detect_contact_type():'+contact)
    if re.match(r"^\+?\d{10,15}$", contact):
      if not self.sms_sender.send(contact, subject, body_plaintext, body_html):
        raise Exception("email failed to send!")
    elif re.match(r"[^@]+@[^@]+\.[^@]+", contact):
      if not self.email_sender.send(contact, subject, body_plaintext, body_html):
        raise Exception("SMS failed to send!")
    else:
      raise ValueError("Invalid contact format")
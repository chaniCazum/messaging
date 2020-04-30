from app import GetByMessageId, AddMessage,DeleteMessage
from messageClass import Message
from unittest.mock import Mock
import pytest
import requests
import json


def test_GetByMessageId_status_code():
 response=requests.get('http://127.0.0.1:5000/GetMessage?message_id=0')
 assert response.status_code==200

def test_GetByMessageId():
 response=requests.get('http://127.0.0.1:5000/GetMessage?message_id=0')
 response_body = response.json()
 assert response_body['message_id']=='0'

def test_AddMessage():
 response=requests.post('http://127.0.0.1:5000/AddMessage?application_id=7888&session_id=33332&message_id=0&participants=jhgfdsfddh&content=dont forget')
 response_body=response.json()
 assert response_body=={
  "application_id": "7888",
  "content": "dont forget",
  "message_id": "0",
  "participants": "jhgfdsfddh",
  "session_id": "33332"
}

def test_AddById_invalid_message_id():
 response=requests.post('http://127.0.0.1:5000/AddMessage?application_id=7888&session_id=44556&message_id=0&participants=jhgfdsfddh&content=dont forget')
 assert response.text=='message_id is uniqe and already in use' 

 
def test_AddMessage_invalid_session_id():
 response=requests.post('http://127.0.0.1:5000/AddMessage?application_id=948254&session_id=33332&message_id=7774586&participants=jhgfdsfddh&content=dont forget')
 assert response.text=='session_id is uniqe and already in use' 


def test_DeleteMessage_application_id():
 response=requests.delete('http://127.0.0.1:5000/DeleteMessage?application_id=777896')
 response_body=response.json()
 success=True
 for message in response_body:
  if message['application_id']=='777896':
    success=False
 assert success==True
   
def test_DeleteMessage_message_id():
 response=requests.delete('http://127.0.0.1:5000/DeleteMessage?message_id=0')
 response_body=response.json()
 success=True
 for message in response_body:
  if message['message_id']=='0':
    success=False
 assert success==True
   



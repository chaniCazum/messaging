from flask import Flask, jsonify, request,json
import requests
from messageClass import Message

app = Flask(__name__)

messages=[]


@app.route("/GetMessage", methods=['GET'])
def GetByMessageId():
    if 'message_id' in request.args:
     id = request.args['message_id']
    else:
      return "Error: No message id field provided. Please specify an id."
    for message in messages:     
     if message.message_id == id:
        return json.dumps(message.__dict__)
    return jsonify({})

@app.route("/AddMessage", methods=['post'])
def AddMessage(): 
    if 'message_id' in request.args:
     temp_message_id=request.args['message_id'] 
     for message in messages:
        if message.message_id==temp_message_id : 
         return "message_id is uniqe and already in use" 
    else:
     temp_message_id=None
    if 'session_id' in request.args:
     temp_session_id=request.args['session_id'] 
     for message in messages:
        if message.session_id==temp_session_id : 
         return "session_id is uniqe and already in use" 
    else:
     temp_session_id=None
    if 'application_id' in request.args:
     temp_application_id=request.args['application_id']
    else:
     temp_application_id=None
    if 'participants' in request.args:
     temp_participants=request.args['participants']
    else:
     temp_participants=None
    if 'content' in request.args:
     temp_content=request.args['content']
    else:
     temp_content=None   
    create_row_data=Message(str(temp_application_id),str(temp_session_id),str(temp_message_id),str(temp_content),str(temp_participants))
    messages.append(create_row_data)
    for message in messages:
     if message.message_id==str(temp_message_id):
      return json.dumps(message.__dict__)

@app.route("/DeleteMessage", methods=['delete'])
def DeleteMessage():
 if 'message_id' in request.args:
    id = request.args['message_id']
    for message in messages:     
     if message.message_id == id:
      messages.remove(message)
 elif 'application_id' in request.args:
    id = request.args['application_id']
    for message in messages:     
      if message.application_id == id:
        messages.remove(message)
 elif 'session_id' in request.args:
    id = request.args['session_id']
    for message in messages:     
     if message.session_id == id:
      messages.remove(message)
 else:       
    return "Error: No id field provided. Please specify an id." 
 return json.dumps([ob.__dict__ for ob in messages])

  
if __name__=="__main__":
    app.run(debug=True)
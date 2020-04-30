Author:Chani Cazum

Email storage:
This is a program that deals with emails.
The program includes receiving and storing email data in the database,
retrieving email data from the database and displaying it to the user,
and deleting emails from the database.

The program's functions are:
* GetById: The function accept message id and pulls out the message data and displays it to the user.
* AddNewMessage: The function receives new emails data including the following parameters: application_id, session_id, message_id, content, and list of participants and stores them in the database If you omit one of the function parameters, the function will set in the missing parameter value:'None' and returns the email that was added
* DeleteById: the function recived one of the following parameters and delete emails according to them:
If you send a applicationId parameter the function will remove all messages with the application id that was sent.
If you send a sessionId parameter the function will remove all messages with the session id that was sent.
If you send a messageId parameter the function will remove the message with the message id that was sent.
And returns the rest of the list left after deleting the requested rows.

In order to execute the python program you will have to install python by downloading the program.
you can confirm your installation by writing in the command line: 'python3 –version' and that will give you the version you are using.
in order to run the program that implements server using “flask” microframework, you will have to install flask.
First open the folder in vscode by clicking open folder and choosing the project folder.
open a new terminal and write the following sentence in order install the virtualenv:'pip3 install virtualenv'
then activate it by writing:'env/Scripts/activate'
after it install flask by writing: pip install flask
and then: APP_FLASK=app.py (the project file_name.py)
and finally you can run the program by writing: 'flask run' or you can just click the button in the top right corner. 

now the program is runing on the locaholhost printed in terminal: 
in order to implement the program you'll have to open postman start by downloading it from the internet.
After you download postman and signed up click the button 'new' on the top left corner and create a new request.

Now you can execute the program starting with POST method:
Chosse the method post and copy the address from the terminal to the search line http://127.0.0.1:5000 (this adress is usually the default) add '/AddMessage' (wich is the name of the function)
Now you can insert your new message by insert into the key column the key you want to add you will have to add the following parameters: application_id, session_id, message_id, content, and list of participants,
In the value column, enter the value you want to enter according to the keys you entered in the key column.
If you miss one of the parameters the function will set in the missing parameter value:'None',
click the send buttom next to the search line, now the function added your new message, pull it from the data and show your message in the body on the right side.

After you insert data now you can pull it, so we'll use the GET method.
Add anothe file by clicking the plus button above the search line, choose the get method and copy the address from the terminal to the search line add '/GetMessage' (the name of the function)
Now you can insert the message_id of the message you want to pull from the data, so in the params window insert into the key column 'message_id' and in the value column insert the value of the message you want to pull, click the send buttom next to the search line, then you'll see the data of the wanted message in the body on the right side.

Now we'll use the Delete function to delete messages
Again add anothe file by clicking the plus button above the search line, choose the delete method and copy the address from the terminal to the search line add '/DeleteMessage' (the name of the function),
There are three options for deleting data: you can delete by message_Id– remove single message with the message Id,
you can delete by session_Id – remove all messages with the session Id, or you can delete by message_Id– remove single message with the message Id. so insert to the columns the key and value you have chosen to use for deletion. click the send buttom next to the search line, then you'll see in the body the new messages data without the messages that meet your requirement cause the function already remove them from the list.
  
    
    













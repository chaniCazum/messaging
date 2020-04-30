Test plan:
Writing a test in order to test the program's performance.
In order to test the program I sent a request to the program and saved the data the program returned within a response variable.
Before you execute the test plan that implemented using “pytest” framework you'll have to install pytest.
Open the command line and print: pip3 install -U pytest
execute the app.py program in the terminal by print: flask run,
then open a new terminal at the same time, activate env in this terminal just as you did with the app.py terminal by print: env/Scripts/env, and run the test program writing: pytest, you'll see in the terminal how many tests have passed.

The first test function is - def test_GetById_status_code():
The method checks the status code that should be 200, so it sends to the GetMessage function message id and checks that the status code is really 200 to make sure the program is being implemented correctly.

The function -def test_GetById():
The method sends the GetMessage method a message id and making sure that the programs really returns the wanted message, so it compares what was sent and the message_id attribute of what was received, if the test pass it means that the program really does return what it needs.

The function - def test_AddById_invalid_message_id():
The method sends the AddMessage method details of a new message to add with message_id that already in used and making sure that the programs really keeps the message_id unique, if the method works correctly it will find a message that already bears the given message_id and returns the message: 'message_id is uniqe and already in use'

The function- def test_AddNewMessage_invalid_session_id():
The method is doing the same as the previous function but here it checks that the program keeps the session_id unique.

The function- def test_AddNewMessage():
The method sends the AddMessage method details of a new message to add and making sure that the program really adding the new message to the list, the function returns the sent object by pulling it again from the data, 
in our test we compares the returned object with the sent object.

The function- def test_DeleteById_application_id():
The method sends the DeleteById method a application_id and making sure that the programs really delete the wanted message, the delete function returns the new messages list without the deleted massages then it goes through the entire list of messages and checks to see if there really are any messages with the application_id that sent. 

The function- def test_DeleteById_message_id():
The method is doing the same as the previous function but here it checks that the program delete wanted message with the sent message_id
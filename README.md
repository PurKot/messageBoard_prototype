# Message board application prototype for AggieFit
### Developed by Purnima Kotharu

#### This prototype has been developed to illustrate the working of message board application with both MongoDB and Redis databases 

**_Pre-Requisites:_**

1. Ensure that the local machine has MongoDB installed as a service. 
2. Ensure Redis is installed on the same machine as a service. ( If Databases are not installed on the same machine modify the constants.py file to point to the correct DB servers. 
3. Optional: Modify the Database name in costants.py file if desired. 
4. Ensure python v3.7.0 is installed on the local machine 
5. Extract all the python script files to a folder on the local machine. 
6. If using windows: Run the command at command prompt

              python -m pip install pymongo
7. If running the code on Windows machine, Redis needs Windows subsystem for Linux to be installed. Install Ubuntu subsystem on windows and run the command on Ubuntu shell. 

              $sudo pip install redis
8. For linux machine run:

              $ pip install pymongo 
              $ pip install redis
              
**_Execute the application:_**


1. From the application folder to start the application, run the command

              $ python main.py
              
2. This will start the application and user can see '>' prompt. 
3. Type help to see the list of commands available. 
4. Type `help <command>` to see the syntax and description of a command
5. List of commands implemented in the application are:

             select <boardname> ---- will select a message board topic to read/write/listen messages
             write <message>    ---- will write the message to the previously selected message board
             read               ---- will read all the messages from the selected message board topic
             listen             ---- will subscribe the user to the selected message board and will immediately show any new messages added to the selected message board topic
             stop               ---- will unscribe the user from receiving updates on the selected message board topic
             showboards         ---- will show all the existing topics on message board application. 
             quit               ---- will exit out of the application. 
 
         


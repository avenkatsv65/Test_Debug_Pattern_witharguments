

--debugging a pre-existing file..

Directly ran 'Run and Debug'.. On the choose debugger, option...
debug with arguments--option selected
on prompt, passed the parameter-- here it is value 3
Error: module not found

on the terminal, check the version of the python u r running( from whichever env you are running. it could be base env or virtual env and select that environment in the 'select python interpreter' option. Ideally, its recommended to install packages in a 'virtualenvironment' to avoid conflicts.
Opened Command paletter, selected, python interpreter.
System prompted to create a launch.json(infact it created automatically)
I added the "args" :["3] parameters in the launch.json
Started Run and debug.. everything worked fine..

from hello_world import world

world(3)

## look after we runned these, these will be printed in the terminal:
##Hello World         hello bro          3

## a new folder will be made- __pycache__- and in that folder, there will be a file called hello_world.cpython-310.pyc. This is a compiled version of the hello_world.py file. When we run the world function from the hello_world module, Python compiles the hello_world.py file into bytecode and saves it as a .pyc file in the __pycache__ folder. This allows for faster execution of the code in subsequent runs, as Python can directly execute the bytecode without needing to recompile the source code.

##after this we learned about python in shell, as it can't be saved , it will not be showned.
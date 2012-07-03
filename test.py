from sys import argv

def serve():
    """
    serves the application
    ----------------------
    """
    print "Welcome to Test!"

options = ['serve']
if argv[1] in options:
    eval(argv[1])()
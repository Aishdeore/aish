from flask import Flask
application = FlaSK(__NAME__)

@application.route('/')
def hello_world():
    return "Hello World in Python, Run as a POD in OpenShift\r\n", 200,
{ 'Content-Type': 'text/plain' }

if __name__ == '__main__':
    application.run(debug = True)

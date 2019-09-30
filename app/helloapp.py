#!/usr/bin/python
from flask import Flask,render_template,request
import socket,random,os,time,argparse

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}
SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')

# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])

# default url just displays a hello from the host we are running on in the color we have
@app.route("/")
def main():
    # return 'Hello'
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[COLOR])

# Inputs some value into a log file and display a text box with the value in the color we have
# url to call will be: input?data=somevalue
@app.route('/input')
def appinput():
    # Retrieve the data
    inputdata = request.args.get('data')

    # If input is not what we expect do a normal hello
    if inputdata is None:
       print("Error | Input format is: /input?data=somevalue")
       return render_template('hello.html', name=socket.gethostname(), color=color_codes[COLOR])

    # Set the hostname and current date
    host = socket.gethostname()
    date = time.strftime("%H:%M:%S %d-%m-%Y")

    # Convert the date output to a string
    now = str(date)

    # Open the file named date in append mode
    # Append the output of hostname and time
    f = open("log/datalog.out", "a")
    f.write(host + ": " + now + " | " + COLOR + " | " + inputdata + "\n")
    f.close()

    # Render with the data page
    return render_template('data.html', name=host, color=color_codes[COLOR], contents=inputdata)

if __name__ == "__main__":
    print("Ready to say hello...")

    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()

    # Determine the color for the page
    if args.color:
        print("Color from command line argument [" + args.color + "]\n")
        COLOR = args.color
        if COLOR_FROM_ENV:
            print("A color was set through environment variable [" + COLOR_FROM_ENV + "]. However, color from command line argument takes precendence.\n")
    elif COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable [" + COLOR_FROM_ENV + "]\n")
        COLOR = COLOR_FROM_ENV
    else:
        print("No command line or environment variable. Picking a Random Color [" + COLOR +"]\n")

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("Color not supported. Received [" + COLOR + "] expected one of " + SUPPORTED_COLORS)
        exit(1)
    
    # Create a log directory if it is not there
    if not os.path.isdir("log"):
        os.mkdir("log")

    # Run the Flask Application
    app.run(host="0.0.0.0", port=8080)


from flask import Flask, render_template
app = Flask(__name__)

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import calendar
from datetime import date

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


instance = dht11.DHT11(pin=17)
lastResult = instance.read()
lastResultTemp = lastResult.temperature

# read data using pin 14
@app.route("/")
def hello():
    result = instance.read()
    return("Temperature: %d C" % result.temperature)
    time.sleep(1)
    
@app.route("/temp")
def temperature():
    weekday = calendar.day_name[date.today().weekday()]
    monthdate = date.today();
    result = instance.read()
    test = result.temperature

    if test < 25:
#	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(27,GPIO.OUT)
	GPIO.output(27,1)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22,0)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,0)
	print "It's Cold"
    
    if test == 25:
#	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(27,GPIO.OUT)
	GPIO.output(27,0)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22,1)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,0)
	print "none"

    if test > 25:
#	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(27,GPIO.OUT)
	GPIO.output(27,0)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22,0)
	GPIO.setup(23,GPIO.OUT)
	GPIO.output(23,1)
	print "It's Hot"
    return render_template("index.html",temp=test, weekday=weekday, monthdate=monthdate)

@app.route("/index")
def test():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
	



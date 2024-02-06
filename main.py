from flask import Flask, render_template, redirect, url_for, flash, jsonify
from datetime import datetime, timedelta, time
import pandas as pd
from pytz import timezone
from flask_socketio import SocketIO, emit
app = Flask(__name__)
import os

socketio = SocketIO(app, debug=True)

data = pd.read_csv("data.csv")

def in_between(now, start, end):
  return start <= now <= end

@socketio.on("getdata")
def getdata():
  timeinzone = timezone("US/Eastern")
  day = datetime.now(timeinzone).strftime("%A")
  timenow = datetime.now(timeinzone).time()
  righttime = None
  if day == "Monday":
    for i in data[data.Day == "Monday"].Time.values.tolist():
        split = str(i).split("-")
        hour1 = int(split[0].split(":")[0])
        minute1 = int(split[0].split(":")[1])
        hour2 = int(split[1].split(":")[0])
        minute2 = int(split[1].split(":")[1])
        if hour1 < 8:
          hour1 += 12
        if hour2 < 8:
          hour2 += 12
        if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
          righttime = i
          break
  if day == "Tuesday":
    for i in data[data.Day == "Tuesday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        break
  if day == "Wednesday":
    for i in data[data.Day == "Wednesday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        break
  if day == "Thursday":
    for i in data[data.Day == "Thursday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        print(righttime)
        break
  if day == "Friday":
    for i in data[data.Day == "Friday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        break
  print(datetime.now(timeinzone).time())
  emit("retrieve_data", {"day": day, "righttime": righttime, "time": str(datetime.now(timeinzone).time())}, broadcast=True)

@app.route('/')
def home():
  timeinzone = timezone("US/Eastern")
  day = datetime.now(timeinzone).strftime("%A")
  righttime = None
  timenow = datetime.now(timeinzone).time()
  if day == "Monday":
    for i in data[data.Day == "Monday"].Time.values.tolist():
        split = str(i).split("-")
        hour1 = int(split[0].split(":")[0])
        minute1 = int(split[0].split(":")[1])
        hour2 = int(split[1].split(":")[0])
        minute2 = int(split[1].split(":")[1])
        if hour1 < 8:
          hour1 += 12
        if hour2 < 8:
          hour2 += 12
        if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
          righttime = i
          break
  if day == "Tuesday":
    for i in data[data.Day == "Tuesday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        break
  if day == "Wednesday":
    for i in data[data.Day == "Wednesday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        break
  if day == "Thursday":
    for i in data[data.Day == "Thursday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        print(righttime)
        break
  if day == "Friday":
    for i in data[data.Day == "Friday"].Time.values.tolist():
      split = str(i).split("-")
      hour1 = int(split[0].split(":")[0])
      minute1 = int(split[0].split(":")[1])
      hour2 = int(split[1].split(":")[0])
      minute2 = int(split[1].split(":")[1])
      if hour1 < 8:
        hour1 += 12
      if hour2 < 8:
        hour2 += 12
      if in_between(timenow, time(hour1, minute1), time(hour2, minute2)):
        righttime = i
        break
  return render_template("index.html", data=data, length=len(data[data.Day == "Monday"].Class.value_counts().index.tolist()), day=day, timezone=timeinzone, time=datetime.now(timeinzone).strftime("%I:%M"), righttime=righttime)


@app.route("/gettime")
def gettime():
  timeinzone = timezone("US/Eastern")
  time = datetime.now(timeinzone).strftime("%A, %B %d, %Y, %I:%M:%S %p")
  return jsonify({"Content": time})
if __name__ == "__main__":
  app.jinja_env.auto_reload = True
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  socketio.run(app, port=os.getenv("PORT", default=5000))
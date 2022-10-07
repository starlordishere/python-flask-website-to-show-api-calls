from flask import Flask,render_template
from get_data import api_data

app = Flask('app')

@app.route('/')
def iss_data():
  #Call apiconnect function to get all data
  listofdatas=api_data()
  #Pass the data and render the index page
  return render_template("index.html",listofdatas=listofdatas)
  
app.run(host='0.0.0.0', port=8080)

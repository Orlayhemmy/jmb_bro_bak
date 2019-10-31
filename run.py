from flask import Flask, jsonify
from dbconnect import fetch_data

app = Flask(__name__)

@app.route('/states')
def fetch_states():
  sql_statement = 'select * from states join cities on state_id=stateid'
  states = jsonify(fetch_data(sql_statement))
  return states

@app.route('/cities')
def fetch_cities():
  sql_statement = 'select * from cities where stateid ='
  cities = jsonify(fetch_data(sql_statement))
  return cities

@app.route('/centers')
def fetch_centers():
  sql_statement = 'select * from centers where cityid ='
  centers = jsonify(fetch_data(sql_statement))
  return centers

if __name__ == '__main__':
  app.run()

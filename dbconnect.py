import pymysql
import os

def fetch_data(sql_statement):
  # Open database connection
  print(os.getenv('HOST'))
  db = pymysql.connect("localhost","root","","BROCHURE" )

  # prepare a cursor object using cursor() method
  cursor = db.cursor(pymysql.cursors.DictCursor)

  try:
    # Execute the SQL command
    cursor.execute(sql_statement)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    return results
  except:
    print ("Error: unable to fetch data")

  # disconnect from server
  db.close()
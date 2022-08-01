
from ftplib import all_errors
import requests, json, datetime

# This function is for all the data on the senate
def fetch_data_senator():
  response = requests.get("https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json")
  
  if response.status_code != 200:
    print("request failed.")
    return False
  
  data = response.json()
  data.sort(key = lambda x: datetime.datetime.strptime(x['disclosure_date'], '%m/%d/%Y'), reverse=True)
  return data

# This function is for all the data on the house of representatives
def fetch_data_representatives():
  response = requests.get("https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json")
  
  if response.status_code != 200:
    print("request failed.")
    return False
  
  data = response.json()
  data.sort(key = lambda x: datetime.datetime.strptime(x['disclosure_date'], '%m/%d/%Y'), reverse=True)
  return data
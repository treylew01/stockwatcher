import datetime
from datarequest import fetch_data_representatives, fetch_data_senator

# returns last_years data based on todays time
def last_year():
  todays_date = datetime.datetime.now()
  subtract_year = todays_date - datetime.timedelta(days=365)
  return subtract_year

# gets all the entries in the last year 
def year_entry(data, cutoff):
  new_dicts = []
  for entry in data:
    if datetime.datetime.strptime(entry['disclosure_date'], '%m/%d/%Y') > cutoff:
      new_dicts.append(entry)
    else:
      break
  return new_dicts

# gets all the people in the dataset - it is conditional on representative or senate
def get_people(data_set, position):
  people_set = set()
  for trade in data_set:
    people_set.add(trade[position])
  return people_set

# returns a set with numbers for user input
def set_with_numbers(the_set):
  counter = 0
  for item in the_set:
    print(f"{counter}: {item}")
    counter += 1

# senator or representative
def main():
  position = input('senator or representative: ')
  current_year_data = year_entry(eval("fetch_data_"+position+"()"), last_year())
  all_people = get_people(current_year_data, position)
  set_with_numbers(all_people)
  set_of_people = input("Enter Corresponding Number: ")
  print(set_of_people)

main()
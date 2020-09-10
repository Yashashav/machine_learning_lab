"""
╔╦╗┌─┐┌─┐┬ ┬┬┌┐┌┌─┐  ╦  ┌─┐┌─┐┬─┐┌┐┌┬┌┐┌┌─┐
║║║├─┤│  ├─┤││││├┤   ║  ├┤ ├─┤├┬┘││││││││ ┬
╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘  ╩═╝└─┘┴ ┴┴└─┘└┘┴┘└┘└─┘

Faculty: Prof. Abhilash G
Student: yashashav_dk
Topic: Find S Algorithm Implementation
"""

import csv

def check_failure_and_first_postive(parsed_data, specific_hyp):
  positive_count = 0
  for every_row in parsed_data:
    concept = every_row[-1].lower()
    if concept == "yes":
      specific_hyp = every_row
      positive_count += 1
      break
  if positive_count == 0:
    return (False, specific_hyp)
  return (True, specific_hyp)

def find_specific(parsed_data):

  # Using UTF-8 to represent "phi" 
  phi = u"\u03D5"

  #Starting with most specific hypothesis
  specific_hyp = [phi for attribute in range(len(parsed_data[1]) - 1)]

  # Checking for zero positives and also trying to find the first positive
  does_algo_run, specific_hyp = check_failure_and_first_postive(parsed_data, specific_hyp)
  
  # print(does_algo_run)
  # print(specific_hyp)

  # If no positive concept found then return to "main"
  if(does_algo_run == False):
    print("No positive concept found. Algorithm fails.")
    return
  
  # If any postive data found then continue
  for every_row in parsed_data:
    concept = every_row[-1].lower()

    # Removing concept cell
    every_row.pop(-1)

    if concept == "yes":
      for index in range(len(every_row)):
        if every_row[index] == specific_hyp[index]:
          continue
        else:
          specific_hyp[index] = "?"
        
  print("Final Hypothesis: h = ",end="")
  print(specific_hyp)


def read_data(file_name):
  with open(file_name, "r") as csv_file:
    csv_data = csv.reader(csv_file)
    parsed_list = []
    for line in csv_data:
      parsed_list.append(line)
      # print(line)
  return parsed_list

if __name__ == "__main__":
  file_name = "data.csv"
  parsed_data = read_data(file_name)
  find_specific(parsed_data)

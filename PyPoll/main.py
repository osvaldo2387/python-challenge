import os
import csv

#Define the variables
original_data="Original Data"
output_data="Output Data"
csv_file="PyPoll.csv"
new_file="Poll_results.txt"
# Define path of csv file
path_csv_file=os.path.join(original_data,csv_file)

#Define new output file
new_file ="Output Data/Poll_results.txt"

# Declaring the Variables 
total_votes = 0
Candidate = {}
Candidate_percent = {}
winner_count = 0
winner = ""

with open(path_csv_file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
    for row in csvreader:
        # The total number of votes cast
        total_votes += 1
        
        #A complete list of candidates who received votes
        if row[2] in Candidate.keys():
            Candidate[row[2]] += 1
        else:
            Candidate[row[2]] = 1

        # The percentage of votes each candidate won
        # make a candidate dictionary
        for key, value in Candidate.items():
            Candidate_percent[key] = round((value/total_votes) * 100, 1)

        # The winner of the election based on popular vote
        for key in Candidate.keys():
            if Candidate[key] > winner_count:
                winner = key
                winner_count = Candidate[key]


# Print 
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in Candidate.items():
    print(key + ": " + str(Candidate_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")


# writing the new file
with open(new_file, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in Candidate.items():
        file.write(key + ": " + str(Candidate_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")
import os
import csv

totalvotes = 0
candidatelist = []
candidatevotes = {}
winner = ""
winner_votes = 0

#Change directory to C:\Users\czope\OneDrive\Desktop\Bootcamp\Module3\Starter_Code>
csv_file_path = 'PyPoll\Resources\\election_data.csv'

#Creating output text file path
output_file_path = 'PyPoll\\analysis\\analysis.txt'
with open(output_file_path, "w") as output_file:
     
    with open(csv_file_path, 'r', encoding='UTF-8') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)

        #Skip the header row
        next(csvreader)

        # Iterate over each row in the CSV file
        for row in csvreader:
            #CALCULATE TOTAL NUMBER OF VOTES----------------------
            totalvotes = totalvotes + 1

            #CALCULATE COMPLETE LIST OF CANDIDATES
            #Initialize candidate column
            candidate = row[2]
            #If the candidate is not already in list, append candidate 
            if candidate not in candidatelist:
                candidatelist.append(candidate)
            
            #CALCULATE THE PERCENTAGE OF VOTES EACH CANDIDATE WON-------
            #Create a dictionary for candidate and candidate votes
            #For every candidate found in the dictionary increment their votes by 1
            if candidate in candidatevotes:
                candidatevotes[candidate] = candidatevotes[candidate] + 1
            else:
            #If the candidate is not found in the dictionary begin their votes with 1
                candidatevotes[candidate] = 1  

    print("Election Results")

    print("----------------------------")
    print(f"Total Votes: {totalvotes}")
    print("----------------------------")

    #Create a loop for every candidate in the list to print their results
    for candidate in candidatelist:
            #Grab the votes from every unique candidate
            votes = candidatevotes[candidate]
            #Calculate the percentage for every unique candidate
            percentage = (votes / totalvotes) * 100
            #Print the candidate name, percentage of votes, and total votes
            print(f"{candidate}: {percentage:.3f}% ({votes}) ")

            #Calculate the winner
            #If the current candidate votes is greater than the winner, save candidate as new winner
            if votes > winner_votes:
                winner_votes = votes
                winner = candidate

    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")


    #Printing results to analysis text file
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {totalvotes}\n")
    output_file.write("----------------------------\n")
    #Create a loop for every candidate in the list to print their results
    for candidate in candidatelist:
            #Grab the votes from every unique candidate
            votes = candidatevotes[candidate]
            #Calculate the percentage for every unique candidate
            percentage = (votes / totalvotes) * 100
            #Print the candidate name, percentage of votes, and total votes
            output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

            #Calculate the winner
            #If the current candidate votes is greater than the winner, save candidate as new winner
            if votes > winner_votes:
                winner_votes = votes
                winner = candidate   
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")

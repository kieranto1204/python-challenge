# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("python-challenge", "PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("python-challenge", "PyPoll","analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts

list_of_candidate= []
votes_won = {}


# Winning Candidate and Winning Count Tracker

winner_name = ""
winning_votes = 0
winning_percent = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)

        print(". ", end="")

        # Increment the total vote count for each row

        total_votes = total_votes + 1

        # Get the candidate's name from the row

        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them

        if candidate_name not in list_of_candidate:

            list_of_candidate.append(candidate_name)

            votes_won[str(candidate_name)] = 0

        # Add a vote to the candidate's count
    
        votes_won[candidate_name] = (int(votes_won[candidate_name]) + 1)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)

    output = ("Election Results" + "\n" + "-------------------------"+ "\n" + "Total Votes: " + str(total_votes) + "\n" + "-------------------------" + "\n")

    print (output)

    # Write the total vote count to the text file

    txt_file.write(output)

    # Loop through the candidates to determine vote percentages and identify the winner

    for candidate_name in votes_won:

        # Get the vote count and calculate the percentage
        total_won_votes = votes_won[candidate_name]

        percent_of_votes = (total_won_votes/total_votes)*100

        percent_of_votes = format(percent_of_votes, ".3f")

        results = (candidate_name + ": " + str(percent_of_votes) + "%" + " (" + str(total_won_votes) + ")" + "\n" + "\n")

        # Update the winning candidate if this one has more votes

        if (int(total_won_votes) > int(winning_votes)) and (float(percent_of_votes) > float(winning_percent)):
            winning_votes = total_won_votes
            winning_percent = percent_of_votes
            winner_name = candidate_name


        # Print and save each candidate's vote count and percentage

        print(results)

        txt_file.write(results)


    # Generate and print the winning candidate summary

    summary = ("Winner: " + winner_name + "\n" + "-------------------------")

    print(summary)


    # Save the winning candidate summary to the text file

    txt_file.write(summary)
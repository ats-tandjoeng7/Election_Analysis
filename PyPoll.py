# Add our dependencies.
#import random
#import sys, colorsys
import os
import csv
import datetime as dt
# Use getcwd to prevent path from being undiscovered
mypath = os.getcwd()
# variable to load a file from a path.
file_to_load = os.path.join(mypath, "Resources", "election_results.csv")
# variable to save the file to a path.
file_to_save = os.path.join(mypath, "analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
# Create a county list and county votes dictionary.
county_list = []
county_votes = {}
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load, 'r', encoding='utf-8') as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
            # Add the existing county to the list of counties.
            county_list.append(county_name)
            # Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, 'w', encoding='utf-8') as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"{'-'*25}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{'-'*25}\n\n")
#        f"County Votes: \n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
#        print(f'{candidate_name} received **{vote_percentage:.1f}%** of the vote and **{votes:,}** number of votes.')
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"{'-'*25}\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{'-'*25}\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
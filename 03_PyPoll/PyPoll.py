# Add our dependencies.
#import random
#import sys, colorsys
import os
import csv
import datetime as dt
# Use getcwd to prevent path from being undiscovered
mypath = os.getcwd()
# Add a variable to load a file from a path.
file_to_load = os.path.join(mypath, "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join(mypath, "analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.


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

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

#print(f'{candidate_votes} \n {county_votes}')
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
#    print(f'{candidate_name}: received {votes} votes or {vote_percentage:.1f}% of the vote.')

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Print the winning candidate (to terminal)
winning_candidate_summary = (
    f"{'-'*25}\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"{'-'*25}\n")
print(winning_candidate_summary)

'''
# Save the results to our text file.
with open(file_to_save, 'w', encoding='utf-8') as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"{'-'*25}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{'-'*25}\n\n"
        f"County Votes: {county_votes[county_name]}\n")
    print(election_results, end="")

    txt_file.write(election_results)
#    txt_file.write(election_results+'-'*25+"\nArapahoe\nDenver\nJefferson")

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

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
'''

# Coded for UCB-VIRT-DATA-PT-08-2022-U-B by: Parto Tandjoeng
# Add our dependencies.
import sys
import os
import csv
from collections import defaultdict
# use getcwd or "\\" on Windows to prevent path from being undiscovered
# variable to load a file from a path.
file_to_load = os.path.join("./Resources", "election_results.csv")
# variable to save a file to a path.
file_to_save = os.path.join("./analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}
# County list and county votes dictionary.
county_options = []
county_votes = {}
candidate_options_bycounty = []
candidate_votes_bycounty = {}
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Track the top county, county voter turnout and percentage
top_county = ""
top_count = 0
top_percentage = 0
# analyze candidate's vote breakdown by county
user_input = str(input("Key in 1. Arapahoe, 2: Denver, 3: Jefferson or simply press <Enter> to continue: "))
if (user_input == "1"): bycounty = "Arapahoe"
elif (user_input == "2"): bycounty = "Denver"
elif (user_input == "3"): bycounty = "Jefferson"
else: bycounty=0

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
        if county_name not in county_options:
            # Add the existing county to the list of counties.
            county_options.append(county_name)
            # Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
        # analyze candidate's vote breakdown by county
        if bycounty != 0:
            if county_name == bycounty:
                if candidate_name not in candidate_options_bycounty:
                    # Add the candidate name to the candidate list.
                    candidate_options_bycounty.append(candidate_name)
                    # And begin tracking that candidate's voter count.
                    candidate_votes_bycounty[candidate_name] = 0
                candidate_votes_bycounty[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, 'w', encoding='utf-8') as txt_file:
    # Print the final vote count (to terminal and file)
    election_results = (
        f"\nElection Results\n"
        f"{'-'*25}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{'-'*25}\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
    # loop to get the county from the county dictionary.
    for county_name in county_votes:
        # Retrieve the county vote count.
        votes = county_votes[county_name]
        # Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each county, their voter count, and percentage to the terminal.
        county_stats = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_stats)
        # Save the county votes to a text file.
        txt_file.write(county_stats)
        # Write an if statement to determine the top county and get its vote count.
        if (votes > top_count) and (vote_percentage > top_percentage):
            # If true then set top_count = votes and top_percentage = vote_percentage.
            top_count = votes
            top_percentage = vote_percentage
            # Set the top_county equal to the county's name.
            top_county = county_name
    # Print the county with the largest turnout to the terminal.
    top_county_summary = (
        f"\n{'-'*25}\n"
        f"Largest County Turnout: {top_county}\n"
        f"{'-'*25}\n\n")
    print(top_county_summary, end="")
    # Save the county with the largest turnout to a text file.
    txt_file.write(top_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        if bycounty != 0:
            votes_bycounty = candidate_votes_bycounty[candidate_name]
            vote_percentage_bycounty = float(votes_bycounty) / float(county_votes.get(bycounty)) * 100
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

    if bycounty != 0:
        # candidate's vote breakdown and popularity by county
        print(f"Candidate Votes in {bycounty} County\n{'-'*25}\n")
        for candidate_name in candidate_votes:
            # Retrieve vote count of a candidate.
            votes_bycounty = candidate_votes_bycounty[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage_bycounty = float(votes_bycounty) / float(county_votes.get(bycounty)) * 100
            print(f"{candidate_name}: {vote_percentage_bycounty:.1f}% ({votes_bycounty:,})\n")
        print(f"{'-'*25}\n")
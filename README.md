# Election_Analysis
This project exposed us to the power of Python and how we can leverage many of its useful packages, libraries, modules, and functions for performing efficient data analytics and data visualization.

## Table of Contents
- [Overview of Project](#overview-of-project)
  - [Resources](#resources)
  - [Challenge Overview](#challenge-overview)
- [Election Audit Results](#election-audit-results)
- [Challenge Summary](#challenge-summary)
- [Future Work](#future-work)
- [References](#references)

## Overview of Project
Module 3 assignment triggered some rigorous exercises for understanding Python coding concepts and how we apply some of its module, functions, and data structures to perform analysis and visualization of the election data more efficiently. We were required to supply some data analytics to fulfill the audit requirements, including the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout. Election data were from a Colorado Board of Elections employee, who has further requested additional Election-Audit Results to complete the election audit of a recent local congressional election as below.
- Provide total votes that were cast in this congressional election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Identify the county that had the largest number of votes.
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Identify the candidate who won the election, and what their vote count and their percentage of the total votes.
- Election-Audit Summary, in which we will provide a business proposal to the election commission on how this script can be used with some modifications for any election and two examples.

### Resources
- Data Source: election_results.csv
- Source Code: PyPoll_Challenge.py (PyPoll.py is a subset)
- Output File: election_results.txt
- Software: [Python 3.9.12](https://docs.python.org/release/3.9.12/), [Visual Studio Code 1.71.1](https://code.visualstudio.com/updates/v1_71)

### Challenge Overview
Outline of our deliverables and a written report:
- ☑️ Deliverable 1: The Election Results Printed to the Command Line
- ☑️ Deliverable 2: The Election Results Saved to a Text File
- ☑️ Deliverable 3: A written Analysis of the Election Audit (this ["README.md"](./README.md))

All deliverables in Module 3 challenge are committed in this GitHub repo as outlined below.  
main branch  
|&rarr; [./README.md](./README.md)  
|&rarr; [./PyPoll.py](./PyPoll.py)  
|&rarr; [./PyPoll_Challenge.py](./PyPoll_Challenge.py)  
|&rarr; ./Resources/  
  &emsp; |&rarr; [./Resources/election_results.csv](./Resources/election_results.csv)  
|&rarr; ./analysis/  
  &emsp; |&rarr; [./analysis/election_analysis.txt](./analysis/election_analysis.txt)  

## Election-Audit Results
Our preliminary analysis of the election show that:
- There were **369,711** total votes cast in the election.
- The candidates were:
  - Candidate 1: Charles Casper Stockham
  - Candidate 2: Diana DeGette
  - Candidate 3: Raymon Anthony Doane
- The candidate results sorted in descending order were:  
🥇 Diana DeGette received **73.8%** of the vote and **272,892** number of votes.  
🥈 Charles Casper Stockham received **23.0%** of the vote and **85,213** number of votes.  
🥉 Raymon Anthony Doane received **3.1%** of the vote and **11,606** number of votes.  
- The winner of the election was:  
🎊 **Diana DeGette**, who received **73.8%** of the vote and **272892** number of votes.

Our additional analysis of the election show that:
- The counties where election took place were:
  - County 1: Arapahoe
  - County 2: Denver
  - County 3: Jefferson
- The county results (including percentage of votes and voter turnout for each county) sorted in descending order were:  
🥇 Denver County tabulated **82.8%** of the vote and **306,055** number of votes.  
🥈 Jefferson County tabulated **10.5%** of the vote and **38,855** number of votes.  
🥉 Arapahoe County tabulated **6.7%** of the vote and **24,801** number of votes.  
- The county with the highest turnout was:  
🎊 **Denver County**, which accumulated **82.8%** of the vote and **306,055** number of votes.

## Challenge Summary
The breakdown of each candidate's votes and populary in each county can also be analyzed by modifying our Python code slightly. We added an extra code that let us crunch the election data further to study whether the winning candidate won the election in all counties or she only won by a lot in certain counties or the county with the largest number of turnout. Please refer to **Table I** for more details. Interestingly the winning candidate did not win in all the counties, though she did win by more than 73% overall and 78% in Denver County alone, which is the county with the largest number of turnout. The winning candidate was slightly less popular than the 1<sup>st</sup> candidate (Candidate 1: Charles Casper Stockham) in Jefferson County. The 3<sup>rd</sup> candidate (Candidate 3: Raymon Anthony Doane) received merely 3.1% of the vote regardless of county.

**Table I: Runtime Performance Improvement by Code Refactoring**  
| County Name | Diana DeGette [votes] | [%]   | Charles Casper Stockham | [%]   | Raymon Anthony Doane | [%]] |
| :---	      |    ---:               |  ---: |     ---:                | ---:  |     ---:             | ---: |
| Arapahoe    | 15,647	              | 63.1% |   8,302                 | 33.5% |     852              | 3.4% |
| Denver      | 239,282               | 78.2% |  57,188                 | 18.7% |   9,585              | 3.1% |
| Jefferson   | 17,963	              | 46.2% |  19,723                 | 50.8% |   1,169              | 3.0% |
| Overall     | 272,892               | 73.8% |  85,213                 | 23.0% |  11,606              | 3.1% |

## Future Work
Two proposals for the code modifications would be:
1. A modified code for crunching election data in each county, state, or country across the globe, which can be used globally in every county/state/country to deliver more objective results. Experimental code is highlighted below, which I also used to transform the election data into an insightful summary that can be presented to the election commission as shown in **Table I**. This is embedded in the source code (PyPoll_Challenge.py).
```
# analyze candidate's vote breakdown by county
candidate_options_bycounty = []
candidate_votes_bycounty = {}
user_input = str(input("Key in 1. Arapahoe, 2: Denver, 3: Jefferson, or press <Enter> to continue: "))
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
    if bycounty != 0:
      if county_name == bycounty:
        if candidate_name not in candidate_options_bycounty:
          # Add the candidate name to the candidate list.
          candidate_options_bycounty.append(candidate_name)
          # And begin tracking that candidate's voter count.
          candidate_votes_bycounty[candidate_name] = 0
        candidate_votes_bycounty[candidate_name] += 1

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
```
2. Code refactoring that could transform the current code into an efficient one. This will be critical, especially when the code will be applied to crunching real big data. One idea is to use more efficient data structures, probably `defaultdict()`, or recycle some existing useful modules/libraries. In this project, I also used `dictionary.get()` to retrieve the total votes by county for further analyses.
```
# Add our dependencies.
from collections import defaultdict
:
(some codes here, like dictionary and list assignment)
:
```
A modified code that can be linked to more efficient data visualization tools, like Matplotlib, will also be better, so that the election commission can better analyze the tabulated votes and visualize the results quickly throughout several categories.

## References
[Python](https://docs.python.org/)\
[os.path.join() on windows?](https://stackoverflow.com/questions/67772480/os-path-join-on-windows)\
[Dict with 2 keys and one value](https://stackoverflow.com/questions/51679677/how-to-create-dict-with-2-keys-and-one-value)\
[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

# Election Analysis
This project exposed us to the power of Python and how we can leverage many of its useful packages, libraries, modules, and functions for performing efficient data analytics and data visualization.

## Table of Contents
- [Overview of Project](#overview-of-project)
  - [Resources](#resources)
  - [Challenge Overview](#challenge-overview)
- [Election Audit Results](#election-audit-results)
- [Challenge Summary](#challenge-summary)
- [Future Work](#future-work)
- [Lessons Learned and Troubleshooting](#lessons-learned-and-troubleshooting)
  - [Problem Statement](#problem-statement)
  - [Troubleshooting Flows](#troubleshooting-flows)
  - [Validation and Solutions](#validation-and-solutions)
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
- Output File: election_analysis.txt
- Software: [Python 3.9.12](https://docs.python.org/release/3.9.12/), [Visual Studio Code 1.71.1](https://code.visualstudio.com/updates/v1_71), or their newer releases

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
We are delighted to present our complete Election-Audit Results along with the total votes of ***369,711***, the name of County with the top turnout, ***Denver County***, and the name of winning candidate, ***Diana DeGette*** (see [Election-Audit Analysis Report](./analysis/election_analysis.txt)). To comply fully with the electoral integrity and ensure objective vote tabulation and accountable final results, the election commission and Colorado Board of Elections are welcomed to use our script [PyPoll_Challenge.py](./PyPoll_Challenge.py) and validate that our results are accurate and credible. The official summary of the election audit is highlighted below.

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
- The top county with the highest turnout was:  
🎊 **Denver County**, which accumulated **82.8%** of the vote and **306,055** number of votes.

## Challenge Summary
The breakdown of each candidate's votes and populary in each county can also be analyzed by modifying our Python code slightly. We added an extra code that let us crunch the election data further to study whether the winning candidate won the election in all counties or she only triumphed by a lot in certain counties or the county with the largest number of turnout. Please refer to **Table I** for additional analysis details and better understanding of some unique trends of this election. Interestingly enough, the winning candidate did not win in all the counties, though she did win by 73.8% overall and a whopping 78.2% in Denver County alone, which is the county with the largest number of turnout. The winning candidate was slightly less popular than the 1<sup>st</sup> candidate (Candidate 1: Charles Casper Stockham) in Jefferson County. The 3<sup>rd</sup> candidate (Candidate 3: Raymon Anthony Doane) received merely 3.1% of the vote on average regardless of county.

**Table I: Official Election-Audit Summary**

| County Name | Diana DeGette [votes] |   [%] | Charles Casper Stockham [votes] |   [%] | Raymon Anthony Doane [votes] |  [%] |
| :---	      |    ---:               |  ---: |    ---:                         |  ---: |    ---:                      | ---: |
| Arapahoe    |  15,647	              | **63.1%** |   8,302                         | 33.5% |     852                      | 3.4% |
| Denver      | 239,282               | **78.2%** |  57,188                         | 18.7% |   9,585                      | 3.1% |
| Jefferson   |  17,963	              | 46.2% |  19,723                         | **50.8%** |   1,169                      | 3.0% |
| Overall     | 272,892               | **73.8%** |  85,213                         | 23.0% |  11,606                      | 3.1% |

## Future Work
Finally, we would like to propose two proposals for modifications of the code, such that it will serve as a more objective tool for election data analysis and have a more robust feature for future applications.

1. A modified code for crunching election data in each county, state, or country across the globe, which can be used globally in every county/state/country to deliver more objective results. Experimental code is parly highlighted below, which I also used to transform the election data into an insightful summary that can be presented to the election commission and boards as shown in **Table I**. This added functionality is embedded in our source code ([PyPoll_Challenge.py](./PyPoll_Challenge.py)).

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

2. Code refactoring that could transform the current code into an efficient one for crunching big data. This will be critical, especially when the code will be applied to crunching real massive election data. One idea is to use more efficient data structures, probably `defaultdict()`, or recycle some existing useful modules/libraries. In this project, I also used `dictionary.get()` to retrieve the total votes by county without manual recalculation for further data analysis.

```
# Add our dependencies.
from collections import defaultdict
:
(some codes here, like dictionary and list assignment)
:
```

A modified code that can be linked to more efficient data visualization tools, like Matplotlib, will also be better because this will enable the election commission and boards to quickly analyze the tabulated votes and visualize the results throughout several categories.

## Lessons Learned and Troubleshooting
Because some of us, who depend on their unique Windows locale settings, experienced problems with input/output and undiscovered path, I went on to pursue extra researches for understanding the real root cause and finding a robust solution that helps us answer: "Why are we required to use forward slashes rather than backward slashes when handling relative paths?" I hope my lessons learned on troubleshooting problems of undiscovered path will be useful.

### Problem Statement
Some Windows O/S users could not easily access their local paths because of persistent errors, such as
- OSError: [Errno 22] Invalid argument: \'.**\\x07**nalysis\\election_analysis.txt\'
- FileNotFoundError: [Errno 2] No such file or directory: \'.\\\\Resources\\\\election_results.csv\'
Although hints were hardly noticeable without examining the error messages closely, we could notice two crucial clues that helped us identify the real root cause.

### Troubleshooting Flows
My troubleshooting progressed in a sequential order as follows.
1. Observation and replication of the symptoms.
  - Method: run three lines of code to replicate the symptoms. The `print()` displayed `.nalysis\election_analysis.txt` instead of `.\analysis\election_analysis.txt` or `./analysis/election_analysis.txt`.

  ```
  >>> import os
  >>> file_to_save = os.path.join(".\analysis", "election_analysis.txt")
  >>> print(file_to_save)
  .nalysis\election_analysis.txt
  ```

  - Replicable in either [VS Code](https://code.visualstudio.com/updates/v1_71), [PyCharm](https://www.jetbrains.com/pycharm/), or Linux/Git Bash with [Vi/Vim](https://www.vim.org/) text editor.
  - Editor that best triggers the crucial clues: **Vi/Vim editor** in Linux/Git Bash terminal.
2. Observation of crucial clues:
  - Unexpected bell sound every time we ran our code even though we added nothing that should ring the bell in PyPoll_Challenge.py script.
  - **`\x07`** showed up in front of the file path and Python IDE displayed `.nalysis\election_analysis.txt`.
  - Good text editors, e.g. Vi/Vim and VS Code, usually highlight certain escape characters in distinguishable font colors.
3. Isolation of the crucial clues:
  - **`\a`** or **`\x07`** was revealed to be one of the escape characters or [escape sequences](https://www.ibm.com/docs/en/zos/2.3.0?topic=set-escape-sequences) for alert/bell/alarm or the so-called [bell character](https://en.wikipedia.org/wiki/Bell_character).

### Validation and Solutions
The following code, in which we use forward slashes, work regardless of O/S on Windows, Unix/Linux, Macs, etc.

```
import os
# variable to load a file from a path.
file_to_load = os.path.join("./Resources", "election_results.csv")
# variable to save a file to a path.
file_to_save = os.path.join("./analysis", "election_analysis.txt")
```

Although using double back slashes \\\\ basically work for limited O/S including Windows, they are not recommended for codes that may be run in other O/S environments unless we have no other options. The other issue that Windows O/S could complicate further is it does not differentiate lower/uppercase letters in file/path names. Quotes will not cause significant difference, but unlike single quotes, double quotes are generally used for string interpolation in most programming languages, including Markdown. In this case, **`'\'`** is equivalent to **`"\\"`** because the latter will be interpolated, hence both resulting in \\. In summary, each line in the following code snippet works for handling input/output.

```
import os
mypath = os.getcwd()
# variable to save to a txt file in a path named 'analysis'
# Using absolute path instead of relative path
file_to_save = os.path.join(mypath, "analysis", "election_analysis.txt")
# forward slash (recommended)
file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = os.path.join('analysis', 'election_analysis.txt')
# forward slash (recommended)
file_to_save = os.path.join("./analysis", "election_analysis.txt")
file_to_save = os.path.join("./analysis/election_analysis.txt")
file_to_save = os.path.join('./analysis', 'election_analysis.txt')
file_to_save = os.path.join('./analysis/election_analysis.txt')
# backward slash (only works for Windows and very limited O/Ss)
file_to_save = os.path.join(".\\analysis", "election_analysis.txt")
file_to_save = os.path.join(".\\analysis\\election_analysis.txt")
# backward slash (only works for Windows and very limited O/Ss) '\A' for avoiding escape char '\a'
file_to_save = os.path.join('.\Analysis', 'election_analysis.txt')
file_to_save = os.path.join('.\Analysis\election_analysis.txt')
```

Each line listed below, however, caused the syntax errors as mentioned previously. If we execute the following code in Linux/Git Bash terminal, we will hear ringing bell sound instead, which is probably suitable for welcoming the winner of this election 🎊.

```
import os
# doesn't work because '\a' or '\x07' is an escape character for alert/bell/alarm sound
file_to_save = os.path.join(".\analysis", "election_analysis.txt")
file_to_save = os.path.join('.\analysis', 'election_analysis.txt')
print(file_to_save)
```

## References
[Python](https://docs.python.org/)\
[os.path.join() on windows?](https://stackoverflow.com/questions/67772480/os-path-join-on-windows)\
[Dict with 2 keys and one value](https://stackoverflow.com/questions/51679677/how-to-create-dict-with-2-keys-and-one-value)\
[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

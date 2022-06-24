# The data we need to retrieve.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path - a new file named election_analysis.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote count
total_votes = 0

# Candidate Options - declare a new list
candidate_options = []

# Declare empty dictionary for candidate votes
candidate_votes = {}

# Declare variables for Winning counts
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Upen the election results to read the file
with open(file_to_load) as election_data:

    # To do: Read and analyze the data here
    # Read the file object with the reader function.  file_reader is a variable
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in teh CSV file
    for row in file_reader:
        
        #Add to the total vote count
        total_votes +=1

        # Print the candidate name for each row
        candidate_name = row[2]

        #If the candidate does not match an existing candidate - first instance of the candidate
        if candidate_name not in candidate_options:
       
            # Add the candidate name to the candidate list.       
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrievee vote count for a candidate
        votes = candidate_votes[candidate_name]

        #  Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # If truen then set winning_count = votes and winning_percenate = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set teh winning candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count and percentage to terminal.
    #print (f"The winning candidate is {winning_candidate}, who received {winning_percentage:1f}% of the vote.")
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)
  




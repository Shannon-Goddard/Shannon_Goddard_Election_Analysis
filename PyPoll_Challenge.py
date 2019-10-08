# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a vaiable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
       # Add to the total vote count
        total_votes += 1

       # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add it to the candidate lists
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Initialize a total vote counter.
    total_votes = 0

# Create a list for the counties.
county_options = []

# Create a dictionary where the county is the key and the 
# votes cast for each county in the election are the values.
county_votes = {}

# Create an empty string that will hold the county name that had the largest turnout.
winning_county = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
       # Add to the total vote count
        total_votes += 1

       # Declare a variable that represents the number of votes that a county receives.
        county_name = row[1]

        # If the county does not match any existing county add it to the county lists
        if county_name not in county_options:

            # Add the county name to the county list.
            county_options.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")           
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    
    # Print the final vote count to the terminal.
    county_results = (
        f"\nCounty Votes:\n")
    print(county_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(county_results)

# Determine the percentage of votes for each county by looping through the counts.
# Iterate through the county lists.
    for county in county_votes:

    # Retrieve vote count of a county.
        votes = county_votes[county]

    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's name, vote count, and percentage of
        # votes to the terminal
        print(county_results)

        # Save the county results to out text file.
        txt_file.write(county_results)

        # Determine winning vote count, winning percentage, and county
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning_count = votes and winning_percent =

            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set the winning_county equal to the county's name.
            winning_county = county

    # Print the winning county results to the terminal
    winning_county_summary = ( 
        f"-----------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-----------------------------\n")

    print(winning_county_summary)
    # Save the winning county's results to the text file.
    txt_file.write(winning_county_summary)

    # Track the winning candidate, vote count, and percentage.
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate in candidate_votes:
       
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's name, vote count, and percentage of votes to the terminal
        print(candidate_results)

        # Save the candidate results to out text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal
    winning_candidate_summary = ( 
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n")
    
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    
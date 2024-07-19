# Open csv file
file = open('Resources/election_data.csv', 'r')

# Set File Contents
content = file.read()

#close file
file.close()

# Split the content into lines
lines = content.splitlines()

total_votes = 0

candidates = []
vote_count = []


# Iterate over each line
for line in lines:
    if not line.startswith("Ballot"): 
        split_line = line.split(",")

        ballot_id = int(split_line[0])
        county = split_line[1]
        candidate = split_line[2]

        total_votes = total_votes + 1

        if candidate in candidates:
            index = candidates.index(candidate)
            vote_count[index] = vote_count[index] + 1
        else: 
            candidates.append(candidate)
            vote_count.append(1)

        
print("\nElection Results\n")
print("...........................\n")
      
print("Total Votes: " + str(total_votes) + "\n")

print("...........................\n")

winner_name = ""
winner_vote_count = 0


for candidate in candidates: 
    index = candidates.index(candidate)
    candidate_vote_count = vote_count[index]

    vote_percentage = round((candidate_vote_count/total_votes)*100, 3)
    print(candidate + ": " + str(vote_percentage) + "% (" + str(candidate_vote_count) + ")\n") 

    if candidate_vote_count > winner_vote_count: 
        winner_name = candidate
        winner_vote_count = candidate_vote_count

print("...........................\n")
print("Winner: " + winner_name)
print("\n...........................\n")

new_file = open("analysis/results.txt", "w")

new_file.write("\nElection Results\n")
new_file.write("...........................\n")
      
new_file.write("Total Votes: " + str(total_votes) + "\n")

new_file.write("...........................\n")

winner_name = ""
winner_vote_count = 0


for candidate in candidates: 
    index = candidates.index(candidate)
    candidate_vote_count = vote_count[index]

    vote_percentage = round((candidate_vote_count/total_votes)*100, 3)
    new_file.write(candidate + ": " + str(vote_percentage) + "% (" + str(candidate_vote_count) + ")\n") 

    if candidate_vote_count > winner_vote_count: 
        winner_name = candidate
        winner_vote_count = candidate_vote_count

new_file.write("...........................\n")
new_file.write("Winner: " + winner_name)
new_file.write("\n...........................\n")


#close new_file
new_file.close()
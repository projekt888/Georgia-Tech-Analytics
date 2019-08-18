#main.py eric roberts 2019 PyPoll
import csv
def print_output(total_votes, candidates, perc, votes,winner): # a nice report
    output_string = "Election Results"+'\n'
    output_string+="----------------------------"+'\n'
    output_string+="Total Votes: " + str(total_votes)+'\n'
    output_string+="----------------------------"+'\n'
    for x in range(len(candidates)):
        output_string+=candidates[x]+": "+str(perc[x])+" ("+str(votes[x])+")"+'\n'
    output_string+="----------------------------"+'\n'
    output_string+="Winner: "+winner+'\n'
    return(output_string)

with open ('election_data.csv') as csv_file: #reads the file
    csv_reader = csv.reader(csv_file, delimiter=',')
    records = 0
    candidates = []
    votes = []
    percentages = []
    for row in csv_reader:
        if (records > 0):
            temporary_candidate = row[2]
            if temporary_candidate in candidates:
                votes[candidates.index(temporary_candidate)]+=1
            else:
                candidates.append(row[2])
                votes.append(1)

        records+=1

    total_votes = 0
    for n_v in votes:
        total_votes += n_v

    for v in votes:
        percentages.append(v/total_votes)

print(print_output(total_votes,candidates,percentages,votes,candidates[votes.index(max(votes))]))

f = open("pyvote.txt", "x")
f.write(print_output(total_votes,candidates,percentages,votes,candidates[votes.index(max(votes))]))
f.close()

#main.py eric roberts 2019 PyPoll
import csv

def print_output(total_votes, election_results, winner): # a nice report
    output_string = "Election Results"+'\n'
    output_string+="----------------------------"+'\n'
    output_string+=f"Total Votes: {total_votes}"+'\n'
    output_string+="----------------------------"+'\n'
    for candidate in election_results:
        output_string+=f"{candidate['name']}: {candidate['percentage']*100:.3f}% ({candidate['votes']})"+'\n'
    output_string+="----------------------------"+'\n'
    output_string+="Winner: "+winner+'\n'
    return(output_string)

with open ('election_data.csv') as csv_file: #reads the file
    csv_reader = csv.reader(csv_file, delimiter=',')
    election_results = []
    total_votes = 0
    winner = ""
    winners_votes = 0

    row = next(csv_reader)
    for row in csv_reader:

        new_candidate = True
        total_votes +=1

        for candidate in election_results:
            if(candidate["name"] == row[2]):
                new_candidate = False
                candidate["votes"]+=1

        if new_candidate:
            election_results.append({"name":row[2],"votes":1,"percentage":0})

    #percentages and winner
    for candidate in election_results:
        if candidate["votes"] > winners_votes:
            winners_votes = candidate["votes"]
            winner = candidate["name"]
        candidate["percentage"] = candidate["votes"]/total_votes

print(print_output(total_votes,election_results,winner))

f = open("pyvote.txt", "w")
f.write(print_output(total_votes,election_results,winner))
f.close()

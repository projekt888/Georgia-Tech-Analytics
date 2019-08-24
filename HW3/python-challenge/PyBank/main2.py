#main.py eric roberts 2019 (PyBank)
import csv
import statistics
import operator

def print_output(months, net_total_profits, avg, month_max,max,month_min,min): #creates the report
    output_string = "Financial Analysis"+'\n'
    output_string+="----------------------------"+'\n'
    output_string+=f"Total Months: {months}"+'\n'
    output_string+=f"Total: ${net_total_profits:.0f}"+'\n'
    output_string+=f"Average  Change: ${avg:.2f}"+'\n'
    output_string+=f"Greatest Increase in Profits: {month_max} (${max:.0f})"+'\n'
    output_string+=f"Greatest Decrease in Profits: {month_min} (${min:.0f})"+'\n'
    return(output_string)

with open ('budget_data.csv') as csv_file: #reads the file, assumes it's in the same directory
    csv_reader = csv.reader(csv_file, delimiter=',')
    months = 0
    last_month = 0
    this_month = 0
    deltas = {}
    net_total_profits = 0

    row = next(csv_reader) #skip the header
    for row in csv_reader:

        months+=1
        net_total_profits += float(row[1])

        if (months>1):
            #dont record the first month as a change
            this_month = float(row[1])
            deltas[str(row[0])] = this_month - last_month

        last_month = float(row[1])

max_month = max(deltas.items(),key=operator.itemgetter(1))
min_month = min(deltas.items(),key=operator.itemgetter(1))

print(print_output(months, net_total_profits, statistics.mean(list(deltas.values())),max_month[0],max_month[1],min_month[0],min_month[1]))
### NOW WRITE THIS TO A file
f = open("pybank.txt", "w")
f.write(print_output(months, net_total_profits, statistics.mean(list(deltas.values())),max_month[0],max_month[1],min_month[0],min_month[1]))
f.close()

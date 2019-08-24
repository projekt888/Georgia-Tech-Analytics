#main.py eric roberts 2019 (PyBank)
import csv
import statistics

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
    changes = [] # deltas (how much money did we make/lose)
    months_a = [] #a parallel array with the months.  The parallel array lets me use the max and min functions
    net_total_profits = 0

    row = next(csv_reader) #skip the header
    for row in csv_reader:

        months+=1
        net_total_profits += float(row[1])

        if (months>1):
            #dont record the first month as a change
            this_month = float(row[1])
            changes.append(this_month - last_month)
            months_a.append(str(row[0]))

        last_month = float(row[1])

    print(print_output(months, net_total_profits, statistics.mean(changes),months_a[changes.index(max(changes))],max(changes),months_a[changes.index(min(changes))],min(changes)))
    ### NOW WRITE THIS TO A file
    f = open("pybank.txt", "w")
    f.write(print_output(months, net_total_profits, statistics.mean(changes),months_a[changes.index(max(changes))],max(changes),months_a[changes.index(min(changes))],min(changes)))
    f.close()

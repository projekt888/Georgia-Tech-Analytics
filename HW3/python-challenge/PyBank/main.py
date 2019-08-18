#main.py eric roberts 2019 (PyBank)
import csv
import statistics

def print_output(months, net_total_profits, avg, month_max,max,month_min,min): #creates the report
    output_string = "Financial Analysis"+'\n'
    output_string+="----------------------------"+'\n'
    output_string+="Total Months: " + str(months)+'\n'
    output_string+="Total " + str(net_total_profits)+'\n'
    output_string+="Average  Change:" + str(avg)+'\n'
    output_string+="Greatest Increase in Profits: " + month_max+ ": " + str(max)+'\n'
    output_string+="Greatest Decrease in Profits: " + month_min+ ": " + str(min)+'\n'
    return(output_string)

with open ('budget_data.csv') as csv_file: #reads the file
    csv_reader = csv.reader(csv_file, delimiter=',')
    lines = 0
    months = 0
    last_month = 0
    this_month = 0
    changes = [] # deltas (how much money did we make/lose)
    months_a = [] #a parallel array with the months.  The parallel array lets me use the max and min functions
    net_total_profits = 0
    for row in csv_reader:
            #skip the header
            lines+=1
            if (lines >1):
                months+=1
                net_total_profits += float(row[1])

                #dont record the first month as a change
                if (lines>2):
                    this_month = float(row[1])
                    changes.append(this_month - last_month)
                    months_a.append(str(row[0]))

                last_month = float(row[1])

    print(print_output(months, net_total_profits, statistics.mean(changes),months_a[changes.index(max(changes))],max(changes),months_a[changes.index(min(changes))],min(changes)))
    ### NOW WRITE THIS TO A file
    f = open("pybank.txt", "x")
    f.write(print_output(months, net_total_profits, statistics.mean(changes),months_a[changes.index(max(changes))],max(changes),months_a[changes.index(min(changes))],min(changes)))
    f.close()

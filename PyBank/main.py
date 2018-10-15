#PyBank
#import modules
import os
import csv

#file path to read
csvBank = os.path.join('Resources', 'budget_data.csv')

#file path to write
outFile = os.path.join('Resources', 'output.txt')

rows=[] #place holder for rows array so it does not disapper after csvfile closes

#create file pointer for read
with open (csvBank, newline="") as csvfile:
    #creates a reader 
    csvBudget=csv.reader(csvfile,delimiter=',')
    #to see the header
    csv_header=next(csvBudget)
    #print(csv_header)

    #to read row one at a time and populate in "rows" array
    rows = [row for row in csvBudget]

#create file pointer for write
with open(outFile,"w") as txtfile:

    #print header
    print("Financial Analysis")
    print("-----------------------------")

    print("Financial Analysis",file=txtfile)
    print("-----------------------------",file=txtfile)
    
    #to get total months
    months = len(rows)
    
    print(f'Total Months: {months}')
    print(f'Total Months: {months}', file=txtfile)
    
    #to get total net amount of profit/losses
    total = sum(int(row[1]) for row in rows)
    print(f'Total: ${total}')
    print(f'Total: ${total}',file=txtfile)

    #to print greateset increase in profits
    greatestInc=0
    prevProfit=0
    greatestMonth=""
    for row in rows:
        currentProfit=int(row[1]) #profit of current month found in second column
        
        if((currentProfit-prevProfit) > greatestInc):
            greatestMonth = row[0]
            greatestInc = currentProfit-prevProfit
        prevProfit = currentProfit    

    print(f'Greatest Increase in Profits: {greatestMonth} (${greatestInc})')
    print(f'Greatest Increase in Profits: {greatestMonth} (${greatestInc})',file=txtfile)

    #to get the greatest decrease
    prevProfit=0
    greatestDec = 0
    greatestMonth = ""
    for row in rows:
        currentProfit=int(row[1]) #profit of current month found in second column
        
        if((currentProfit-prevProfit) < greatestDec):
            greatestMonth = row[0]
            greatestDec = currentProfit-prevProfit
        prevProfit = currentProfit    

    print(f'Greatest Decrease in Profits: {greatestMonth} (${greatestDec})')
    print(f'Greatest Decrease in Profits: {greatestMonth} (${greatestDec})',file=txtfile)

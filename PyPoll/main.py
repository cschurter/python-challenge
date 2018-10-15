#PyPoll
#import modules
import os
import csv

#file path to read
csvPoll = os.path.join('Resources', 'election_data.csv')

#file path to write
outFile = os.path.join('Resources', 'output.txt')

rows=[] #place holder for rows in array so it does not disapper after csvfile closes
votes={}

#create file pointer for read
with open (csvPoll, newline="") as csvfile:
    #creates a reader 
    csvreader=csv.reader(csvfile,delimiter=',')
    #to see the header
    csv_header=next(csvreader)
    #print(csv_header)

    #to read row one at a time and populate in "rows" array
    rows = [row for row in csvreader]

#create file pointer for write
with open(outFile,"w") as txtfile:

    #print header
    print("Election Results")
    print("-----------------------------")

    print("Election Results",file=txtfile)
    print("-----------------------------",file=txtfile) 

    #total votes
    totalVotes = len(rows)
    print(f'Total Votes: {totalVotes}')
    print(f'Total Votes: {totalVotes}',file=txtfile)
    
    print("-----------------------------") 
    print("-----------------------------",file=txtfile) 

    for row in rows:
        if(row[2] in votes): #if key row[2] exists in votes dictionary
            votes[row[2]] += 1
        else:
            votes[row[2]] =1
    #print(votes) #prints total votes for each candidate
   
    
    for key in votes.keys():
        print(f'{key}:{votes[key]}') 
        print(f'{key}:{votes[key]}',file=txtfile)
    
    #to get percentage of votes each candidate won    
  
        

    



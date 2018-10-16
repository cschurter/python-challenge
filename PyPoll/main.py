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

    #total votes
    totalVotes = len(rows)

    for row in rows:
        if(row[2] in votes): #if key row[2] exists in votes dictionary
            votes[row[2]] += 1
        else:
            votes[row[2]] =1
    #print(votes) #prints total votes for each candidate
       
    #to get percentage of votes each candidate won    
    def getPercentage(votes):
        return (votes/totalVotes)

    #print header
    print("Election Results")
    print("-----------------------------")

    print("Election Results",file=txtfile)
    print("-----------------------------",file=txtfile) 

    print(f'Total Votes: {totalVotes}')
    print(f'Total Votes: {totalVotes}',file=txtfile)
    
    print("-----------------------------") 
    print("-----------------------------",file=txtfile) 
    
    keys=list(votes.keys())
    counts=list(votes.values())

    khanVotes = votes['Khan']
    correyVotes = votes['Correy']
    liVotes = votes['Li']
    otooleyVotes = votes["O'Tooley"]

    print(f'{keys[0]}: {getPercentage(khanVotes):.3%} ({counts[0]})')
    print(f'{keys[0]}: {getPercentage(khanVotes):.3%} ({counts[0]})', file=txtfile)
    
    print(f'{keys[1]}: {getPercentage(correyVotes):.3%} ({counts[1]})')
    print(f'{keys[1]}: {getPercentage(correyVotes):.3%} ({counts[1]})', file=txtfile)
    
    print(f'{keys[2]}: {getPercentage(liVotes):.3%} ({counts[2]})')
    print(f'{keys[2]}: {getPercentage(liVotes):.3%} ({counts[2]})', file=txtfile)
    
    print(f'''{keys[3]}: {getPercentage(otooleyVotes):.3%} ({counts[3]})''')
    print(f'''{keys[3]}: {getPercentage(otooleyVotes):.3%} ({counts[3]})''', file=txtfile)
    
    print("-----------------------------") 
    print("-----------------------------",file=txtfile) 

    indxWinner = counts.index(max(counts))
    print(f'Winner: {keys[indxWinner]}')
    print(f'Winner: {keys[indxWinner]}',file=txtfile)

    print("-----------------------------") 
    print("-----------------------------",file=txtfile)
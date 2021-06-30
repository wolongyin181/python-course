import csv

with open('scoreboard.csv','a') as file:
    csvwriter=csv.writer(file)
    csvwriter.writerow(['Brock','2'])


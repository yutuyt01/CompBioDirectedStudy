#importing the necessary packages
import csv

#initializing an empty list to store the similarities
similarities = []

#opening the first tsv file
with open('C:\Comp Bio\CompBioDirectedStudy\DatabaseExtract_v_1.01.csv', newline='') as tsvfile1:
    data1 = csv.reader(tsvfile1)
    #skipping the header row
    next(data1)
    #iterating through each row in the tsv file
    for row in data1:
        #storing the value of the chosen columns in variables
        value1 = row[1]
        

#opening the second tsv file
with open('C:\Comp Bio/brain.tsv', newline='') as tsvfile2:
    data2 = csv.reader(tsvfile2, delimiter='\t')
    #skipping the header row
    next(data2)
    #iterating through each row in the tsv file
    for row in data2:
        #storing the value of the chosen columns in variables
        value3 = row[2]
        #checking if the values of the chosen columns are equal
        if value1 == value3:
            #appending the similarity to the list
            similarities.append(value1)

#printing the list of similarities
print(similarities)
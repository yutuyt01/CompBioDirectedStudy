# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from Bio import Entrez, SeqIO, pairwise2
from Bio.Seq import Seq

from Bio.pairwise2 import format_alignment
Entrez.email = "compbioproject23@gmail.com"

handle = Entrez.efetch(db="nuccore",
                       id="NM_000014.6",
                       rettype="fasta",
                       retmode="text")

record = SeqIO.read(handle, "fasta")

siRNA = Seq("")
seedRegion = Seq("")
geneSequence = record.seq
i = 23
g = 7
h = 0
sequenceArray = []
idList = []


testRegion = Seq("")
# real file remmed out
#for index, record in enumerate(SeqIO.parse("../../Documents/GRCh38_latest_rna.fna", "fasta")):
for index, record in enumerate(SeqIO.parse("../../Downloads\TestGenes.fasta", "fasta")):
    assert isinstance(record.seq, object)
    sequenceArray.append(record.seq)
    idList.append(record.id)
    # print(idList)
    # print(sequenceArray)

matchArray = [0] * Seq.__len__(geneSequence)
siRNAArray = [Seq("")] * Seq.__len__(geneSequence)

while i < Seq.__len__(geneSequence):
    #siRNA = geneSequence[i - 23:i]
    siRNA = "CCAGGACTGCGGGAAGGCGCGGG"
    # print(siRNA)
    seedRegion = siRNA[1:8]
    # print(seedRegion)
    h = 0
    g = 7
    matches = 0
    siRNAArray[i-23] = siRNA
    while h < len(sequenceArray):
        g = 7
        while g < Seq.__len__(sequenceArray[h]):
            pullSequence = sequenceArray[h]
            testRegion = pullSequence[g - 7:g]
            # print(testRegion)
            if seedRegion == testRegion:
                print('Match!')
                print('Occurred at nucleotide', (g-7))
                print('siRNA strand of ' + siRNA + ' and a base region of ' + seedRegion)
                print('                 -------')
                print('Occured in gene ' + idList[h])
                print()
                matches += 1
                # TODO complement
            g += 1
        h += 1
    i += 1
    matchArray[i-23] = matches


for i in range(5):
    print("The least number of matches occurs here at " + siRNAArray[matchArray.index(min(matchArray))]) #+ " with " + min(matchArray) + " matches")
    print(min(matchArray))
    matchArray.pop(matchArray.index(min(matchArray)))




#minIndex = min(matchArray)
#bestStrand = sequenceArray[minIndex]
#print('Your best strand of siRNA is ' + )




# print(record.seq)

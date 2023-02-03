from Bio import Seq
from Bio.Seq import Seq
from itertools import combinations
import math

class siRNADesign:
    # This class defines a tester for input sequences. Initalize with studies that user indicates to use
    def __init__(self, uitei, reynolds, amarzguioui, tempstability):
        self.uitei = uitei
        self.reynolds = reynolds
        self.amarzguioui = amarzguioui
        self.tempstability = tempstability
        self.irTest = ""
    def computeSeedRegionStab(self, sequence):
        gccontent = (sequence.count("G") + sequence.count("C")) / len(sequence)
        return (79.8 + (15 * math.log10(0.1)) + (58.4 * gccontent) + (11.8 * math.pow((gccontent), 2)) - (820 / len(sequence)))
    def check(self, sequence):
        if (self.uitei == True):
            # True = passes check
            if (
                # Rule 1 - position 1 needs to be A and U 
                (sequence.find("A", 0, 1) != -1  or sequence.find("U") != -1) and
                # Rule 2 - AU rich (>=4) in 1-7
                sequence.count("A", 0, 7) + sequence.count("U", 0, 7) >= 4 and
                # Rule 3 - G or C at position 19
                (sequence.count("G", 18, 19) or sequence.count("C", 18, 19))
                # Rule 4 - no GC stretch longer than 9                 
            ):
                for i in range(len(sequence) - 10):
                    stretch = sequence[i : i + 10]
                    if (stretch.count("G") + stretch.count("C")) > 9:
                        return False # fails rule 4
                pass # passes ui-tei   
            else:
                return False # fails rules any rule 1-3
        if (self.reynolds == True):
            # TODO Reynolds rule currently assumes full compelentation on passenger strand - THIS IS NOT NECESSARILY THE CASE! Do more research if we go to regionals. 
            # Rule 1 - No inverted repeats (computationally slightly heavy)
            irTest = [sequence[x:y] for x, y in combinations(range(len(sequence) - 10), r = 2)]   
            # first 10 NT 
            irTest2nd = sequence[10:len(sequence)]
            for v in irTest:
                rv = v.reverse_complement_rna()
                # TODO if we go onto regionals i want to expand on rna folding kinetics - reverse strands of more than 3 is just a placeholder
                if len(rv) > 3:
                    if (irTest2nd.find(rv) != -1):
                        #print("found r complement" + str(sequence.find(rv)) + v)
                        print("failing inv reps FIX THIS!")
                        #return False # fails, has inverted repeats
                        pass
            if (
                # Rule 2 - 3 or more AUs from 1 to 5
                sequence.count("A", 0, 5) + sequence.count("U", 0, 5) >= 4 and
                # Rule 3 - GC Content of whole sequence 30-52%
                30/100 <= ((sequence.count("G") + sequence.count("C")) / len(sequence)) <= 52/100 and
                # Rule 4 - Nucleotide 1 NOT G or C (redundant with Ui-Tei) see rule 5
                sequence.find("U", 0, 1) != -1 and
                # Rule 5 - Incorporated above. Antisense needs to be A at passenger position 1, which means position 1 nucleotide on guide must be U. More specific than Ui-Tei but NOT conflicting.
                # Rule 6 - Passenger strand cannot be G at nucleotide position 7 on guide. Translates to cannot have C on guide at 7
                sequence.find("C", 6, 7) == -1 and
                # Rule 7 - Must be U at position 10 on guide. Must then be A at nuc 10 
                sequence.find("A", 9, 10) != -1 and
                # Rule 8 - Must be A at position 17 on guide. Must then be U at nuc 17
                sequence.find("U", 16, 17) != -1
            ):
                pass # passes reynolds
            else:
                print("failing reynolds")
                return False
        if (self.amarzguioui == True):
            # TODO amarzguioui is incomplete. I'm going to say that this distinction is not strong enough based on what I could see off their data sets and small siRNA data. Add this as an option after project forum when I can ask someone about A/U differential too
            if (
                # Rule 1 in todo above
                # Rule 2 - G or C at position 19 of passenger. Means 
                0==0
            ):
                pass # passes amarzguioui
            else:
                return False # fails amarzguioui
        if (self.computeSeedRegionStab(sequence=sequence) > self.tempstability):
            #return False # fails seed region temperature designation
            pass # TODO this does not work. I need more background on the formula behind it
        return True # passes all user selected tests
# testing below
testSeq = Seq("UUUAUAUAAAUAUCGGUCGGC")

tester = siRNADesign(True, True, False, 50)
print(tester.check(testSeq))
print(tester.computeSeedRegionStab(testSeq))

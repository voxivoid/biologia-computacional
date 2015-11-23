__author__ = 'André'
from Bio import SeqIO
import random
"""
fasta_sequences = SeqIO.parse(open(u".\\fasta"),'fasta')
for i in fasta_sequences:
    print i.seq

simulator(u".\\fasta", 0, 1, 0, 0)
"""

def simulator(fastaDir, nGen, mr, rr, rfl):
    fastaSequences = SeqIO.parse(open(fastaDir),'fasta')
    sequences = []
    for fastaSeq in fastaSequences:
        sequences.append(list(str(fastaSeq.seq)))
    for i in range(nGen):
        print "::::::::::::: Gen " + str(i) + ":::::::::::::"
        mutation(sequences, mr)
        recombination(sequences, rr, rfl)

def mutation(sequences, mr):
    print "------- Mutation -------"
    for fastaSeq in sequences:
        rngMutate = random.random()
        if(rngMutate <= mr):
            rngPosition = random.randint(0, len(fastaSeq) - 1)
            print "Pos: " + str(rngPosition)
            while True:
                rngBase = random.choice("actg")
                if(rngBase != fastaSeq[rngPosition]):
                    fastaSeq[rngPosition] = rngBase
                    break

        print "".join(fastaSeq)

def recombination(sequences, rr, rfl):
    print "------- Recombination -------"
    for fastaSeq in sequences:
        rngRecombination = random.random()
        if(rngRecombination <= rr):
            rngPosition = random.randint(0, len(fastaSeq) - 1 - rfl)
            print "Pos: " + str(rngPosition)
            while True:
                rngSequence = random.randint(0, len(sequences) - 1)
                if(sequences[rngSequence] is not fastaSeq):
                    print "Seq: " + str(rngSequence)
                    for i in range(rngPosition, rngPosition + rfl):
                        fastaSeq[i] = sequences[rngSequence][i].lower()
                    break
        print "".join(fastaSeq)



simulator(u".\\fasta", 3, 1, 1, 4)

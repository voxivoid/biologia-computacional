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
    mutation(sequences, mr)

def mutation(sequences, mr):
    for fastaSeq in sequences:
        rngMutate = random.random()
        if(rngMutate <= mr):
            rngPosition = random.randint(0, len(fastaSeq) - 1)
            while True:
                rngBase = random.choice("actg")
                if(rngBase != fastaSeq[rngPosition]):
                    print rngPosition
                    fastaSeq[rngPosition] = rngBase
                    break

        print "".join(fastaSeq)

simulator(u".\\fasta", 0, 1, 0, 0)

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import random

def mutation(sequences, mr):
    #print "------- Mutation -------"
    for fastaSeq in sequences:
        rngMutate = random.random()
        if(rngMutate <= mr):
            rngPosition = random.randint(0, len(fastaSeq) - 1)
            #print "Pos: " + str(rngPosition)
            while True:
                rngBase = random.choice("ACTG")
                if(rngBase != fastaSeq[rngPosition]):
                    fastaSeq[rngPosition] = rngBase
                    break

        #print "".join(fastaSeq)

def recombination(sequences, rr, rfl):
    #print "------- Recombination -------"
    for fastaSeq in sequences:
        rngRecombination = random.random()
        if(rngRecombination <= rr):
            rngPosition = random.randint(0, len(fastaSeq) - 1 - rfl)
            #print "Pos: " + str(rngPosition)
            while True:
                rngSequence = random.randint(0, len(sequences) - 1)
                if(sequences[rngSequence] is not fastaSeq):
                    #print "Seq: " + str(rngSequence)
                    for i in range(rngPosition, rngPosition + rfl):
                        fastaSeq[i] = sequences[rngSequence][i].upper()
                    break
        #print "".join(fastaSeq)

def simulator(fastaDirInput, nGen, mr, rr, rfl):
    fastaSequences = SeqIO.parse(open(fastaDirInput),'fasta')
    sequences = []
    for fastaSeq in fastaSequences:
        sequences.append(list(str(fastaSeq.seq)))
    for i in range(nGen):
        #print "::::::::::::: Gen " + str(i) + ":::::::::::::"
        mutation(sequences, mr)
        recombination(sequences, rr, rfl)

    sequencesOutput = []
    for seq in sequences:
        sequencesOutput.append("".join(seq))
    return sequencesOutput



def randomSequence(size):
    dna = ""
    for count in range(size):
        dna += random.choice("CGTA")
    return dna

def initialRandomFasta(fastaDirOutput, size, popsize):
    records = []
    initialRecords = []
    for i in range(2):
        rSequence = randomSequence(size)
        initialRecords.append(SeqRecord(Seq(rSequence), "seq" + str(i) + "_initial", "", "", [], [], {}, {}))
        for j in range(popsize/2):
            records.append(SeqRecord(Seq(rSequence), "seq" + str(i) + "_" + str(j), "", "", [], [], {}, {}))
    SeqIO.write(records, fastaDirOutput, "fasta")
    return initialRecords

def q2():
    fastaDirInput = u".\\q2.fasta"
    initialRecords = initialRandomFasta(fastaDirInput, 100,6)

    sequences = simulator(fastaDirInput, 1000, 0.1, 0, 0)
    saveRecordsFasta(initialRecords, sequences, u".\\q2_1.fasta")

    sequences = simulator(fastaDirInput, 1000, 0.1, 0.1, 5)
    saveRecordsFasta(initialRecords, sequences, u".\\q2_2.fasta")

    sequences = simulator(fastaDirInput, 1000, 0.1, 0.001, 5)
    saveRecordsFasta(initialRecords, sequences, u".\\q2_3.fasta")

    sequences = simulator(fastaDirInput, 1000, 0.001, 0.1, 5)
    saveRecordsFasta(initialRecords, sequences, u".\\q2_4.fasta")

    sequences = simulator(fastaDirInput, 2500, 0.1, 0.01, 5)
    saveRecordsFasta(initialRecords, sequences, u".\\q2_5.fasta")

def saveRecordsFasta(initialRecords, sequences, fastaOutputDir):
    records = []
    for rec in initialRecords:
        records.append(rec)
    for i in range(1,3):
        for j in range(len(sequences)/2):
            records.append(SeqRecord(Seq(sequences[j]), "seq" + str(i-1) + "_" + str(j), "", "", [], [], {}, {}))
    SeqIO.write(records, fastaOutputDir, "fasta")


q2()
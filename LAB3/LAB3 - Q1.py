from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import random
import math

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
    hd = []
    jc = []
    for i in range(nGen):
        #print "::::::::::::: Gen " + str(i) + ":::::::::::::"
        mutation(sequences, mr)
        recombination(sequences, rr, rfl)
        sequencesOutput = []
        for seq in sequences:
            sequencesOutput.append("".join(seq))

        x = 0
        hdTemp = 0
        jcTemp = 0
        for i in range(len(sequencesOutput)):
            for j in range(i+1, len(sequencesOutput)):
                h = float(hammingDistance(sequencesOutput[i], sequencesOutput[j]))
                hdTemp += float(h)
                if (h < 0.75):
                    jcTemp += jukesCantor(h)
                x += 1
        hdTemp /= float(x)
        jcTemp /= float(x)
        hd.append(hdTemp)
        jc.append(jcTemp)
    print hd
    print jc
    f = open("q1_output.txt", "w")
    for i in range(len(hd)):
        f.write(str(i) + " " + str(hd[i]) + " " + str(jc[i]) + "\n")
    f.close()

def hammingDistance(s1, s2):
    return (sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2)))/float(len(s1))

def jukesCantor(p):
    return (-3/float(4)) * math.log(float(1) - ((4/float(3)) * float(p)))

def randomSequence(size):
    dna = ""
    for count in range(size):
        dna += random.choice("CGTA")
    return dna

def initialRandomFasta(fastaDirOutput, size, popsize):
    records = []
    rSequence = randomSequence(size)
    for i in range(popsize):
        records.append(SeqRecord(Seq(rSequence), "seq" + str(i), "", "", [], [], {}, {}))
    SeqIO.write(records, fastaDirOutput, "fasta")

def q1():
    fastaDirInput = u".\\q1.fasta"
    initialRandomFasta(fastaDirInput, 100, 100)

    simulator(fastaDirInput, 5000, 0.1, 0, 0)

def saveRecordsFasta(sequences, fastaOutputDir):
    records = []
    for i in range(1,3):
        for j in range(len(sequences)/2):
            records.append(SeqRecord(Seq(sequences[j]), "seq" + str(i-1) + "_" + str(j), "", "", [], [], {}, {}))
    SeqIO.write(records, fastaOutputDir, "fasta")


q1()
#simulator(u".\\fasta", "", 3, 1, 1, 4)

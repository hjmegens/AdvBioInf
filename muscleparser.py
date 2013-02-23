import argparse
import sys
import os

parser = argparse.ArgumentParser( description='Aligns fasta file and returns stats per aligned base')
parser.add_argument("-i", "--infile", help="input file", nargs=1)
parser.add_argument("-o", "--outfile", help="output file", nargs=1)

def read_FASTA(filename):
    with open(filename) as file:
        contents = file.read()
    entries = contents.split('>')[1:]
    partitioned_entries = [entry.partition('\n') for entry in entries]
    name_seq_pairs = [(entry[0],entry[2]) for entry in partitioned_entries]
    name_seq_pairs2 = [(pair[0],pair[1].replace('\n','')) for pair in name_seq_pairs]
    return name_seq_pairs2

def compute_average_length(seq_list):
    lengths = [len(entry[1]) for entry in seqs]
    totallength=0
    for length in lengths:
        totallength += length

    averagelength = totallength/len(lengths)
    return averagelength

def set_dna_or_rna(hashtable):
    prefered_base = 'T'
    if hashtable['U']>hashtable['T']:
       prefered_base = 'U'
    return prefered_base

def print_row(rowtuple):
    t1,t2,t3,t4,t5,t6,t7,t8 = rowtuple
    print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'.format(t1,t2,t3,t4,t5,t6,t7,t8))

args = parser.parse_args()
fasta_file=args.infile[0]
alignedfile=args.outfile[0]
seqs = read_FASTA(fasta_file)

averagelength = compute_average_length(seqs)

print('total sequences: '+str(len(seqs))+'\tmean length: '+str(averagelength)+'\n',end='')

cmd = 'muscle -in '+fasta_file+' -out '+alignedfile+' -log logfile.txt 2>output.txt'
os.system(cmd)

aligned_seqs = read_FASTA(alignedfile)
length_alignment = len(aligned_seqs[0][1])

print('length alignment: '+str(length_alignment)+'\n',end='')

print_row(('base','A','C','G','T','N','-','sum'))

for i in range(length_alignment):
    bases={'A': 0,'C': 0,'G': 0,'U': 0,'T': 0,'N': 0,'-': 0}
    for j in range(len(aligned_seqs)):
        for base in bases.keys():
            #print('base is now: '+base+' and count is: '+str(bases[base]))
            if aligned_seqs[j][1][i].upper() == base:
                bases[base] += 1
    
    total = 0
    for base in bases.keys():
       total += bases[base]

    dna_or_rna = set_dna_or_rna(bases)
    print_row((i,bases['A'],bases['C'],bases['G'],bases[dna_or_rna],bases['N'],bases['-'],total))


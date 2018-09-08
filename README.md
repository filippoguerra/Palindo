# Palindo
A lil program to find palindromic DNA sequences.
In the analysis of the input sequence the only a priori assumption that is made is that the recognized sequence is palindromic. Additional information about the flanking bases can also be retrieved: in general, the program recognizes any sequence that has formula:
N(n)P(m)X(o)P(m)N(n)
Where N(n) is a sequence composed by any n bases, P(m) is the sequence of which the reverse complement appears downstream X(o), the central bases. The program can discriminate between strong (G/C) bases and weak (A/T) bases at the X position. 
Examples of such sequence are: 
N(0)P(3)X(1)P(3)N(0): ACATTCT; CGTAACG;
N(2)P(3)X(1)P(3)N(2): GATACGGTACG; CTGACGGTCGA;
N(4)P(4)X(1)P(4)N(4): TCGAGTGCAGCACTACA; TAGCAACATTGTTGGGA. 
The function palfinder can retrieve all the palindromes with sequence N0P3X1P3N0 present in Drosophila melanogaster genome (137mln bp) in 2:45 minutes of CPU time. 
The sequences are also indexed by occurrence and can be analyzed to give a normalized occurrence of each sequence with the function ratio. 
The last function in the program, called logo, is a utility function to create .csv files that retrieves the occurrence of each base at each position for a given set of sequences. This is useful to have a clear overview on the identity of the bases flanking the palindrome. Any program for the analysis of data (e.g. MS Excel) can be used to create weblogo-like bar charts

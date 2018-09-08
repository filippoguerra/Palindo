print "Here we have three functions:"
print "-palfinder(file):\n \t takes a text file containing fasta-like sequence and finds palindromes.\n \t Returns a list of palindromes ordered by occurance or alphabetically. These are respectively inputs for -ratio and -findseq"
print "-ratio(enriched,reference):\n \t takes the output of palfinder for a putative target region or a sequence enriched in palindromes and compare it with a reference."
print "-logo(list):\n \t creates a csv matrix with recurrance of any base at any position in a sequence"
def palfinder(file):
    content = open(file).readlines()
    z=str(raw_input("Do you want to discriminate between different central wobbling bases? (y/n)"))
    x=int(raw_input("How many central wobbling bases does the target site have? (0,1,2...n)"))
    y=int(raw_input("How many bases are specifically recognised by the TF? (3,4...n); 0=unknown")) 
    q=int(raw_input("How many flanking bases outside the core palindromic region are you interested into? "))
    sequence=""
    general="N"*q+"P"*y+"X"*x+"P"*y+"N"*q
    title="Common palindrome sequences with structure "+general+ "in sequences: \n "
    nucleotides={"A":"T","T":"A","C":"G","G":"C"}
    for riga in content:
        if riga[0]==">":
            title += riga.strip() + "\n"           
        elif riga[0] in nucleotides and riga[1] in nucleotides:
            sequence+=riga.strip()
    P=["A","C"]
    listpalindrome={}
    pos=0
    distance=0
    c=1
    import sys
    toolbar_width = 40
    pbs="A"
    print "Will analyse " + str(len(sequence))+ " bases, looking for sequences like "+general
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in xrange(toolbar_width):
        while pos <len(sequence)-(q+y*2):
            if sequence[pos+distance+1+x] == nucleotides.get(sequence[pos-distance]):
                distance+=1
            else:
                core=sequence[pos+1:pos+x+1].replace("A","W").replace("T","W").replace("C","S").replace("G","S")
                if y>0 and distance>(y-0.5):
                    pbs=sequence[pos-q-y+1:pos+1]+core+sequence[pos+1+x:pos+y+1+x+q]
                elif y==0 and distance>3:
                    pbs=sequence[pos-(q-distance+1):pos+1]+core+sequence[pos+1+x:pos+distance+1+x+q]
                else:
                    pbs="A"
                    if (float(c)/40)<(float(pos)/len(sequence)):
                        sys.stdout.write("-")
                        sys.stdout.flush()
                        c+=1
                if pbs!="A":
                    if z=="n":
                        pbs=pbs.replace("W","X").replace("S","X")
                    if sequence[pos-1] in P:
                        pbs=pbs[::-1]
                    if pbs not in listpalindrome:
                        listpalindrome[pbs]=1
                    else:
                        listpalindrome[pbs]+=1
                pos+=1
                distance=0
    sys.stdout.write("-"+"\n")

    save=raw_input("Save list of palindromic sequences in a file? (y/n) ")
    if save=="y":
        tupla=sorted (listpalindrome.items(), key=lambda x:x[1])
        fale=raw_input("Name destination file\n")
        f=open(str(fale)+'.txt','w')
        f.write(title)
        f.write(str( tupla))
    return listpalindrome

def ratio(g,b):
    ratio={}
    rutio={}
    for putativesite in g:
        if putativesite in b:
            rutio [str (putativesite) + "; " + str (putativesite[::-1])]=(float(g[putativesite])/float(b[putativesite]))
            ratio [str (putativesite) + "; " + str (putativesite[::-1])]=(float(g[putativesite])/float(b[putativesite]))
        else:
            rutio[str (putativesite) + "; " + str (putativesite[::-1])]=str(g[putativesite])+"; specific"
            
    sorta= sorted (rutio.items(), key=lambda x:x[1])
    fale=raw_input("Name destination file\n")
    f=open(str(fale)+'.txt','w')
    f.write(str(sorta))
    return ratio

def logo(content):
    out=""
    pos=0
    quast=[]
    lista=[]
    quest= raw_input("Sequences to be found separated by comma, no space: ").split(",")
    for x in quest:
        quast.append(x[::-1])
        quast.append(x)    
    for x in content:
        lista.append(x)
    length=len(lista)
    n=len(lista[0])
    a=[0]*n
    t=[0]*n
    g=[0]*n
    c=[0]*n
    s=[0]*n
    w=[0]*n
    x=[0]*n
    pus=0
    while pos < length-1:
            if any (x in lista[pos] for x in quast):
                while pus<n:
                    if (lista[pos])[pus]=="A":
                        a[pus]=a[pus]+content[lista[pos]]
                    if (lista[pos])[pus]=="T":
                        t[pus]=t[pus]+content[lista[pos]]
                    if (lista[pos])[pus]=="C":
                        c[pus]=c[pus]+content[lista[pos]]
                    if (lista[pos])[pus]=="G":
                        g[pus]=g[pus]+content[lista[pos]]
                    if (lista[pos])[pus]=="W":
                        w[pus]=w[pus]+content[lista[pos]]
                    if (lista[pos])[pus]=="S":
                        s[pus]=s[pus]+content[lista[pos]]
                    if (lista[pos])[pus]=="X":
                        x[pus]=x[pus]+content[lista[pos]]
                    pus +=1
                pos+=1
                pus=0
            else:
                pos+=1
    out+= "A,"+ str(a).strip("[").strip("]") + "\n"
    out+= "T,"+ str(t).strip("[").strip("]") + "\n"
    out+= "C,"+ str(c).strip("[").strip("]") + "\n"
    out+= "G,"+ str(g).strip("[").strip("]") + "\n"
    out+= "W,"+ str(w).strip("[").strip("]") + "\n"
    out+= "S,"+ str(s).strip("[").strip("]") + "\n"
    out+= "X,"+ str(x).strip("[").strip("]") + "\n"
    
    fale=raw_input("Name the .csv file\n")
    f=open(str(fale)+'.csv','w')
    f.write(str(out))

#add genome names to the header of each sequence
#The "~" needed by coverM to calculate the species' abundance
f=open("/projects/afodor_research/ssun5/pangenome/pan_names.txt")
seq=f.readlines()
list1=map(str.strip, seq)

for bins in list1:
    bin_path="/projects/afodor_research/ssun5/pangenome/pangenome/"+bins+"_pan_1.fasta"
    with open (bin_path, "r") as myfile:
        lines=myfile.readlines() 
        for line in lines:
            if ">" in line:
                line1=">"+bins+"~"+line[1:]
                print(line1)
            else:
                print(line)

#map the genomes/pangenomes to the metagenome reads to calculate their abundance in each sample. 
f=open("/Users/shansun/Google Drive/China/wgs/bins/wgs_names.txt")
seq=f.readline()
seq=seq.strip("\n")
list1=seq.split(",")
a=[]
for i in range(10):
    
    output_name="/Users/shansun/Google Drive/China/wgs/bins/map_batch/pangenome/pangenome"+str(i)+".sh"    
    print("#!/bin/bash \n#PBS -l walltime=128:00:00\n#PBS -l procs=10\n#PBS -l mem=80GB\n#PBS -M ssun5@uncc.edu\n#PBS -m bea\n#PBS -q copperhead\ncd /users/ssun5/mash/", file=open(output_name,"w"))
    wgs_n=list1[(i*20):(i*20+20)]
    for wgs in wgs_n:
        r1="/projects/afodor_research/ssun5/china_bins/china_wgs1/"+wgs+"/"+wgs+"_350.nohost_R1.fq.gz"
        r2="/projects/afodor_research/ssun5/china_bins/china_wgs1/"+wgs+"/"+wgs+"_350.nohost_R2.fq.gz"
        line1="bwa mem  -t 10  /scratch/ssun5/pangenome/pangenomes.fa "+r1+" "+r2+" >/scratch/ssun5/pangenome/"+wgs+".sam"
        line2="samtools view -S -b /scratch/ssun5/pangenome/"+wgs+".sam -o /scratch/ssun5/pangenome/"+wgs+".bam"
        line3="samtools sort  /scratch/ssun5/pangenome/"+wgs+".bam  /scratch/ssun5/pangenome/"+wgs+"_sorted"
        line4="./coverm genome  -m relative_abundance mean trimmed_mean covered_fraction covered_bases variance -b  /scratch/ssun5/pangenome/"+wgs+"_sorted.bam -s '"'~'"' >/scratch/ssun5/pangenome/"+wgs+".tab"
        print(line1, file=open(output_name, "a"))
        print(line2, file=open(output_name, "a"))
        print(line3, file=open(output_name, "a"))
        print(line4, file=open(output_name, "a"))
        a.append(wgs)
            
                                         
i=10
output_name="/Users/shansun/Google Drive/China/wgs/bins/map_batch/pangenome/pangenome"+str(i)+".sh"    
print("#!/bin/bash \n#PBS -l walltime=128:00:00\n#PBS -l procs=10\n#PBS -l mem=80GB\n#PBS -M ssun5@uncc.edu\n#PBS -m bea\n#PBS -q copperhead\ncd /users/ssun5/mash/", file=open(output_name,"w"))
wgs_n=list1[200:214]

for wgs in wgs_n:
    r1="/projects/afodor_research/ssun5/china_bins/china_wgs1/"+wgs+"/"+wgs+"_350.nohost_R1.fq.gz"
    r2="/projects/afodor_research/ssun5/china_bins/china_wgs1/"+wgs+"/"+wgs+"_350.nohost_R2.fq.gz"
    line1="bwa mem  -t 10  /scratch/ssun5/pangenome/pangenomes.fa "+r1+" "+r2+" >/scratch/ssun5/pangenome/"+wgs+".sam"
    line2="samtools view -S -b /scratch/ssun5/pangenome/"+wgs+".sam -o /scratch/ssun5/pangenome/"+wgs+".bam"
    line3="samtools sort  /scratch/ssun5/pangenome/"+wgs+".bam  /scratch/ssun5/pangenome/"+wgs+"_sorted"
    line4="./coverm genome  -m relative_abundance mean trimmed_mean covered_fraction covered_bases variance -b  /scratch/ssun5/pangenome/"+wgs+"_sorted.bam -s '"'~'"' >/scratch/ssun5/pangenome/"+wgs+".tab"
    print(line1, file=open(output_name, "a"))
    print(line2, file=open(output_name, "a"))
    print(line3, file=open(output_name, "a"))
    print(line4, file=open(output_name, "a"))
    a.append(wgs)

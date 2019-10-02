#! usr/bin/python3
#generate batch assembly and bin scripts
f=open("/Users/Shan/Google Drive/China/wgs/wgs_list.txt")
seq=f.readline()
seq=seq.strip("\n")
list1=seq.split(sep=",")
i=1
for n in list1:
    output_name="/Users/Shan/Google Drive/China/wgs/assem_script/"+str(i)+"_1.sh"
    oname1="/projects/afodor_research/ssun5/china_wgs/meta/P101SC17080831_02_B6_3_result_20180523/01.CleanData/"+n+"/"+n+"_350.nohost.fq1.gz"
    oname2="/projects/afodor_research/ssun5/china_wgs/meta/P101SC17080831_02_B6_3_result_20180523/01.CleanData/"+n+"/"+n+"_350.nohost.fq2.gz"
    fname1="/scratch/ssun5/china_wgs1/"+n+"/"+n+"_350.nohost_R1.fq.gz"
    fname2="/scratch/ssun5/china_wgs1/"+n+"/"+n+"_350.nohost_R2.fq.gz"
    dname1="/scratch/ssun5/china_wgs1/"+n
    
    print("#!/bin/bash\n#PBS -l walltime=120:00:00\n#PBS -l procs=10\n#PBS -l mem=80GB\n#PBS -M ssun5@uncc.edu\n#PBS -m bea\n#PBS -q copperhead\n\n# Below here enter the commands to start your job.\n", file=open(output_name,"w"))
    print("mkdir /scratch/ssun5/china_wgs1/"+n, file=open(output_name, "a"))
    print("cp "+oname1+" "+fname1, file=open(output_name, "a"))
    print("cp "+oname2+" "+fname2, file=open(output_name, "a"))
    print("lfs migrate -c 2 "+fname1, file=open(output_name, "a"))
    print("lfs migrate -c 2 "+fname2, file=open(output_name, "a"))
    print("metaspades.py -1 "+fname1+" -2 "+fname2+" -o "+dname1+"/assembly/ -m 150", file=open(output_name, "a"))
    print("metabat2 -i "+dname1+"/assembly/contigs.fasta -o "+dname1+"/bins/bin -v -m 2000", file=open(output_name, "a"))
    print("checkm lineage_wf -f "+dname1+"/CheckM.txt -x fa -t 10 "+dname1+"/bins/ "+dname1+"/SCG", file=open(output_name, "a"))
    i=i+1
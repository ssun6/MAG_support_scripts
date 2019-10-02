#! usr/bin/python3
#print bins that doesnt pass the standard that completeness >50 and contamination <5
with open ("/Users/Shansun/all_CheckM.txt", "r") as myfile:
    for line in myfile:
        if "CheckM" in line:
            sample_n=line.split("/")[0]
        if "------" in line:
            continue
        if "bin." in line:
            list1=line.split()
            comp=float(list1[12])
            comt=float(list1[13])
            if comp <50 or comt>5:
                print("{}_{}.fa".format(sample_n, list1[0]))
                
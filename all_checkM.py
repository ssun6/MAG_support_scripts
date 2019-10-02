#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#! usr/bin/python3
#re-organize the files structure
with open ("/Users/shansun/Google Drive/bariatric/all_checkm.txt", "r") as myfile:
    for line in myfile:
        if "CheckM" in line:
            sample_n=line.split("/")[1]
        if "------" in line:
            continue
        if "bin." in line:
            line1=line
            list1=line1.split()
            print(sample_n+"_"+"\t".join(list1))
                

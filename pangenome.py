#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
df1 = pd.read_csv("/Users/shansun/Google Drive/China/wgs/bins/bin_info2.csv",index_col=0, header = 0,delimiter=",")
for n in df1["fastani_group"][1:].unique():
    sname=n.split("g__")[1].replace(";s_","_").replace(" ","_")
    print "mkdir /projects/afodor_research/ssun5/pangenome/cluster/"+sname  
    a="cp /projects/afodor_research/ssun5/pangenome/all_n/"+df1.loc[df1["fastani_group"]==n,].iloc[:,0]+".fa /projects/afodor_research/ssun5/pangenome/cluster/"+sname
    b=a.tolist()
    for i in b:
        print str(i)


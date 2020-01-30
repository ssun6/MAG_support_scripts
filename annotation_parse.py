#!/usr/bin/env python2
import os,sys
from collections import Counter
from time import sleep
import numpy as np
import pandas as pd

i=1
snames=[]
for file1 in os.listdir("/Users/shansun/Google Drive/China/wgs/bins/batch_fun/"):
    if file1.endswith(".annotations"):
        GOs=[]
        KOs=[]
        genes=[]
        K_dis={}
        snames.append(file1.split(".emapper")[0])
        with open (os.path.join("/Users/shansun/Google Drive/China/wgs/bins/batch_fun/", file1), "r") as f:  #open file
            lines = f.readlines() #read lines
            for line in lines:
                if line!="\n" and not line.startswith("#"):
                    genes.append(line.split("\t")[4])
                    GOs=GOs+line.split("\t")[5].split(",")
                    KOs=KOs+line.split("\t")[6].split(",")
                    for j in range(len(line.split("\t")[6].split(","))):
                        K_dis[line.split("\t")[6].split(",")[j]]=line.split("\t")[12].split(",")[0]

            GOs=filter(None, GOs)
            KOs=filter(None, KOs)
            genes=filter(None,genes)

            K_tab1=pd.DataFrame(Counter(KOs).items(), columns=['KEGG', 'Freq'])
            GO_tab1=pd.DataFrame(Counter(GOs).items(), columns=['GO', 'Freq'])
            gene_tab1=pd.DataFrame(Counter(genes).items(), columns=['gene', 'Freq'])
            
            if i==1:
                K_tab=K_tab1
                GO_tab=GO_tab1
                gene_tab=gene_tab1
            else:
                K_tab=K_tab.merge(K_tab1,left_on='KEGG',right_on='KEGG',how='outer', sort=True)
                GO_tab=GO_tab.merge(GO_tab1,left_on='GO',right_on='GO',how='outer', sort=True)
                gene_tab=gene_tab.merge(gene_tab1,left_on='gene',right_on='gene',how='outer', sort=True)
            
            i=i+1
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-50s] %d%%" % ('='*(i/22), i/11))
            sys.stdout.flush()
            sleep(0.25)
                
K_tab=pd.DataFrame(K_tab)
col_names=snames
col_names.insert(0,"KEGG")
K_tab.columns=col_names
K_tab.to_csv("/Users/shansun/Google Drive/China/wgs/bins/K_tab.csv", sep=',', header=True, index=False)

GO_tab=pd.DataFrame(GO_tab)
col_names[0]="GO"
GO_tab.columns=snames
GO_tab.to_csv("/Users/shansun/Google Drive/China/wgs/bins/GO_tab.csv", sep=',', header=True, index=False)

gene_tab=pd.DataFrame(gene_tab)
col_names[0]="Gene"
gene_tab.columns=col_names
gene_tab.to_csv("/Users/shansun/Google Drive/China/wgs/bins/gene_tab.csv", sep=',', header=True, index=False)

for keys,values in K_dis.items():
    K_dis[keys]=values.strip()

KEGG_annot=pd.DataFrame.from_dict(K_dis,orient='index').drop("")
KEGG_annot.to_csv("/Users/shansun/Google Drive/China/wgs/bins/KEGG_annotation.csv", sep=',', header=False, index=True)

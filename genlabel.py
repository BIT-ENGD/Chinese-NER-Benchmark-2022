import os
from dataset import *

data_path="data"





for dn in DATASET:
    label_path=os.path.join(data_path,dn,LABEL_FILE_NAME)
    alltags=set()
    for fn in DATASET[dn]:
     
        fullname=os.path.join(data_path,dn,fn)
        with open(fullname,"r") as f:
            for line in f:
                all=line.split()
                if(len(all)<2):
                    continue 
                else:
                    alltags.add(all[1])
    
    with open(label_path,"w") as f:
        for ln in alltags:
            f.writelines(ln.strip())
            f.write("\n")

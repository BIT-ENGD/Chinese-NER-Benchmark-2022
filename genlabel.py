import os
dataset={"MSRA":["train_dev.char.bmes","train_dev.char.bmes","test.char.bmes"],
        "People_Daily":["example.train","example.dev","example.test"],
        "ResumeNER":["train.char.bmes","dev.char.bmes","test.char.bmes"],
        "WeiboNER":["train.all.bmes","dev.all.bmes","test.all.bmes"]
}

data_path="data"
label_file="labels.char"




for dn in dataset:
    label_path=os.path.join(data_path,dn,label_file)
    alltags=set()
    for fn in dataset[dn]:
     
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

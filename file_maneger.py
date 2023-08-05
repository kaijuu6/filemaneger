#file maneger
#GUI tkinter
import os
import csv
import pprint

if __name__ == '__main__':
    inputname = "datafile_in/"
    outputname = "sort/"

    if not(os.path.exists(inputname)):
        os.mkdir(inputname)
        
    if not(os.path.exists(outputname)):
        os.mkdir(outputname)
        
    
    #define name as [:,1]
    allfile=[] 
    allfile.append(["name"])
    allfile[0].append("VSM_raw")
    allfile[0].append("VSM_MsMatch")
    allfile[0].append("MOKE")
    allfile[0].append("XRD")

    ## if you need newparameter makeprogram for it
    
    ## program restert method
    
    

    ####analize 

    ## name
    fname = os.listdir(inputname+".")
    #print(fname,len(fname))
    for i, name in enumerate(fname):
        allfile.append([name])
        with open(inputname+name) as f:
            reader = csv.reader(f)
            #print(type(reader))
            row = []
            for col in reader:
                row.append(col)
            print(row[0][0]=="Ver")
            if row[0][0]=="Ver":
                allfile[i+1].append(name)
            else:
                allfile[i+1].append("nofile")

        
    
    
    print(allfile)
    # for i, e in enumerate(list_1) :
    # if search_value in e :
    #     index_list.append(i)
    # print(fname.index("TXT"))

    


    ####end analise
    #open("file", mode='w')
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
    allfile.append(["filename"])
    allfile[0].append("dir")
    allfile[0].append("mesurement")
    #allfile[0].append("VSM_MsMatch")
    #allfile[0].append("MOKE")
    allfile[0].append("sanplename")
    allfile[0].append("date")
    allfile[0].append("anotherkey")
    

    ## if you need newparameter makeprogram for it
    
    ## program restert method
    
    

    ####analize 


    ## name
    #fname = os.walk(inputname+".")
    fname = os.listdir(inputname+".")
    
    #print(fname,type(fname))

    # for i, name in enumerate(fname):
    #     allfile.append([name])
    #     with open(inputname+name) as f:
    #         reader = csv.reader(f)
    #         #print(type(reader))
    #         row = []
    #         for col in reader:
    #             row.append(col)
    #         print(row[0][0]=="Ver")
    #         if row[0][0]=="Ver":
    #             allfile[i+1].append(1)
    #         else:
    #             allfile[i+1].append(0)

    #         if row[0][0]=="Sample\t":
    #             allfile[i+1].append(1)
    #         else:
    #             allfile[i+1].append(0)
    #         #print(row)

    #         #find samplename this process must be last
    #         if row[0][0]=="Ver":
    #             allfile[i+1].append(row[2][1])
    #         elif row[0][0]=="Sample\t":
    #             recname = row[2][0]
    #             barnum = row[2][0].index('-')
    #             # print(row[2][0],type(row[2][0]))
    #             # print(type(row[2][0].index('-')))
    #             # print(recname[barnum-1:barnum+9])
    #             allfile[i+1].append(recname[barnum-1:barnum+9])
    #         else:
    #             print("sample name is not found")

    # with open("attribute.csv", 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerows(allfile)

    linedata = []
    for dirs, subdirs, files in os.walk(inputname):
        print("ディレクトリ：", dirs)
        linedata = []
        for subdir in subdirs:
            print("内部のディレクトリ名：", subdir)
        for file in files:
            print("ファイル名：", file)
            print(dirs)
            linedata.append(file)
            linedata.append(dirs)
            val =input(file+"mesurementtype")
            linedata.append(val)
            print(linedata)
        print("===============")
        allfile.append(linedata)
    print(allfile)

    



        
    
    
    #print(allfile)


    # for i, e in enumerate(list_1) :
    # if search_value in e :
    #     index_list.append(i)
    # print(fname.index("TXT"))

    


    ####end analise
    #open("file", mode='w')
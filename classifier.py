import os
import shutil
from random import randint
from shutil import rmtree
import zipfile
import datetime

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def movefile(tdir,filename):
    pf=filename
    filename=filename.split("\\")[-1]
    temp=os.listdir(tdir)
    while filename in temp:
        ex=filename.split('.')[1]
        filename=filename.split('.')[0]+str(random_with_N_digits(4))+"."+ex
    os.rename(pf,filename)
    shutil.move(filename,tdir+"/"+filename)
        


def makedirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return 1
    else:
        return 0
        

def makereqdirs(directory):
    val=makedirectory(directory+"/Images_ext")
    val=makedirectory(directory+"/Docs_ext")
    val=makedirectory(directory+"/Excel_Sheets_ext")
    val=makedirectory(directory+"/PDFS_ext")
    val=makedirectory(directory+"/Textfiles_ext")
    val=makedirectory(directory+"/HTMLfiles_ext")
    val=makedirectory(directory+"/Coding_ext")
    val=makedirectory(directory+"/Videos_ext")
    val=makedirectory(directory+"/Presentations_ext")
    val=makedirectory(directory+"/Music_ext")
    val=makedirectory(directory+"/Extras_ext")

def makenewtlist(directory):
    tlist=os.listdir(directory)
    dirs=[]
    for i in range(len(tlist)):
        if '.' not in tlist[i]:
           dirs.append(tlist[i])

    for i in range(len(dirs)):
        for path, subdirs, files in os.walk(dirs[i]):
            for name in files:
                print(os.path.join(path,name))
                movefile(directory,os.path.join(path, name))
    
    tlist=os.listdir()
    return tlist
            
            

def deleteempty(directory):
    tlist=os.listdir(directory)
    for i in range(len(tlist)):
        if "." not in tlist[i]:
            if os.path.isdir(directory+"\\"+tlist[i]):
                length=len(os.listdir(directory+"\\"+tlist[i]))
                if length==0:
                    os.rmdir(directory+"\\"+tlist[i])
                
        
def classify(extensive,directory):
    start=os.listdir(directory)
    if extensive==0:
        tlist=os.listdir(directory)
    else:
        tlist=makenewtlist(directory)
    makereqdirs(directory)
    for i in range(len(tlist)):
        filename=tlist[i]
        if "." not in filename:
            continue
        extension=filename.split('.')[1]
        extension=extension.lower()
        filename=str(filename)
        if (extension=='jpeg' or extension=='jpg' or extension=='png' or extension=='bmp'):
            movefile(directory+"\Images_ext",directory+"\\"+filename)
        elif (extension=='doc' or extension=='docx'):
            movefile(directory+"\Docs_ext",directory+"\\"+filename)
        elif (extension=='xls' or extension=='xlsx'):
            movefile(directory+"\Excel_Sheets_ext",directory+"\\"+filename)
        elif (extension=='ppt' or extension=='pptx'):
            movefile(directory+"\Presentations_ext",directory+"\\"+filename)
        elif (extension=='pdf'):
            movefile(directory+"\PDFS_ext",directory+"\\"+filename)
        elif (extension=='txt'):
            movefile(directory+"\Textfiles_ext",directory+"\\"+filename)
        elif (extension=='htm' or extension=='html'):
            movefile(directory+"\HTMLfiles_ext",directory+"\\"+filename)
        elif filename=="extract.py":
            continue
        elif (extension=='cpp' or extension=='c' or extension=='java' or extension=='py' or extension=='js'):
            movefile(directory+"\Coding_ext",directory+"\\"+filename)
        elif (extension=='mp4'):
            movefile(directory+"\Videos_ext",directory+"\\"+filename)
        elif (extension=='mp3' or extension=="wav"):
            movefile(directory+"\Music_ext",directory+"\\"+filename)
        else:
            movefile(directory+"\Extras_ext",directory+"\\"+filename)

    deleteempty(directory)

  
def printlist(a):
    for i in range(len(a)):
        print(a[i])

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def backup(path,storepath):
    now = datetime.datetime.now()
    s=str(now.strftime("%Y_%m_%d %H_%M"))
    zipf = zipfile.ZipFile(storepath+"/BACKUP_"+s+".zip",'w', zipfile.ZIP_DEFLATED)
    zipdir(path, zipf)
    zipf.close()


def printhelp():
    h="\n    ----------------- \n"
    h=h+"\n    CLASSIFIER -- v 1.0\n\n"
    h=h+"\n    This Application will classify all your files and directories in defined directories for Images, Documents etc..\n"
    h=h+"\n    Method to run the classifier (type this in shell): python classifier.py classify pathofdirectory mode \n"
    h=h+"    Method to run the backup the classifier (type in shell) : python classify.py backup pathofdirectory destinationpath\n"
    h=h+"\n    mode is an integer either 0 or 1.\n    0 - Non-extensive mode (direcotries will not be touched, rest files will be classifeid)\n"
    h=h+"    1 - Extensive mode, all the directories will be opened and all files will be classified. This mode will take more time\n\n"
    h=h+"    Backup will be a zip file stored to defined location\n"
    h=h+"\n    ----------------- \n"
    print(h)
    
#classify(1,"C:/Users/LALIT ARORA/Desktop/plots1")
#backup("C:/Users/LALIT ARORA/Desktop/plots1","C:/Users/LALIT ARORA/Desktop")

def printreport(mode,directory):
    print("\n\n    ------------------------\n")
    print("        REPORT")
    if mode==0:
        print("    Mode Selected : Non Extensive\n")
    else:
        print("    Mode Selected : Extensive\n")
    print("    Directory Selected : "+str(directory))
    print("\n\n    ------------------------\n")
    
if __name__=="__main__":
    import sys
    arguments=sys.argv
    if len(arguments)==2 and arguments[1]=="help":
        printhelp()
    elif len(arguments)==4 and arguments[1]=="classify" and (arguments[3]=='0' or arguments[3]=='1'):
        directory=arguments[2]
        mode=int(arguments[3])
        classify(mode,directory)
        printreport(mode,directory)
    elif len(arguments)==4 and arguments[1]=="backup":
        fdir=arguments[2]
        tdir=arguments[3]
        backup(fdir,tdir)
    else:
        print("Invalid Command!")
    
    

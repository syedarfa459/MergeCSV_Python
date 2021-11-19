#!/usr/bin/python
import csv
import os
import fnmatch

SourcePath = '/mnt/landing/ptcl/edw/edwdev/tnl/jobs/Group_BTEQSLJM/FilestoUpload/datafiles/'
TargetPath = '/mnt/landing/ptcl/edw/edwdev/tnl/jobs/Group_BTEQSLJM/TgtFiles/proc/'

def output_csv(file):
    with open(file,'r') as getfile:
        content = csv.reader(getfile,delimiter=',')
        if content is not None:
            counter = 0
            for line in content:
                if counter == 0:
                    # print(f'Column names are {line}')
                    counter += 1
                else: 
                    with open(TargetPath + 'collected.txt','a') as merged:
                        writerobj = csv.writer(merged)
                        writerobj.writerow(line)
                        merged.close()
        print("Done...Locked!!")

def get_csv(csvdir):
    csvlist = []
    for filename in csvdir:
        # if filename.endswith('.csv'):
        if fnmatch.fnmatch(filename,'HOST03*'+'pmresult*'+'Counters*'+'*.csv'):
            csvlist.append(filename)
    return csvlist


if os.path.isfile(TargetPath + 'collected.txt'):
    os.remove(TargetPath + 'collected.txt')
csv_filesdir = os.listdir(SourcePath)
for file in get_csv(csv_filesdir):
    print(file)
    output_csv(SourcePath + file)


# for file in path:
#     if file:
#         myfile = 'datafiles/myfile1.csv'
#         read_csv(myfile)






                
            


import csv
import os
import fnmatch

#defined functions
def output_csv(filepath,filename):
    count = 0
    counter = 0
    file_list,file_number = [],[]
    if fnmatch.fnmatch(filename,'HOST03*'+'pmresult*'+'AJKNewCounters*'+'.csv'):
        file_number += [filename[19:44]]
        # print(file_number)
        file_list += [filename]
        # print(file_list)
        # print("HANNNNNNNNNNNNNNGGGGGGGGG")
        with open(filepath,'r') as getfile:
            content = csv.reader(getfile,delimiter=',')
            if content is not None:
                for line in content:
                    if count == 0:
                        # print(f'Column names are {line}')
                        count += 1
                    else:
                        with open('./CollectedData/collected_HOST03.txt','a',newline='') as merged:
                            writerobj = csv.writer(merged)
                            # print(line)
                            # print(filename)
                            line = line + file_list + file_number
                            # print(line)
                            # print('Hellllloooo')
                            # new_row = list(line.append('filename: '+filename))
                            writerobj.writerow(line)
                            # print("YAHAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
                            merged.close()
                            count += 1
                            # print("YAHAANNNNNNNNNNNNNNNNNNNNNNNNNNNNNN22222222222222")
                        
    elif fnmatch.fnmatch(filename,'History*'+'FTRMTR*'+'Counters*'+'*.csv'):
        file_list += [filename]
        file_number += [filename[43:60]]
        with open(filepath,'r') as getfile:
            newcontent = csv.reader(getfile,delimiter=',')
            if newcontent is not None:
                for newline in newcontent:
                    if counter == 0:
                        counter += 1
                    else:
                        with open('./CollectedData/collected_History.txt','a',newline='') as merged2:
                            writerobj2 = csv.writer(merged2)
                            newline = newline + file_list + file_number
                            writerobj2.writerow(newline)
                            merged2.close()
                            counter += 1
    print('Done!!')
    if count != 0:
        print("Total rows of file History_Performance_FTRMTR_BI_New_Counters inserted", count)
    if counter != 0:
        print("Total rows of HOST03_pmresult_AJKNewCountersFileHuaweiBI inserted", counter)

def get_csv(csvdir):
    csvlist = []
    csvlist2 = []
    for filename in csvdir:
        # if filename.endswith('.csv'):
        if fnmatch.fnmatch(filename,'HOST03*'+'pmresult*'+'AJKNewCounters*'+'*.csv'):
            csvlist.append(filename)
        elif fnmatch.fnmatch(filename,'History*'+'FTRMTR*'+'Counters*'+'*.csv'):
            csvlist2.append(filename)
    return csvlist,csvlist2


#main code
if os.path.isfile('./CollectedData/' + 'collected_History.txt'):
    os.remove('./CollectedData/' + 'collected_History.txt')
if os.path.isfile('./CollectedData/' + 'collected_HOST03.txt'):
    os.remove('./CollectedData/' + 'collected_HOST03.txt')

csv_filedir = os.listdir("./datafiles")

csv_lst1,csv_lst2 = get_csv(csv_filedir)

if csv_lst1:
    for filename in csv_lst1:
        print(filename)
        print(type(filename))
        output_csv('./datafiles/'+ filename,filename)

if csv_lst2:
    for filename in csv_lst2:
        print(filename)
        output_csv('./datafiles/'+ filename,filename)

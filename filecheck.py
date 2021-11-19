import os
import fnmatch
def get_csv(csvdir):
    csvlist = []
    for filename in csvdir:
        if fnmatch.fnmatch(filename,'HOST03*'+'pmresult*'+'Counters*'+'*.csv'):
            csvlist.append(filename)
    return csvlist

csv_filedir = os.listdir("./datafiles")
# get_csv(csv_filedir)

for file in get_csv(csv_filedir):
    print(file)

# for file in os.listdir('./datafiles'):
#     if fnmatch.fnmatch(file,'HOST03*'+'pmresult*'+'Counters*'+'*.csv'):
#         print(file)
#     else:
#         pass
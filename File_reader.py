#Python code to read CSV file and provid e output file in CSV

import csv
import os,sys

def isUnique(lis, value):
    if value in lis:
         return -1
    else:        
         lis.append(value)
         return 1
         
def open_output(file_name):
    with open(file_name,mode='w') as out_csv:
        csv_writer=csv.writer(out_csv, delimiter=',') 
        return csv_writer
         
#def writeInfile(row):
#    csv_writer = open_output(file_name)
#    csv_writer.writerow(row)

def openPath(path):
    try:
        files=os.listdir(path)
        return files
    except WindowsError:
        print 'Path is not valid. Please Check!!!'
         
#Main program Starts
print '******************************************************'
print '*                File Processing                     *'
print '******************************************************' 
print ' ' 
path=raw_input('Enter input folder path: ')
print path
checkForFiles=openPath(path)   
if checkForFiles:  
    file_name='test_out.csv'
    #csv_writer = open_output(file_name)
    #if csv_writer:
    #    print 'Output file ', file_name , 'is in use. Please do not open  the file.'
    #else:
    #    print 'issue in Output file ', file_name 
    
    lis=[]    
    tot_count=0
    for file in checkForFiles:
        path=path
        input_file=path+file        
        with open(input_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print 'Column names are ' , row
                    #writeInfile(row)
                    #csv_writer.writerow(row)
                    line_count += 1
                else:
                #print '\t ',  row[0] ,'works in the ' , row[1]
                    value=int(row[0])
                    print 'value:', value
                    isNotPresent=isUnique(lis, value)
                    #if isNotPresent:
                      #  writeInfile(row)
                      #  csv_writer.writerow(row)
                    line_count += 1
        csv_file.close()
        tot_count=tot_count + line_count
    print 'Processed ',  tot_count, 'lines.'
    print 'Number of lines wrote in output file:'
    print lis
else:
   print ' No files present in the Folder!!'







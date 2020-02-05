import csv
import glob

inputs = []  # etc
count = 0

for files in glob.glob('C:/Users/User/Desktop/FinalProject/backupCSVs/*E0.csv'):
    inputs.append(files)
    print files

#determine field names 
fieldnames = []
for filename in inputs:
  with open(filename, "r") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for h in headers:
      if h not in fieldnames:
        if len(h) > 0:
            fieldnames.append(h)
            count += 1
            print h

print fieldnames
#copy the data
with open("master.csv", "wb") as master:   
  writer = csv.DictWriter(master, fieldnames=fieldnames)
  print writer
  for filename in inputs:
    with open(filename, "r") as file:
      reader = csv.DictReader(file)  # Uses the field names in this file
      #print reader
      for line in reader:
        print filename
        #print line
        #break
        writer.writerow(line)
        
print count
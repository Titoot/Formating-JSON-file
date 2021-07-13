#to make sure that the code works
print("starting...")
#opens files
file2 = open("pass1.txt", "w")
with open("users_formated.txt", "r") as f:
    for line in f:
        #locate a word
        if "\"active\":\"1\"" in line:
            #finds it's index
            indx = line.find("mobile")
            #extacts the required part
            filter = line[indx + 8:indx + 23]
            #removes unnecessary (edit it with your needs)
            filter2 = filter.replace("\",", "")
            filter3 = filter2.replace("\"", "")
            filter4 = filter3.replace("n","")
            print(filter4)
            
            #writes to another file (with a linebreak)
            file2.write(filter4 + "\n")
            
            

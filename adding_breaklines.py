#to make sure that the code works
print("starting...")

with open("update/user21_active.txt", "r") as f:
        #reads the file
        lol = f.read()
        #puts a breakline
        #edit the replace with your need
        iii =  lol.replace("},{","},\n{")
        #opens a file to write on       
        f2 = open("update/user21_active_formated.txt", "w")
        #write to that file
        f2.write(iii)
 

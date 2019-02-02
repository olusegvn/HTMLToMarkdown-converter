#This python file converts HTML files to Markdown
import numpy as np
import os
import sys, re
import subprocess


#opening
print("_"*30 + "Convert HTML to Markdown" + "_"*30)


#impot html files
try:
    path_to_files = input("\n\nEnter path to html files : ")
    path_to_outfiles = input("Choose directory to place Markdown files : ")

    files = os.listdir(path_to_files)

except(OSError):
    print("Unable to find files in directory : {0}".format(path_to_files))



#declare substitution array 
sub_array = [["<p>", "\n"], ["</p>", "\n"], ["<br>", "\n"],
            ["<strong><em>","***"], ["</em></strong>", "***"],
            ["<strong>", "**"], ["</strong>", "**"],["<ul>", ""],            
            ["<em>", "*"], ["</em>", "*"],["<li>","\n- "],
            ["</li>","\n"],["<code>","``"],["</code>", "``"]    
            ]

i=1
#append header files (eg h1) to array
for i in range(11):
    header = "<h"+ str(i) +">"
    htag = "#"*i
    sub_array.append([header, htag])


#append end of header tags
for i in range(11):
    header = "</h"+ str(i) +">"
    htag = "#"*i
    sub_array.append([header, "\n"])




#open and repair each file

#open the file
#try used to catch errors while opening the files
try:
    status = "Files successfully converted !!!" 
    for file in files:
        filename = path_to_files + "/"+ file

        #to pick only html files
        if  file.endswith("html"):
                
            #print (filename)
            infile = open(filename, "r")
            print ("\n\nOpening {0} ...".format(file)  )
            print("\nworking on file ...")
            text = infile.read()
            i = 0
            
            #substitute html characters in the file according to the substitution array
            for i in range(len(sub_array)): 

                r = re.compile(sub_array[i][0])
               # print  (sub_array[i][0])
                repl = str(sub_array[i][1])    
               # print (repl)        
                outtext, count = re.subn(r,repl,text )
                text = outtext
               # print(outtext)
            print("\n" + file + " successfully repaired !!!")

            #close file
            infile.close()

            #print output file
            Check = input("print output ?(y/n)")
            check = Check.lower()
            if check == "y":     
                print ("\n\nOutput for {0}: \n".format(file))
                print (outtext)
            

            #write substituted text to new file
            outfile_name = "Repaired"+file+".txt"
            outfile = path_to_outfiles+"/"+outfile_name
            Outfile = open(outfile, "w")
            Outfile.write(text)
            Outfile.close()

#catch permission errors
except(PermissionError):
    print("\n\nPermission to read {0} denied .".format(file))
    status = "Sorry, Conversion was unsuccessfull."
   

except(NameError):
    status = "Sorry, Conversion was unsuccessful."
    pass
    

    
#finally ..
finally :
    print("\n\n"+ status)
    print("\n\nfor more amazing scripts : IG: iamcoder_o, Github: olusegvn")
    
    

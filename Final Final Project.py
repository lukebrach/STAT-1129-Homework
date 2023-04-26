#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import string

class Cooccurrence:
    def __init__(self, filename, *args):
        self.filename = filename
        self.listofwords = []
        if args:
            self.searchwords = args
        else:
            self.searchwords = []
        self.preprocessed = False

    def read_file(self):
        try:
            with open(self.filename) as fileopen:
                filelist = fileopen.readlines()
        except FileNotFoundError:                    #Backup if File Doesnt Exist
            print("File does not exist")
            return []

        return filelist

    def preprocess_text(self, filelist):
        data_dict = {}
        for i in range(len(filelist)):
            sentence = filelist[i]
            filelist[i] = ''.join(c for c in filelist[i] if c.isalpha() or c.isspace()) #removing puntuation
            filelist[i] = filelist[i].lower()
            filelist[i] = filelist[i].replace("\n", '')
            lineposition = i + 1
            for x in filelist[i]:
                splitlist = re.split(r' ', filelist[i])
                for y in splitlist:
                    if y in self.listofwords:
                        if lineposition in data_dict[y]:
                            continue
                        else:
                            data_dict[y].append(lineposition)
                    else:
                        data_dict.update({y: [lineposition]})
                        self.listofwords.append(y)

        self.preprocessed = True
        return data_dict

    def search_words(self, data_dict):
        found_lines = []
        for p in self.searchwords:
            p = p.lower().replace("'", "")  # Convert to lowercase and remove apostrophes
            if p in data_dict:
                print(p, " occurs in lines: ", data_dict[p])
                found_lines.append(set(data_dict[p])) #these are the values from the dictionary
            else:
                print(p, " does not occur in the file")
                found_lines.append(set())

        common_lines = set.intersection(*found_lines) #determines which lines are shared from the dictionary
        if len(common_lines) > 0:
            print("The words", ", ".join(self.searchwords), "occur together in lines: ", common_lines)
        else:
            print("The words", ", ".join(self.searchwords), "do not occur together in any line.")

    def main(self):
        if not self.searchwords:
            print("You must provide a valid file name and words") #If Class is left empty
            return

        filelist = self.read_file()
        if not filelist:
            return

        data_dict = self.preprocess_text(filelist)
        self.search_words(data_dict)


# In[2]:


#Test 1
test1a=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","the")
test1a.main()
print()
test1b=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","the","is")
test1b.main()
print()
test1c=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","true","knowledge","imagination")
test1c.main()


# In[3]:


#Test 2
test2a=Cooccurrence("xxxxx")
test2a.main()
print()
test2b=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","The")
test2b.main()
print()
test2c=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","can't")
test2c.main()
print()
test2d=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","nature")
test2d.main()
print()
test2e=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","can't")
test2e.main()
print()
test2f=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","cat")
test2f.main()
print()
test2g=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt")
test2g.main()


# In[4]:


#Test 3
test3a=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/gettysburg.txt","nation")
test3a.main()
print()
test3b=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/gettysburg.txt","here","dead")
test3b.main()
print()
test3c=Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/gettysburg.txt","It","is")
test3c.main()


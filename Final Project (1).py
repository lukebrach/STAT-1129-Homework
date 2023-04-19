#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:





# In[29]:


class Child:
    def __init__(self,filename,*args):
        self.filename=filename
        self.words= args
    def welcome(self):
        print(self.words)

test=Child("amogus.txt"," the ", " moon ", " is ", " made ", " of "," cheese ")
test.welcome()


# In[84]:


class coocerrence:
    def __init__(self,filename,*args):
        self.filename=filename
        self.words= args
    def fileopener(self):
        import string
        try:
            filestring=[]
            fileopen=open(self.filename)
            for x in fileopen:
                filestring.append(x)
            return filestring
        except:
            print("File Does Not Exist")
        

test=coocerrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt"," the ", " moon ", " is ", " made ", " of "," cheese ")
test.fileopener()
string=test.fileopener()
len(string)


# In[96]:


class coocerrence:
    def __init__(self,filename,*args):
        self.filename=filename
        self.words= args
    def fileopener(self):
        import string
        try:
            filelist=[]
            fileopen=open(self.filename)
            for x in fileopen:
                filelist.append(x)
       # except:
           # print("File Does Not Exist")
    #def preprocessing(self):
      #  self.fileopener()
            translator = str.maketrans('','',string.punctuation + string.digits)
            for i in range(len(filelist)):
                sentence=filelist[i]
                sentence=sentence.replace("-",'').replace("''",'')
                sentence = sentence.translate(translator)
                sentence=sentence.lower()
                filelist[i]=sentence
            return filelist
        except:
            print("there is an error")
test=coocerrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt"," the ", " moon ", " is ", " made ", " of "," cheese ")
test.fileopener()


# In[193]:


class coocerrence:
    def __init__(self,filename,*args):
        self.filename=filename
        self.words= args
    def fileopener(self):
        import re
        import string
        try:
            #dataframe==read_file("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt")
            filelist=[]
            listofwords=[]
            fileopen=open(self.filename)
            for x in fileopen:
                filelist.append(x)
       # except:
           # print("File Does Not Exist")
    #def preprocessing(self):
      #  self.fileopener()
            #translator = str.maketrans('','',string.punctuation + string.digits)
            Data_Dict={}
            for i in range(len(filelist)):
                sentence=filelist[i]
                filelist[i]=''.join(c for c in filelist[i] if c.isalpha() or c.isspace())
                filelist[i]=filelist[i].lower()
                filelist[i]=filelist[i].replace("\n",'')
                lineposition=i+1
                for x in filelist[i]:
                    splitlist=re.split(r' ',filelist[i])
                    for y in splitlist:
                        #listofwords.append(y)
                        if y in listofwords:
                            #Data_Dict[y].append(i)
                            continue
                        else:
                            Data_Dict.update({y:[lineposition]})
                            listofwords.append(y)
                    #res=[*set(Data_Dict.values)]
            return Data_Dict
        except:
            print("there is an error")
test=coocerrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt"," the ", " moon ", " is ", " made ", " of "," cheese ")
test.fileopener()


# In[208]:


import re
import string

class Cooccurrence:
    def __init__(self, filename,*args):
        self.filename = filename
        self.listofwords = []
        self.searchwords=args

    def fileopener(self):
        try:
            filelist = []
            with open(self.filename) as fileopen:
                for line in fileopen:
                    filelist.append(line)
            #self.preprocessing(filelist)
    #def preprocessing(self, filelist):
            data_dict = {}
            for i in range(len(filelist)):
                sentence = filelist[i]
                filelist[i] = ''.join(c for c in filelist[i] if c.isalpha() or c.isspace())
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
        except FileNotFoundError:
            print("File does not exist")
        for p in self.searchwords:
            print(p, " occurs in lines: ",data_dict[p])

test = Cooccurrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt","the","blame")
test.fileopener()


# In[82]:


#I have no idea what I f*cked up here
class coocerrence:
    def __init__(self,filename,*args):
        self.filename=filename
        self.words= args
    def fileopener(self):
        import string
        try:
            filelist=[]
            fileopen=open(self.filename)
            for x in fileopen:
                filelist.append(x)
            return filelist #This output is a list of every line in the file
        except:
            print("File Does Not Exist")
    def preprocessing(self):
        try:
            lowercasefilelist=[]
            for x in filelist:
                xlower=x.lower()
                lowercasefilelist.append(xlower)
            return lowercasefilelist
        except:
            print("Error with lowercase")

test=coocerrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt"," the ", " moon ", " is ", " made ", " of "," cheese ")
test.fileopener


# In[83]:


class coocerrence:
    def __init__(self,filename,*args):
        self.filename=filename
        self.words= args
    def fileopener(self):
        import string
        try:
            filestring=[]
            fileopen=open_file(self.filename)
            filedata=read_data(self.filename)
            print(filedata)
        except:
            print("File Does Not Exist")
            
test=coocerrence("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Final-project/Final-project/einstein.txt"," the ", " moon ", " is ", " made ", " of "," cheese ")
string=test.fileopener()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


import urllib.request


# In[3]:


import argparse


# In[4]:


import re
from collections import Counter
import datetime 


# In[5]:


def downloadData(url):
    # print("download data")
    filename='week3_logfile.csv'
    urllib.request.urlretrieve(url,filename)
    # print(url)
    return filename


# In[6]:



# process data with error log
def processData(filename):  
    data=[]
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


# In[7]:




# Check requests for image percentage wise
def getFileInfo(data):
    count=0
    for item in data:
        found = re.findall(r'([-\w]+\.(?:JPEG|GIF|PNG|JPG|jpeg|jpg|gif|png))', item[0])
        if len(found) and int(item[3]) == 200 :
            count += 1
    print("Image requests account for " +str(count/len(data) *100)+ "%  of all requests")


# In[8]:



# Extra Credit
def hourInfo(data):
    Time = Counter()
    for item in data:
        tim = datetime.datetime.strptime(str(item[1]),'%Y-%m-%d  %H:%M:%S')
        if int(item[3]) == 200:
            Time[str(tim.hour)]+=1
    for k, v in sorted(Time.most_common()):
        print("Hour "+ str(k)+" has "+ str(v)+" hits")  


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help='please enter url')
    args = parser.parse_args()
    # print(args.url)
    if args.url != None:
        try:
            # print("start")
            csvFileName = downloadData(args.url)
            # print(input("Enter a valid number: "))
            data = processData(csvFileName)
            getFileInfo(data)
            popularBrowser(data)
            hourInfo(data)
           
        except:
            print("something happened wrong!")

    else:
        print("Exit")
        parser.exit() 

if __name__ == "__main__":
    main() 


# In[ ]:





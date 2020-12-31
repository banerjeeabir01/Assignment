import threading 
#this is for python 3.0 and above.
from threading import*
import time
import json

d={} #'d' is the dictionary in which we store data                                
try:
    
    with open('sample.json') as json_file:
        d = json.load(json_file)                                    #" this is "sample.json"..  the Json file- database
except:
    with open("sample.json", "w") as json_file:
        
        json.dump(d,json_file)  


#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    try:
        with open('sample.json') as json_file:
            d = json.load(json_file)
    except:
        with open("sample.json", "w") as json_file:
            json.dump(d,json_file)   
        
    if key in d:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jsonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
                print("Key-Value pair Created and SAVED in JSON FILE")
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3
    with open("sample.json", "w") as json_file:
        json.dump(d, json_file) 
#for read operation
#use syntax "read(key_name)"
            
def read(key):
    with open('sample.json') as json_file: 
        d = json.load(json_file)
    
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JsonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri
    with open("sample.json", "w") as json_file:
        json.dump(d, json_file)

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    with open('sample.json') as json_file: 
        d = json.load(json_file)
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted from JSON FILE")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")

    
    with open("sample.json", "w") as json_file:
        json.dump(d, json_file)



#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,value):
    with open('sample.json') as json_file: 
        d = json.load(json_file)
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
                print("Key-Value Pair modified");
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
            print("Key-Value Pair modified");
    with open("sample.json", "w") as json_file:
        json.dump(d, json_file)
print("DATASTORE\n Choose the option")


while(1):
    print("\n1.Create(TIME TO LIVE Duration optional) 2.Read  3. Delete 4.Modify 5.EXIT()\n")
   
    
    n=input()
    if(n=="1"):
        print("enter key and value(separated by space)and TIME TO LIVE Duration optional example: India 5")
        a=list(map(str,input().split()))
      
        if(len(a)==3):
            key=a[0]
            value=a[1]
            timeout=a[2]
            create(key,int(value),int(timeout))
        else:
            key=a[0]
            value=a[1]
            create(key,int(value))
            
        

    elif(n=="2"):
       
        print("enter key to READ (example:","India)")
        print(read(input()))
        
    elif(n=="3"):
        print("enter key to DELETE (example:","India)")
        delete(input())
    elif(n=="4"):
       
        print("enter key and value(separated by space)example:","India 5")
        key,value,=map(str,input().split())
        
        modify(key,int(value))
        
    elif(n=="5"):
        break
    else:
        print("ENTER THE CORRECT CHOICE")
        

    
    
    
          
          
          



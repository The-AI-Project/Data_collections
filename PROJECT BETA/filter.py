from bs4 import BeautifulSoup
from json import loads,dumps
from time import sleep
global jqueryx
jqueryx={
}
listing=[]

def jfiling(listx,inc):
    print(inc)
    listing.extend(listx)
    print(listing)
    return(listing)
    
    pass
def Merge(dict1, dict2):
    res = dict1 | dict2
    return res
def wr():
    file=open("C:\\Users\\hp\\Desktop\\PROJECT BETA\\selfstudy.com\\dataset.json","r+")
    print(file)
    dta=loads(file.read())
    jque=Merge(dta,jqueryx)
    file.close()
    file=open("C:\\Users\\hp\\Desktop\\PROJECT BETA\\selfstudy.com\\dataset.json","w")
    file.write(dumps(jque))
    file.close()
def fixer(val,nval):
    #["question num","question","optionA","optionB","optionC","optionD","src"]
    val[1]=val[1]+" "+val[2]
    val[2]=val[3]
    val[4]=val[5]
    val[5]=nval
    #print(f"fron here {val}")
    return val
    pass
def Filter(mock):
    inc=0
    print(f"working on mock test {mock}....")
    jstring={}
    num=0
    #jstring[f"test{num}"]=[
    #                       {
    #                           f"Question{i}":["question","optionA","optionB","optionC","optionD","src"],
    #                           f"Question{i}":["question","optionA","optionB","optionC","optionD","src"]
    #                       }
    #                   ]
    with open("dataa.html","r",encoding='utf-8') as file:
        data=file.read()
        file.close()
    soup = BeautifulSoup(data, 'html5lib')
    #HERE WE SEPERATED ONLY QUIZ FORM PART
    for hit in soup.findAll(attrs={'id' : 'quiz'}):
        pass
    xhit=str(hit)
    jquery={}
    soup = BeautifulSoup(xhit,features="html.parser")
    #THIS IS A PRALLEL STP TO FIND WHICH QUESTION IS HAVING THE IMG
    for para in soup.find_all('p'):
        img = para.find('img')
        if img:
            ques = para.find_previous('li').find('h6').text.strip()
            jquery[ques]=img['src']
            print(jquery)
            print(f"Image detected in question {ques}: {img['src']}")
    
    #HERE WE SEPERATING TEXT PART BY SKIPPING THE GIVEN TAGS DATA
    #what we learn:
    #different way to write loop
    #[s.exxtract() for s in soup(['style', 'script', '[document]', 'head', 'title','span'])]
    for s in soup(['style', 'script', '[document]', 'head', 'title','span']):
        s.extract() 
    visible_text = soup.getText()
    i=0
    what=["question num","question","optionA","optionB","optionC","optionD","src"]#the it is n
    pr_what=["Question","question","optionA","optionB","optionC","optionD","src"]#if its n+1
    valx=visible_text.split("\n")
    cm=(len(valx))
    inc=1
    
    jqueryx[f"Test_{mock}"]={}
    print(jquery)
    sleep(2)
    for item in range(0,cm):
        char=valx[item].splitlines()
        if('Submit Test' in char  ):
            print("found")
            char=""
        if(len(char)!=0 and char!="Submit Test"):#we need two list parallel to flow
            
            if(i==6):
                pr_what=what
                if( what[0] in jquery):#inserted img src
                    what[6]=(jquery[what[0]]) 
                    #print(what)
                    i=0
                
                else:
                    what[6]=None
                    listing=jfiling(what,inc)
                    inc+=1
                    
                    i=0
            what[i]=char[0]
            if(what[0].startswith("Question")==False):
                #we will do shifting till we get true
                pr_what=fixer(pr_what,what[0])
                i-=1
                
            
            i+=1
            
        else:
            pass
       # sleep(0.05)
    #for item in visible_text.split("\n"):
        #print(item)
    jqueryx[f"Test_{mock}"]=listing
    wr()
    listing=[]
    inc=0
    sleep(5)
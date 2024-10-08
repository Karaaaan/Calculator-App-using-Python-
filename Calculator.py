print("-------------------------CALCULATOR VERSION 1-------------------------------------")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. FORMULAE")
mode=True
add=True
addList=[]
subList=[]
mulList=[]
divList=[]
def addiTion():
    print("ADDITION")
    addList.clear()
    while(add):
        
        number=int(input("ENTER NUMBER"))
        addList.append(number)
        question=input("Add Y/N")
        if(question.lower()=='y'):
            
            print("ADDITION EQUALS "+str(sum(addList)))
            ask=input("DO YOU WANT TO GO BACK ? Y/N")
            if(ask.lower()=='y'):
                break
                




def subTraction():
    print("SUBTRACTION")
    subList.clear()
    while True:
        number=int(input("ENTER NUMBER"))
        subList.append(number)
        question=input("Sub Y/N")
        if(question.lower()=='y'):
            print(subList)
            sub=subList[0]
            for number in range(1,len(subList)):
                sub=sub-subList[number]
                
            print("SUBTRACTION EQUALS "+str(sub))
            ask=input("DO YOU WANT TO GO BACK ? Y/N")
            if(ask.lower()=='y'):
                break


def multiplication():
    print("MULTIPLICATION")
    mulList.clear()
    while True:
        
        number=int(input("ENTER NUMBER"))
        mulList.append(number)
        question=input("Multiply Y/N")
        if(question.lower()=='y'):
            mul=mulList[0]
            for number in range(1,len(mulList)):
                mul=mul*mulList[number]
            
            print("MULTIPLICATION EQUALS "+str(mul))
            ask=input("DO YOU WANT TO GO BACK ? Y/N")
            if(ask.lower()=='y'):
                break
def diviSion():
    print("DIVISION")
    divList.clear()
    while True:
        
        number=int(input("ENTER NUMBER"))
        divList.append(number)
        question=input("DIVIDE Y/N")
        if(question.lower()=='y'):
            div=divList[0]
            for number in range(1,len(divList)):
                div=divList[number]/div
            
            print("DIVISION EQUALS "+str(div))
            ask=input("DO YOU WANT TO GO BACK ? Y/N")
            if(ask.lower()=='y'):
                break
while(mode):
    n1=int(input("ENTER A NUMBER"))
    if(n1==1):
        addiTion()
    elif(n1==2):
         subTraction()
    elif(n1==3):
         multiplication()
    elif(n1==4):
        diviSion()
    






    

import requests
import re
import pandas as pd
import xlwt
from xlwt import Workbook

def fetch_result(seatNo,Mname):
    r = requests.post(${endpoint})
    try:
        return re.search('GPA :- (.*) MANDATORY AUDIT COURSE NOT COMPLETED', r.text).group(1)
    except:
        try:
            return re.search('GPA :- (.*) </td></tr><tr><td></td><td></td><td align=\'LEFT\'></td></tr><tr><td align=\'LEFT\' colspan=9>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;RESULT DATE : Oct 2022', r.text).group(1)
        except: 
            #print(seatNo,Mname, end=" ")
            return "--"

def gen_all_result():
    workbook = pd.read_excel('test.xlsx', usecols = 'A:C')
    workbook.head()
    #print(workbook)
    seatNo = workbook['seat'].tolist()
    Mname = workbook['mname'].tolist()
    Uname = workbook['uname'].tolist()
    max=0
    min=10
    mpos=0
    pos=0

    # Workbook is created
    wb = Workbook()
  
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    for i in range(0,len(seatNo)):
        x = fetch_result(seatNo[i],Mname[i])
        if x=="--":
            continue
        marks = float(x)
        sheet1.write(i, 0, Uname[i])
        sheet1.write(i, 1, marks)
        if marks>max:
            max=marks
            pos=i
        if marks<min:
            min=marks
            mpos=i
        print(max,min)

    #print(Uname[pos],max)
    #print(Uname[mpos],min)
    wb.save('final.xlsx')

def get_sm(roll):
    workbook = pd.read_excel('result.xlsx', usecols = 'B:F')
    workbook.head()
    #print(workbook)
    rollNo = workbook['Roll No'].tolist()
    seatNo = workbook['SeatNo'].tolist()
    Mname = workbook['Mother'].tolist()
    Uname = workbook['Student Name'].tolist()
    prn = workbook['PRN'].tolist()
    print(prn)
    try:    
        index = rollNo.index(roll)
        print(roll,Uname[index],end=" = ")
        print(fetch_result(seatNo[index],Mname[index]),"GPA")
    except:
        print("RollNo not found!")

#def gen_all_dob():
    

def menu():
    print("Choose an automation:")
    print("1. Check your GPA")
    print("2. Create SGPA Excel")
    print("3. Check DOB")
    print("4. Create DOB Excel")
    print("5. Exit")
    n=1
    while n!=5:
        n=input("Choice: ")
        if n.isnumeric()==True:
            n = int(n)
            if n==1:
                roll=1
                while roll:
                    roll = input("Enter RollNo:")
                    if roll.isnumeric()==True:
                        roll = int(roll)
                        get_sm(roll)
                    else:
                        print("Invalid Input")
            elif n==2:
                gen_all_result()
            elif n==3:
                print("Enter RegistrationNo:",end=" ")
                regno = input()
            #elif n==4:
                #gen_all_dob()
            elif n==5:
                exit()
            else:
                print("INVALID CHOICE")
        else:
            print("INTEGER VALUE please!")




  





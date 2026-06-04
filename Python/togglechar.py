#take user input
String = 'GuDDuBHaiyA'
#initialize other empty String
String1 = str()
#iterate through String
for i in String:
    #check the case of each iterator
    if i.isupper():
        #change it to opposit case
        i = i.lower()
        #Concat each iterator to String1
        String1 = String1 + i
    else:
        i = i.upper()
        String1 = String1 + i
#print String1
print(String + ' after changing ' + String1)

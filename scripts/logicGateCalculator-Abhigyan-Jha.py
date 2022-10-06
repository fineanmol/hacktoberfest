#AI LAB 1:MAKE LOGIC GATE CALCULATOR IN PYTHON

print("Logic Gate Calculator");
def AND (a,b):
 a=int(a)
 b=int(b)
 if a==1 and b==1:
    return 1;
 else:
   return 0

def OR (a,b):
 a=int(a)
 b=int(b)
 if a==1:
  return 1;
 elif b==1:
  return 1
 else:
  return 0

def XOR(a,b):
 a=int(a)
 b=int(b)
 if a==1 and b==0:
  return 1
 elif a==1 and b==1:
  return 0
 elif a==0 and b==1:
  return 1
 elif a==0 and b==0:
  return 0
  
if __name__=="__main__":
 a=input("Enter a => ")
 b=input("enter b => ")
 c=input("Enter Operand =>  ")
 if c =="AND":
  print("RESULT => ",AND(a,b))
 elif c=="OR":
  print("RESULT => ",OR(a,b)) 
 elif c=="XOR":
  print("RESULT => ",XOR(a,b))
  
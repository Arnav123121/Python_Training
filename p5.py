# Removing spaces from the string:

#1. rstrip()===>To remove spaces at right hand side

#2. 1strip()===>To remove spaces at left hand side

#3. strip() ==>To remove spaces both sides

city=input("Enter your city Name:")

scity=city.strip()

if scity== 'Hyderabad':

    print("Hello Hyderbadi..Adab")

elif scity== 'Chennai':

    print("Hello Madrasi...Vanakkam")

elif scity=="Bangalore":

    print("Hello Kannadiga... Shubhodaya")
    
else:
    print("your entered city is invalid")
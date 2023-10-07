print ("Hello")
name=input ("Enter your first name PLZ : ")
family=input ("Enter your last name PLZ : ")
S1 = float(input("Enter Your First Score: "))
S2 = float(input("Enter Your Second Score: "))
S3 = float(input("Enter Your Third Score: "))

avg = (S1+S2+S3)/3
print ("Average :", avg )

if (avg >= 17) :
    print ("Dear",name,family,"Your Average Is Great")

elif (17 > avg >= 12):
    print ("Dear",name,family,"Your Average Is Normal")

elif (avg < 12):
    print ("Dear",name,family,"You Have Failed, Try Harder")

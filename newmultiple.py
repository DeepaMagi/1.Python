class MultipleFunctions:
    #Dispaying different fields
    def Subfields():
        list=['Machine Learning','Neural Networks','Computer Vision','Robotics','Speech Processing','Natural Language Processing']
        for i in list:
            print(i)
            
    #Finding Even and Odd number
    def oddEven():
        number=int(input("Enter a number:"))
        if(number%2==0):
            print(number,"is even")
        else:
            print(number, "is odd")
        
    #Checking for eligibility for marriage
    def Eligible():
        gender=input("Your Gender: ")
        age=int(input("Your age: "))
        if((gender=="Female") and (age>=18) or(gender=="Male") and (age>=21)):
            print("Eliglble for Marriage")
        else:
            print("Not Eligible for Marriage")
            
    #Finding percentage of 10th marklist
    def percentage(subject1,subject2,subject3,subject4,subject5):
        total=(subject1+subject2+subject3+subject4+subject5)
        average=total/5
        lst=[subject1,subject2,subject3,subject4,subject5]                   
        for x in lst:            
            print(x)
        print("Total: ",total)
        print("Percentage:",average)
        
    #Finding Area and perimeter for two different triangles    
    def triangle1(height,breadth):
        print("Area of a triangle:",(height*breadth)/2)
    def triangle2(height1,height2,breadth):
        print("Perimeter of triangle:",(height1+height2)+breadth)
    
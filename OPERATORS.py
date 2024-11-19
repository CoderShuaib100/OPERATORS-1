print("The maximum marks is 100")
maths = int(input("Enter your Maths Marks: "))
tamil = int(input("Enter your Tamil Marks: "))
english = int(input("Enter your English Marks: "))
science = int(input("Enter your Science Marks: "))
social = int(input("Enter your Social Marks: "))
hindi = int(input("Enter your Hindi Marks: "))
gk = int(input("Enter your GK Marks: "))

sum = maths + tamil + english + science + social + hindi + gk

avg = sum // 8

print("The average of the subjects is",avg)

percent = avg * 100

print("The percentage of the marks scored in your subjects is",percent)
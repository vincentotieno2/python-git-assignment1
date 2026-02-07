marks=int(input("Enter your marks:"))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
else:
    print("Fail")

leads=[120,450,90,800]
qualified=[]
for lead in leads:
    if lead>=300:
        qualified.append(lead)
    print(qualified)
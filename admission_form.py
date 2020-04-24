from tkinter import *
# from tkinter import tkk
root=Tk()
root.configure(bg="black")
Label(root, text="Fitness Club", font="lucida 30 bold italic", fg="blue", bg="black").grid()
def done():
    print("Submitting The Form.")
    with open("data.txt", "a") as s:
        s.write("Fitness Club")
        a=user1.get("First_Name").get()
        s.write(F"\nFirst Name:{a}\n")
        b=user1.get("Last_Name").get()
        s.write(f"Last Name:{b}\n")
        c=user2.get("Current_weight").get()
        s.write(f"Current Weight:{c}\n")
        d=user2.get("Height").get()
        s.write(f"Height:{d}\n")
        e=user2.get("BMI").get()
        s.write(f"Body Mass Index:{e}\n")
        f=user2.get("Age").get()
        s.write(f"Age:{f}\n")
        g=user2.get("Goal_Weight").get()
        s.write(f"Goal Weight:{g}\n")
        h=user3.get("Current_Street_Address").get()
        s.write(f"Current Address:{h}\n")
        i=user3.get("Permanent_Street_Address").get()
        s.write(f"Permanent Address:{i}\n")
        j=user3.get("City").get()
        s.write(f"City:{j}\n")
        k=user3.get("State").get()
        s.write(f"State:{k}\n")
        l=user3.get("Postal").get()
        s.write(f"Postal Code:{l}\n")
        m=user4.get("Area_code").get()
        s.write(f"Area Code:{m}\n")
        n=user4.get("Phone_no").get()
        s.write(f"Phone Number:{n}\n")
        o=user4.get("Emergency_contact").get()
        s.write(f"Emergency Contact:{o}\n")
        p=user4.get("Relationship").get()
        s.write(f"Relationship:{p}\n")
        q=user4.get("E-Mail").get()
        s.write(f"E-Mail:{q}\n")
        r=suggestion_value.get()
        if suggestion_value.get()==1:
            s.write(f"Read terms and condition:No\n")
        else:
            s.write(f"Read terms and condition:Yes\n")
root.geometry("650x550")
#Student Details
f1=LabelFrame(root, text="Full Name", bg="black", fg="white")
f1.grid(row=1, column=0, sticky=W)
# f1.pack(fill=X, anchor=W)
l1=["First Name", "Last Name"]
for i in range(len(l1)):
    cur_label="l1" + str(i)
    cur_label=Label(f1, text=l1[i], bg="black", fg="white")
    cur_label.grid(row=i, column=0)
name_var=StringVar()
user1={
    "First_Name":StringVar(),
    "Last_Name":StringVar()
}
count=0
for i in user1:
    cur_entry="entry" + i
    cur_entry=Entry(f1, width=93, textvariable=user1[i])
    cur_entry.grid(row=count, column=1)
    count+=1
#Basic Details
f2=LabelFrame(root, text="Basic Details", bg="black", fg="white")
f2.grid(row=4, column=0, sticky=W)
l2=["Current Weight", "Height", "BMI", "Age", "Goal Weight"]
for i in range(len(l2)):
    cur_label2="l2" + str(i)
    cur_label2=Label(f2, text=l2[i], bg="black", fg="white")
    cur_label2.grid(row=i, column=0)
user2={
    "Current_weight":StringVar(),
    "Height":StringVar(),
    "BMI":StringVar(),
    "Age":StringVar(),
    "Goal_Weight":StringVar()
}
count1=0
for i in user2:
    cur_entry="entry" + i
    cur_entry=Entry(f2, width=89, textvariable=user2[i])
    cur_entry.grid(row=count1, column=1)
    count1+=1
#Address
f3=LabelFrame(root, text="Address", bg="black", fg="white")
f3.grid(row=10, column=0, sticky=W)
l3=["Current Street Address", "Permanent Street Address", "City", "State", "Postal"]
for i in range(len(l3)):
    cur_label3="l3" + str(i)
    cur_label3=Label(f3, text=l3[i], bg="black", fg="white")
    cur_label3.grid(row=i, column=0)
user3={
    "Current_Street_Address":StringVar(),
    "Permanent_Street_Address":StringVar(),
    "City":StringVar(),
    "State":StringVar(),
    "Postal":StringVar()
}
count2=0
for i in user3:
    cur_entry="entry" + i
    cur_entry=Entry(f3, width=80, textvariable=user3[i])
    cur_entry.grid(row=count2, column=1)
    count2+=1
f4=LabelFrame(root, text="Contact", bg="black", fg="white")
f4.grid(row=17, column=0, sticky=W)
l4=["Area code", "Phone No.", "Emergency Contact", "Relationship", "E-Mail"]
for i in range(len(l4)):
    cur_label4="l4" + str(i)
    cur_label4=Label(f4, text=l4[i], bg="black", fg="white")
    cur_label4.grid(row=i, column=0)
user4={
    "Area_code":StringVar(),
    "Phone_no":StringVar(),
    "Emergency_contact":StringVar(),
    "Relationship":StringVar(),
    "E-Mail":StringVar()
}
count3=0
for i in user4:
    cur_entry="entry" + i
    cur_entry=Entry(f4, width=85, textvariable=user4[i])
    cur_entry.grid(row=count3, column=1)
    count3+=1
suggestion_value=IntVar()
suggestion=Checkbutton(root, text="I have Read, Understand and Agree to all the TERMS and CONDITION of the FITNESS CLUB.", variable="suggestion_value").grid(row=24, column=0)
Button(root, text="SUBMIT", bg="black", fg="white", command=done).grid(row=27, column=0)
root.mainloop()
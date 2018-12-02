import csv
List = []
while 1:
    name = input("Enter Name:")
    email = input("Enter email:")
    mobile = input("Enter mobile:")
    university = input("Enter university:")
    major = input("Enter major:")
    profile = {'Name': name ,'email': email ,'mobile': mobile ,'university': university ,'major': major }
    List.append(profile)
    stop = input("Type STOP to stop")
    if stop == 'STOP':
        break
fieldnames = ["Name","email","mobile","university","major"]
try:
    with open('task.csv','w',newline = '') as f:
        w = csv.DictWriter(f,fieldnames=fieldnames)
        w.writeheader()
        w.writerows(List)
except IOError:
    print("IO error")

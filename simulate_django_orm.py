import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
print("Git connection successfull")

# cur.execute("create database DjangoORM")
# print("Database Created")

# cur.execute('''create table employee(
#     id int primary key auto_increment,
#     name varchar(20),
#     designation varchar(30),
#     salary decimal(10,2)
#     )''')
# print("Table created")

class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for col in kwargs.keys():
            if cols!="":
                cols+=','
                placeholder+=','
            cols+=col
            placeholder+='%s'
            
        values=tuple(kwargs.values())
        query=f"insert into employee({cols}) values({placeholder})"
        cur.execute(query,values)
        conn.commit()
    
    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())
     
    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}={kwargs[key]}")
            print(cur.fetchall())
    
    def update(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"update employee set {key}='{kwargs[key]}' where id={args[0]}")
            conn.commit()

    
    def delete(self,*args,**kwargs):
        cur.execute(f"delete from employee where id={args[0]}")
        conn.commit()
    
    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}='{kwargs[key]}'")
            print(cur.fetchall())

employee=Employee()
while True:
    print("1 for Create Employee")
    print("2 for List all Employee")
    print("3 for Employee detail view")
    print("4 for Update Employee")
    print("5 for Delete Employee")
    print("6 for filter Employee")
    print("7 for exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        name=input("Enter the name : ")
        desig=input("Enter the designation : ")
        salary=float(input("Enter the salary : "))
        employee.create(name=name,designation=desig,salary=salary)
        print("-----------------------")
        
    elif choice==2:
        employee.list()
        print("-----------------------")
        
    elif choice==3:
        id=int(input("Enter the employee ID : "))
        employee.retrieve(id=id)
        print("-----------------------")
        
    elif choice==4:
        id=int(input("Enter the employee ID : "))
        print("1 for Update Name\n2 for Update Designation\n3 for Update Salary")
        choice=int(input("Enter your choice : "))
        if choice==1:
            name=input("Enter the new name : ")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("Enter the new designation : ")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("Enter the new salary : "))
            employee.update(id,salary=salary)
        else:
            print("Invalid choice")
        
        print("-----------------------")
        
    elif choice==5:
        id=int(input("Enter the id to be deleted : "))
        employee.delete(id)
        print("-----------------------")
        
    elif choice==6:
        print("1 for ID\n2 for Name\n3 for Designation\n4 for Salary")
        choice=int(input("Enter your choice : "))
        if choice==1:
            id=int(input("Enter the id : "))
            employee.filter(id=id)
        elif choice==2:
            name=input("Enter the name : ")
            employee.filter(name=name)
        elif choice==3:
            desig=input("Enter the designation : ")
            employee.filter(designation=desig)
        elif choice==4:
            salary=float(input("Enter the salary : "))
            employee.filter(salary=salary)
        else:
            print("Invalid choice")
        print("-----------------------")
    
    elif choice==7:
        print("Exiting.....")
        break 
    
    else:
        print("Invalid Choice")
        print("-----------------------")


conn.close()
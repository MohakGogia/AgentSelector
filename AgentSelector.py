import random
import datetime

my_objects = []


#Declaring class agent for taking all agent details
class Agent:
    def __init__(self,num,avail,av_time,role):
        self.agent_no = num
        self.is_available = bool(avail)
        self.available_since = av_time
        self.role = role
    def get(self):
        print("____________________________")
        print("Available agent Details: ")
        print("____________________________")
        print(f'Agent No: {self.agent_no}')
        print(f'Is Available: {self.is_available}')
        print(f'Available Since: {self.available_since}')
        print(f'Role: {self.role}')


#Input agent data from user   
def take_data():
    global n
    n = int(input(("How many agents data do you want to enter:")))
    for i in range(n):
        print("----------------------------")
        print(f'Enter data for Agent {i+1}')
        print("----------------------------")
        a_no = int(input("Agent No:"))
        is_a = int(input("Is available (T->1/F->0):"))
        if is_a == 0:
            ts_avail = "NULL"
        else:
            ts_avail = input("Time since available ('%H:%M:%S):")
        role = input("Role:")
        my_objects.append(Agent(a_no,is_a,ts_avail,role.lower()))


#Agent selection mode - All                          
def all():
    issue = input("\n Enter Issue (support/sales/finance/hr) :")
    issue = issue.lower().split()
    for i in range(n):
        if my_objects[i].is_available==True:
            if my_objects[i].role in issue:
                print("\n")
                my_objects[i].get()


#Agent selection mode - Random  
def ran():
    issue = input("\n Enter Issue (support/sales/finance/hr) :")
    issue = issue.lower().split()
    temp=[]
    for i in range(n):
        if(my_objects[i].is_available == True):
            if my_objects[i].role in issue:
                temp.append(my_objects[i].agent_no)
    r = random.choice(temp)
    for i in range(n):
        if my_objects[i].agent_no == r:
            print("\n")
            my_objects[i].get()


#Agent selection mode - LeastBusy
def leastbusy():
    issue = input("\n Enter Issue (support/sales/finance/hr) :")
    issue = issue.lower().split()
    flag = True
    time = datetime.datetime.now()
    curtime = str(time)[11:19]
    for i in range(n):
        if my_objects[i].is_available == True:
            if my_objects[i].role in issue:
                t = my_objects[i].available_since
                FMT = '%H:%M:%S'
                tdelta = datetime.datetime.strptime(curtime, FMT) - datetime.datetime.strptime(t, FMT)
                if flag:
                    maximum = tdelta
                    pos = my_objects[i].agent_no
                    flag = False
                if tdelta > maximum:
                    maximum = tdelta
                    pos = my_objects[i].agent_no
    for i in range(n):
        if(my_objects[i].agent_no == pos):
            print("\n")
            my_objects[i].get()


#Driver function 
if __name__ == "__main__":
    take_data()
    mode = input("\n\n Enter Agent Selection Mode (all/random/leastbusy) :")
    mode = mode.lower().strip()
    if mode == 'all':
        all()
    elif mode == 'random':
        ran()
    elif mode == 'leastbusy':
        leastbusy()
    else:
        print("Invalid Mode")

    

#sql connectivity--
import mysql.connector as m
db=m.connect(host='localhost',user='root',password='1234',database='nirvana')
mycursor=db.cursor()
print()
print('                                                  WELCOME TO HOTEL NIRVANA\n\n')



num=1000
#booking section--
def book():
    try:
        pid=1
        mycursor.execute("select count(*) from booking")  
        for x in mycursor.fetchone():
            pid+=x
        print('---')
        name=input('enter your name: ')
        phone=input('enter your phone number: +91')
        address=input('enter your address: ')
        room=int(input('''<<SELECT ROOM TYPE>> 
    1. Standard Non-AC 
    2. Standard AC 
    3. 3-Bed Non-AC 
    4. 3-Bed AC\nenter room choice: '''))
        sql='INSERT INTO booking values(%s,%s,%s,%s,%s)'
        val=(pid,name,phone,address,room)
        mycursor.execute(sql,val)
        db.commit()
        print('***   room booked successfully   ***')
        if room==1:
            print('Standard Non-AC - Rs1000')
        elif room==2:
            print('Standard AC - Rs2000')
        elif room==3:
            print('3-Bed Non-AC - Rs3000')
        elif room==4:
            print('3-Bed AC - Rs4000')
        else:
            print('error occured 404')
        print('*****   YOUR ID IS {}   **** '.format(pid))
        print('---')
    except:
        print('\n): an error occured please try again :(')

#about rooms--
def room():
    print('---')
    print('''1. Standard Non-AC - Rs1000
2. Standard AC - Rs2000
3. 3-Bed Non-AC - Rs3000
4. 3-Bed AC - Rs4000''')
    print('---')

#payment section--    
def pay():
    try:
        print('---')
        ppid=input('enter your id: ')
        sql='SELECT room FROM booking where id={}'
        sql1='SELECT name FROM booking where id={}'
        mycursor.execute(sql.format(ppid))
        for x in mycursor.fetchone():
            r=x
        mycursor.execute(sql1.format(ppid))
        for n in mycursor.fetchone():
            name=n
        print('Pay via any -\n1.Bank\n2.UPI\n3.Cash')
        print('hello! {} you booked a'.format(name))
        if r==1:
            print('Standard Non-AC Room\nTotal Amount: Rs1000')
        elif r==2:
            print('Standard AC Room\nTotal Amount: Rs2000')
        elif r==3:
            print('3-Bed Non-AC Room\nTotal Amount: Rs3000')
        else:
            print('3-Bed AC Room\nTotal Amount: Rs4000')
        print('---')
    except:
        print('\n): an error occured please try again :(')
def record():
    try:
        print('---')
        ppid=input('enter your id: ')
        sql='SELECT * FROM booking where id={}'
        mycursor.execute(sql.format(ppid))
        c=0
        for j in mycursor.fetchone():
            if c==0:
                print('Customer id: {}'.format(j))
                c+=1
            elif c==1:
                print('Customer Name: {}'.format(j))
                c+=1
            elif c==2:
                print('Customer Phone number: +91{}'.format(j))
                c+=1
            elif c==3:
                print('Customer Address: {}'.format(j))
                c+=1
            else:
                if j==1:
                    print('Customer room: {}'.format('Standard Non-AC'))
                elif j==2:
                    print('Customer room: {}'.format('Standard AC'))
                elif j==3:
                    print('Customer room: {}'.format('3-Bed Non-AC'))
                else:
                    print('Customer room: {}'.format('3-Bed AC'))
        print('---')
    except:
        print('\n): an error occured please try again :(')


#main pogram--
while num!=0:
    num=int(input('''\n1 Rooms Info
2 Booking
3 Payment
4 Record
0 Exit

enter your choice: '''))
    print()
    if num==1:
        room()
    elif num==2:
        book()
    elif num==3:
        pay()
    elif num==4:
        record()
    else:
        exit()

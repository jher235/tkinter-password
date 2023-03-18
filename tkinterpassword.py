from tkinter import *
win = Tk()
users = dict(김재헌='정통',김진웅='통계학과',양석재='정통',김근탁='게임학과')
ct=0


def login():
    global ct
    uid = et1.get().strip()
    pwd = et2.get().strip()
    win2 = Tk()
    if ct > 4:
        win.destroy()
    else:
        print(uid,pwd)
        if uid in users.keys():
            if pwd == users[uid]:    
                # win2.geometry('100x50')
                win2.title('성공입니다')
                lbl2 = Label(win2,text = "로그인 되었습니다")
                lbl2_1 = Label(win2,text = "환영합니다. {}님!".format(uid))
                lbl2.grid(row=0,column=0,sticky=W)
                lbl2_1.grid(row=1,column=0,sticky = W)
                print('로그인 성공')
                win.destroy()
            else:
                win2.title('실패했습니다')
                lbl2 = Label(win2,text = "비밀번호를 다시 확인하세요")
                lbl2_1 = Label(win2,text = "로그인에 {}번 실패하셨습니다. 5번 이상 실패하실 경우 자동으로 프로그램이 종료됩니다.".format(ct))
                lbl2.grid(row=0,column=0,sticky=W)
                lbl2_1.grid(row=1,column=0,sticky = W)
                print("비밀번호를 다시 확인하세요")
                ct +=1
        else:
            lbl2 = Label(win2,text = "아이디를 다시 확인하세요")
            lbl2_1 = Label(win2,text = "로그인에 {}번 실패하셨습니다. 5번 이상 실패하실 경우 자동으로 프로그램이 종료됩니다.".format(ct))
            lbl2.grid(row=0,column=0,sticky=W)
            lbl2_1.grid(row=1,column=0,sticky = W)
            print("아이디를 다시 확인하세요")
            ct +=1
def exit():
    win.destroy()

win.title("사용자 인증")


lb1 =Label(win, text="사용자 이름") 
lb2 = Label(win, text="암호") 
lb1.grid(row = 0,column=0,sticky=E)
lb2.grid(row = 1,column=0,sticky=E)

# lb3 =Label(win, text="안녕") 
# lb4 = Label(win, text="야호") 
# lb3.grid(row = 2,column=0,sticky=E)
# lb4.grid(row = 3,column=0,sticky=E)

# et3 = Entry(win) 
# et4 = Entry(win) 
# et3.grid(row=2,column=1)
# et4.grid(row=3,column=1)


et1 = Entry(win)
et2 = Entry(win)
et1.grid(row = 0, column = 1)
et2.grid(row = 1,column = 1)

lb = Label(win)
lb.grid(row = 2, column = 0, columnspan = 2) #columnspan = 2 두열을 합함
bt1 = Button(lb,text='Ok', command = login)
bt2 = Button(lb,text= "Cancel",command = exit)
bt1.grid(row=0,column=0 , padx = 10)
bt2.grid(row = 0,column=1, padx = 10)

win.mainloop()
import tkinter as tk 
from tkinter import font,ttk
import sys
time_q = 0
prio_var = 0
pid_list = []
at_list = []
bt_list = []
prio_list = []
io_list = []
bt1_list = []
def rr():
    rr_w = tk.Toplevel(b)
    rr_w.title("LJF")
    rr_w.state('zoomed')
    rr_w.configure(bg="#eab676")
    rr_f1 = tk.Frame(rr_w,bg="#eab676")
    rr_f2 = tk.Frame(rr_w,bg="#eab676")
    rr_f1.pack(side="top")
    rr_f2.pack(side='bottom')
    rr_b = tk.Button(rr_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=rr_w.destroy)
    rr_b.bind("<Return>", lambda event=None: rr_b.invoke())
    rr_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    r_q = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),int(x[1])))
    at_list1, pid_list1, bt_list1,num,num2,num3= zip(*sorted_1)
    bt1_list1 = list([int(x) for x in bt_list1])
    num2 = list([int(x) for x in num2])
    num3 = list([int(x) for x in num3])
    avg_wt = 0
    avg_tat= 0
    lvl = 0
    i = 0
    time = int(at_list1[0])
    print(at_list1)
    if(time>0):
        r_q.append((lvl,0,-1,-1))
        print(lvl)
        g_c.append((0,time,0,-1,0))
        lvl += 1
        i+=1
    r_q.append((lvl,1,int(pid_list1[0]),0))
    print(lvl)
    num3[0] = 1
    lvl += 1
    print(num3)
    while(i<len(r_q)):
        rq = r_q[i]
        if(bt1_list1[rq[3]]>time_q):
            g_c.append((time,(time+time_q),1,rq[2],0))
            bt1_list1[rq[3]] -= time_q
            time += time_q
            for j in range(len(at_list1)):
                if(int(at_list1[j])<=time):
                    if(num3[j]==0 and num2[j]==0):
                        num3[j] = 1
                        r_q.append((lvl,1,int(pid_list1[j]),j))
                        print(lvl)
                else:
                    break
            r_q.append((lvl,1,rq[2],rq[3]))
            print(lvl)
            lvl+=1
        else:
            num2[rq[3]] = 1
            g_c.append((time,(time+bt1_list1[rq[3]]),1,rq[2],0))
            time +=bt1_list1[rq[3]]
            bt1_list1[rq[3]] = 0
            ct = time
            ct_list[rq[3]] = ct
            tat = ct - int(at_list1[rq[3]])
            tat_list[rq[3]] = tat
            avg_tat += tat
            wt = tat - int(bt_list1[rq[3]])
            wt_list[rq[3]] = wt
            avg_wt += wt
            flag = False
            for j in range(len(at_list1)):
                if(int(at_list1[j])<=time):
                    if(num3[j]==0 and num2[j]==0):
                        num3[j] = 1
                        r_q.append((lvl,1,int(pid_list1[j]),j))
                        print(lvl)
                        flag = True
                        if(j==(len(at_list1)-1)):   
                            lvl += 1
                    if(j==(len(at_list1)-1)):
                        if(flag==False):
                            tup = list(g_c[len(g_c)-1])
                            tup[4] = 1
                            g_c[len(g_c)-1] = tuple(tup)
                else:
                    if(flag):
                        lvl+=1          
                        break
                    else:
                        if(i==(len(r_q)-1)):
                            r_q.append((lvl,0,-1,-1))
                            print(lvl)
                            lvl+=1
                            g_c.append((time,int(at_list1[j]),0,int(pid_list1[j]),0))
                            r_q.append((lvl,1,int(pid_list1[j]),j))
                            print(lvl)
                            i += 1
                            lvl+=1
                            time = int(at_list1[j])
                            num3[j] = 1
                        else:
                            tup = list(g_c[len(g_c)-1])
                            tup[4] = 1
                            g_c[len(g_c)-1] = tuple(tup)
                            break
        i+=1
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2,pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(rr_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(rr_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(rr_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(rr_f1, text="Gantt Chart and Ready Queue", font=of,width=s)
    g.pack()
    canvas1 = tk.Canvas(rr_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas1.pack(pady=20,padx=182)
    canvas = tk.Canvas(rr_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    lvl = -1
    flag2 = False
    cnt = 0
    print(r_q)
    while index < (len(g_c)):
        canvas1.delete("all")
        fig = 0
        flag = True
        i = 0
        if(flag2==False):
            lvl += 1
        cnt1 = 0
        while(flag):
            tup = r_q[i]
            if(tup[0]<=lvl):
                if(tup[1]==1):
                    canvas1.create_text(fig + (ext/2), 25, text=f"P{tup[2]}", fill="black",font=rf)
                    if(cnt1<cnt):
                        canvas1.create_line(fig + (ext/2) -10, 15, fig + (ext/2) + 10, 35, width=2)
                        canvas1.create_line(fig + (ext/2) + 10, 15, fig + (ext/2) -10, 35, width=2)
                else:
                    canvas1.create_text(fig + (ext/2), 25, text=f"EMPTY", fill="black",font=rf)
                i+=1
                fig+=ext
                if(i==(len(r_q))):
                    flag = False
            else:
                flag = False
            cnt1+=1
        cnt+=1
        rr_w.update()
        rr_w.after(2000)
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)
            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
            if(tup[4]==0):
                flag2 = False
            else:
                flag2 = True
        rr_w.update()
        rr_w.after(2000)
        index += 1
def pp():
    pp_w = tk.Toplevel(b)
    pp_w.title("LJF")
    pp_w.state('zoomed')
    pp_w.configure(bg="#eab676")
    pp_f1 = tk.Frame(pp_w,bg="#eab676")
    pp_f2 = tk.Frame(pp_w,bg="#eab676")
    pp_f1.pack(side="top")
    pp_f2.pack(side='bottom')
    pp_b = tk.Button(pp_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=pp_w.destroy)
    pp_b.bind("<Return>", lambda event=None: pp_b.invoke())
    pp_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list, prio_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),-int(x[3])))
    at_list1, pid_list1, bt_list1, prio_list1,num,num2= zip(*sorted_1)
    if prio_var == -1:
        p_l = list(prio_list1)
        n_p_l = [-int(x) for x in p_l]
        prio_list1 = tuple(n_p_l)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    btl_list1 = list([int(x) for x in bt_list1])
    t_bt = sum(btl_list1)
    for i in range(t_bt):
        min = float('-inf')
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and int(prio_list1[j]) > min:
                min = int(prio_list1[j])
                index = j
                flag = True
        if flag==True:
            g_c.append((time,time+1,1,int(pid_list1[index])))
            btl_list1[index] -= 1
            time+=1
            if(btl_list1[index]==0):
                m_l1 = list(num2)
                m_l1[index] = 1
                num2 = tuple(m_l1)
                ct = time
                ct_list[index] = ct 
                tat = ct - int(at_list1[index])
                tat_list[index] = tat 
                avg_tat += tat
                wt = tat - int(bt_list1[index])
                wt_list[index] = wt 
                avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    g_c.append((time,time+1,1,int(pid_list1[j])))
                    btl_list1[j] -= 1
                    time+=1
                    if(btl_list1[j]==0):
                        m_l1 = list(num2)
                        m_l1[j] = 1
                        num2 = tuple(m_l1)
                        ct = time
                        ct_list[j] = ct 
                        tat = ct - int(at_list1[j])
                        tat_list[index] = tat 
                        avg_tat += tat
                        wt = tat - int(bt_list1[j])
                        wt_list[j] = wt 
                        avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, prio_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, prio_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(pp_f1, show="headings", columns=("Process ID", "Priority", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Priority", text="Priority")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, prio, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, prio_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, prio, at, bt, ct, tat, wt))
    for col in ("Process ID", "Priority","Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(pp_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(pp_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(pp_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(pp_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)
            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        pp_w.update()
        pp_w.after(2000)
        index += 1
def lrtf():
    lrtf_w = tk.Toplevel(b)
    lrtf_w.title("SJF")
    lrtf_w.state('zoomed')
    lrtf_w.configure(bg="#eab676")
    lrtf_f1 = tk.Frame(lrtf_w,bg="#eab676")
    lrtf_f2 = tk.Frame(lrtf_w,bg="#eab676")
    lrtf_f1.pack(side="top")
    lrtf_f2.pack(side='bottom')
    lrtf_b = tk.Button(lrtf_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=lrtf_w.destroy)
    lrtf_b.bind("<Return>", lambda event=None: lrtf_b.invoke())
    lrtf_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),-int(x[2])))
    at_list1, pid_list1, bt_list1, num,num2= zip(*sorted_1)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    btl_list1 = list([int(x) for x in bt_list1])
    t_bt = sum(btl_list1)
    for i in range(t_bt):
        min = float('-inf')
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and int(btl_list1[j]) > min:
                min = btl_list1[j]
                index = j
                flag = True
        if flag==True:
            g_c.append((time,time+1,1,int(pid_list1[index])))
            btl_list1[index] -= 1
            time+=1
            if(btl_list1[index]==0):
                m_l1 = list(num2)
                m_l1[index] = 1
                num2 = tuple(m_l1)
                ct = time
                ct_list[index] = ct 
                tat = ct - int(at_list1[index])
                tat_list[index] = tat 
                avg_tat += tat
                wt = tat - int(bt_list1[index])
                wt_list[index] = wt 
                avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    g_c.append((time,time+1,1,int(pid_list1[j])))
                    btl_list1[j] -= 1
                    time+=1
                    if(btl_list1[j]==0):
                        m_l1 = list(num2)
                        m_l1[j] = 1
                        num2 = tuple(m_l1)
                        ct = time
                        ct_list[j] = ct 
                        tat = ct - int(at_list1[j])
                        tat_list[index] = tat 
                        avg_tat += tat
                        wt = tat - int(bt_list1[j])
                        wt_list[j] = wt 
                        avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(lrtf_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(lrtf_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(lrtf_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(lrtf_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(lrtf_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)

            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        lrtf_w.update()
        lrtf_w.after(2000)
        index += 1
def srtf():
    srtf_w = tk.Toplevel(b)
    srtf_w.title("SJF")
    srtf_w.state('zoomed')
    srtf_w.configure(bg="#eab676")
    srtf_f1 = tk.Frame(srtf_w,bg="#eab676")
    srtf_f2 = tk.Frame(srtf_w,bg="#eab676")
    srtf_f1.pack(side="top")
    srtf_f2.pack(side='bottom')
    srtf_b = tk.Button(srtf_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=srtf_w.destroy)
    srtf_b.bind("<Return>", lambda event=None: srtf_b.invoke())
    srtf_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),int(x[2])))
    at_list1, pid_list1, bt_list1, num,num2= zip(*sorted_1)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    btl_list1 = list([int(x) for x in bt_list1])
    t_bt = sum(btl_list1)
    for i in range(t_bt):
        min = sys.maxsize
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and int(btl_list1[j]) < min:
                min = btl_list1[j]
                index = j
                flag = True
        if flag==True:
            g_c.append((time,time+1,1,int(pid_list1[index])))
            btl_list1[index] -= 1
            time+=1
            if(btl_list1[index]==0):
                m_l1 = list(num2)
                m_l1[index] = 1
                num2 = tuple(m_l1)
                ct = time
                ct_list[index] = ct 
                tat = ct - int(at_list1[index])
                tat_list[index] = tat 
                avg_tat += tat
                wt = tat - int(bt_list1[index])
                wt_list[index] = wt 
                avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    g_c.append((time,time+1,1,int(pid_list1[j])))
                    btl_list1[j] -= 1
                    time+=1
                    if(btl_list1[j]==0):
                        m_l1 = list(num2)
                        m_l1[j] = 1
                        num2 = tuple(m_l1)
                        ct = time
                        ct_list[j] = ct 
                        tat = ct - int(at_list1[j])
                        tat_list[index] = tat 
                        avg_tat += tat
                        wt = tat - int(bt_list1[j])
                        wt_list[j] = wt 
                        avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(srtf_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(srtf_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(srtf_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(srtf_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(srtf_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)

            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        srtf_w.update()
        srtf_w.after(2000)
        index += 1
def hrrn():
    hrrn_w = tk.Toplevel(b)
    hrrn_w.title("SJF")
    hrrn_w.state('zoomed')
    hrrn_w.configure(bg="#eab676")
    hrrn_f1 = tk.Frame(hrrn_w,bg="#eab676")
    hrrn_f2 = tk.Frame(hrrn_w,bg="#eab676")
    hrrn_f1.pack(side="top")
    hrrn_f2.pack(side='bottom')
    hrrn_b = tk.Button(hrrn_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=hrrn_w.destroy)
    hrrn_b.bind("<Return>", lambda event=None: hrrn_b.invoke())
    hrrn_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0])))
    at_list1, pid_list1, bt_list1, num,num2= zip(*sorted_1)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    ct = time + int(bt_list1[0])
    ct_list[0] = ct
    g_c.append((time,ct,1,int(pid_list1[0])))
    time = ct
    tat = ct - int(at_list1[0])
    tat_list[0] = tat
    avg_tat += tat
    wt = tat - int(bt_list1[0])
    wt_list[0] = wt
    avg_wt += wt
    m_l = list(num2)
    m_l[0] = 1
    num2 = tuple(m_l)
    for i in range(len(at_list1)-1):
        min = float('-inf')
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            hrrn_val = ((time - int(at_list1[j]) + int(bt_list1[j]))/int(bt_list1[j])) 
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and hrrn_val > min:
                min = hrrn_val
                index = j
                flag = True
        if flag==True:
            m_l1 = list(num2)
            m_l1[index] = 1
            num2 = tuple(m_l1)
            ct = time + int(bt_list1[index])
            ct_list[index] = ct 
            g_c.append((time,ct,1,int(pid_list1[index])))
            time = ct
            tat = ct - int(at_list1[index])
            tat_list[index] = tat 
            avg_tat += tat
            wt = tat - int(bt_list1[index])
            wt_list[index] = wt 
            avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    m_l2 = list(num2)
                    m_l2[j] = 1
                    num2 = tuple(m_l2)
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    ct = time + int(bt_list1[j])
                    ct_list[j] = ct
                    g_c.append((time,ct,1,int(pid_list1[j])))
                    time = ct
                    tat = ct - int(at_list1[j])
                    tat_list[j] = tat 
                    avg_tat += tat
                    wt = tat - int(bt_list1[j])
                    wt_list[j] = wt 
                    avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(hrrn_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(hrrn_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(hrrn_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(hrrn_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(hrrn_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)

            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        hrrn_w.update()
        hrrn_w.after(2000)
        index += 1
def set_prio(val):
    global prio_var
    prio_var = val
def npp():
    npp_w = tk.Toplevel(b)
    npp_w.title("LJF")
    npp_w.state('zoomed')
    npp_w.configure(bg="#eab676")
    npp_f1 = tk.Frame(npp_w,bg="#eab676")
    npp_f2 = tk.Frame(npp_w,bg="#eab676")
    npp_f1.pack(side="top")
    npp_f2.pack(side='bottom')
    npp_b = tk.Button(npp_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=npp_w.destroy)
    npp_b.bind("<Return>", lambda event=None: npp_b.invoke())
    npp_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list, prio_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),-int(x[3])))
    at_list1, pid_list1, bt_list1, prio_list1,num,num2= zip(*sorted_1)
    if prio_var == -1:
        p_l = list(prio_list1)
        n_p_l = [-int(x) for x in p_l]
        prio_list1 = tuple(n_p_l)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    ct = time + int(bt_list1[0])
    ct_list[0] = ct
    g_c.append((time,ct,1,int(pid_list1[0])))
    time = ct
    tat = ct - int(at_list1[0])
    tat_list[0] = tat
    avg_tat += tat
    wt = tat - int(bt_list1[0])
    wt_list[0] = wt
    avg_wt += wt
    m_l = list(num2)
    m_l[0] = 1
    num2 = tuple(m_l)
    for i in range(len(at_list1)-1):
        min = float('-inf')
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and int(prio_list1[j]) > min:
                min = int(prio_list1[j])
                index = j
                flag = True
        if flag==True:
            m_l1 = list(num2)
            m_l1[index] = 1
            num2 = tuple(m_l1)
            ct = time + int(bt_list1[index])
            ct_list[index] = ct 
            g_c.append((time,ct,1,int(pid_list1[index])))
            time = ct
            tat = ct - int(at_list1[index])
            tat_list[index] = tat 
            avg_tat += tat
            wt = tat - int(bt_list1[index])
            wt_list[index] = wt 
            avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    m_l2 = list(num2)
                    m_l2[j] = 1
                    num2 = tuple(m_l2)
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    ct = time + int(bt_list1[j])
                    ct_list[j] = ct
                    g_c.append((time,ct,1,int(pid_list1[j])))
                    time = ct
                    tat = ct - int(at_list1[j])
                    tat_list[j] = tat 
                    avg_tat += tat
                    wt = tat - int(bt_list1[j])
                    wt_list[j] = wt 
                    avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, prio_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, prio_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(npp_f1, show="headings", columns=("Process ID", "Priority", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Priority", text="Priority")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, prio, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, prio_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, prio, at, bt, ct, tat, wt))
    for col in ("Process ID", "Priority","Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(npp_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(npp_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(npp_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(npp_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)
            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        npp_w.update()
        npp_w.after(2000)
        index += 1
def ljf():
    ljf_w = tk.Toplevel(b)
    ljf_w.title("LJF")
    ljf_w.state('zoomed')
    ljf_w.configure(bg="#eab676")
    ljf_f1 = tk.Frame(ljf_w,bg="#eab676")
    ljf_f2 = tk.Frame(ljf_w,bg="#eab676")
    ljf_f1.pack(side="top")
    ljf_f2.pack(side='bottom')
    ljf_b = tk.Button(ljf_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=ljf_w.destroy)
    ljf_b.bind("<Return>", lambda event=None: ljf_b.invoke())
    ljf_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),-int(x[2])))
    at_list1, pid_list1, bt_list1, num,num2= zip(*sorted_1)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    ct = time + int(bt_list1[0])
    ct_list[0] = ct
    g_c.append((time,ct,1,int(pid_list1[0])))
    time = ct
    tat = ct - int(at_list1[0])
    tat_list[0] = tat
    avg_tat += tat
    wt = tat - int(bt_list1[0])
    wt_list[0] = wt
    avg_wt += wt
    m_l = list(num2)
    m_l[0] = 1
    num2 = tuple(m_l)
    for i in range(len(at_list1)-1):
        min = float('-inf')
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and int(bt_list1[j]) > min:
                min = int(bt_list1[j])
                index = j
                flag = True
        if flag==True:
            m_l1 = list(num2)
            m_l1[index] = 1
            num2 = tuple(m_l1)
            ct = time + int(bt_list1[index])
            ct_list[index] = ct 
            g_c.append((time,ct,1,int(pid_list1[index])))
            time = ct
            tat = ct - int(at_list1[index])
            tat_list[index] = tat 
            avg_tat += tat
            wt = tat - int(bt_list1[index])
            wt_list[index] = wt 
            avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    m_l2 = list(num2)
                    m_l2[j] = 1
                    num2 = tuple(m_l2)
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    ct = time + int(bt_list1[j])
                    ct_list[j] = ct
                    g_c.append((time,ct,1,int(pid_list1[j])))
                    time = ct
                    tat = ct - int(at_list1[j])
                    tat_list[j] = tat 
                    avg_tat += tat
                    wt = tat - int(bt_list1[j])
                    wt_list[j] = wt 
                    avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(ljf_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(ljf_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(ljf_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(ljf_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(ljf_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)

            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext

        ljf_w.update()
        ljf_w.after(2000)
        index += 1
def sjf():
    sjf_w = tk.Toplevel(b)
    sjf_w.title("SJF")
    sjf_w.state('zoomed')
    sjf_w.configure(bg="#eab676")
    sjf_f1 = tk.Frame(sjf_w,bg="#eab676")
    sjf_f2 = tk.Frame(sjf_w,bg="#eab676")
    sjf_f1.pack(side="top")
    sjf_f2.pack(side='bottom')
    sjf_b = tk.Button(sjf_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=sjf_w.destroy)
    sjf_b.bind("<Return>", lambda event=None: sjf_b.invoke())
    sjf_b.pack()
    ct_list = [0] * len(pid_list) 
    tat_list = [0] * len(pid_list)
    wt_list = [0]  * len(pid_list)
    g_c = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        tup_list.append(0)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),int(x[2])))
    at_list1, pid_list1, bt_list1, num,num2= zip(*sorted_1)
    avg_wt = 0
    avg_tat= 0
    time = int(at_list1[0])
    if(time>0):
        g_c.append((0,time,0,-1))
    ct = time + int(bt_list1[0])
    ct_list[0] = ct
    g_c.append((time,ct,1,int(pid_list1[0])))
    time = ct
    tat = ct - int(at_list1[0])
    tat_list[0] = tat
    avg_tat += tat
    wt = tat - int(bt_list1[0])
    wt_list[0] = wt
    avg_wt += wt
    m_l = list(num2)
    m_l[0] = 1
    num2 = tuple(m_l)
    for i in range(len(at_list1)-1):
        min = sys.maxsize
        index = sys.maxsize
        flag = False
        for j in range (len(at_list1)):
            if int(at_list1[j]) <= time and int(num2[j]) == 0 and int(bt_list1[j]) < min:
                min = int(bt_list1[j])
                index = j
                flag = True
        if flag==True:
            m_l1 = list(num2)
            m_l1[index] = 1
            num2 = tuple(m_l1)
            ct = time + int(bt_list1[index])
            ct_list[index] = ct 
            g_c.append((time,ct,1,int(pid_list1[index])))
            time = ct
            tat = ct - int(at_list1[index])
            tat_list[index] = tat 
            avg_tat += tat
            wt = tat - int(bt_list1[index])
            wt_list[index] = wt 
            avg_wt += wt
        else:
            for j in range (len(at_list1)):
                if int(at_list1[j]) > time and int(num2[j]) == 0:
                    m_l2 = list(num2)
                    m_l2[j] = 1
                    num2 = tuple(m_l2)
                    g_c.append((time,int(at_list1[j]),0,-1))
                    time = int(at_list1[j])
                    ct = time + int(bt_list1[j])
                    ct_list[j] = ct
                    g_c.append((time,ct,1,int(pid_list1[j])))
                    time = ct
                    tat = ct - int(at_list1[j])
                    tat_list[j] = tat 
                    avg_tat += tat
                    wt = tat - int(bt_list1[j])
                    wt_list[j] = wt 
                    avg_wt += wt
                    break
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(sjf_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(sjf_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(sjf_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(sjf_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(sjf_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{tup[3]}", fill="black",font=of)
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)

            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text(fig+5, 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        sjf_w.update()
        sjf_w.after(2000)
        index += 1
def fcfs():
    fcfs_w = tk.Toplevel(b)
    fcfs_w.title("FCFS")
    fcfs_w.state('zoomed')
    fcfs_w.configure(bg="#eab676")
    fcfs_f1 = tk.Frame(fcfs_w,bg="#eab676")
    fcfs_f2 = tk.Frame(fcfs_w,bg="#eab676")
    fcfs_f1.pack(side="top")
    fcfs_f2.pack(side='bottom')
    fcfs_b = tk.Button(fcfs_f2, text="Exit", width=25,bg='white',fg='black', font=bf,command=fcfs_w.destroy)
    fcfs_b.bind("<Return>", lambda event=None: fcfs_b.invoke())
    fcfs_b.focus_set()
    fcfs_b.pack()
    ct_list = [] 
    tat_list = [] 
    wt_list = []
    g_c = []
    com = list(zip(at_list, pid_list, bt_list))
    for i, nam in enumerate(com, start=1):
        tup_list = list(nam)
        tup_list.append(i)
        com[i - 1] = tuple(tup_list)
    sorted_1 = sorted(com, key=lambda x: (int(x[0]),int(x[1])))
    at_list1, pid_list1, bt_list1, num= zip(*sorted_1)
    time = int(at_list1[0])
    avg_wt = 0
    avg_tat= 0
    if time > 0:
        g_c.append((0,time,0))
    for i in range(len(at_list1)):
        if(int(at_list1[i])>time):
            g_c.append((time,int(at_list1[i]),0))
            time = int(at_list1[i])
        ct = time + int(bt_list1[i])
        ct_list.append(ct)
        g_c.append((time,ct,1))
        time = ct
        tat = ct - int(at_list1[i])
        tat_list.append(tat)
        avg_tat = avg_tat + tat
        wt = tat - int(bt_list1[i])
        wt_list.append(wt)
        avg_wt = avg_wt + wt
    com1 = list(zip(num, at_list1, pid_list1, bt_list1, ct_list, tat_list, wt_list))
    sorted_2 = sorted(com1, key=lambda x: int(x[0]))
    num,at_list2, pid_list2, bt_list2, ct_list1, tat_list1, wt_list1= zip(*sorted_2)
    tree = ttk.Treeview(fcfs_f1, show="headings", columns=("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"),height=len(at_list1))
    tree.heading("Process ID", text="Process ID")
    tree.heading("Arrival Time", text="Arrival Time")
    tree.heading("Burst Time", text="Burst Time")
    tree.heading("Completion Time", text="Completion Time")
    tree.heading("TurnAround Time", text="TurnAround Time")
    tree.heading("Waiting Time", text="Waiting Time")
    for index, (pid, at, bt, ct, tat, wt) in enumerate(zip(pid_list2, at_list2, bt_list2, ct_list1, tat_list1, wt_list1), 1):
        tree.insert("", index, values=(pid, at, bt, ct, tat, wt))
    for col in ("Process ID", "Arrival Time", "Burst Time","Completion Time","TurnAround Time","Waiting Time"):
        tree.column(col, anchor="center")
    tree.pack(pady=20)
    avg_tat = round(avg_tat / len(tat_list),2)
    avg_wt = round(avg_wt / len(wt_list),2)
    avgtat_l = tk.Label(fcfs_f1, text=f"Average TurnAround Time: {avg_tat}", font=of,width=s)
    avgtat_l.pack()
    avgwt_l = tk.Label(fcfs_f1, text=f"Average Waiting Time: {avg_wt}", font=of,width=s)
    avgwt_l.pack(pady=20)
    g = tk.Label(fcfs_f1, text="Gantt Chart", font=of,width=s)
    g.pack()
    canvas = tk.Canvas(fcfs_f1, width=1001, height=100, bg="#eab676",bd=0, highlightthickness=0)
    canvas.pack(pady=100,padx=182)
    index = 0
    ext = (1000/(len(g_c)))
    while index < (len(g_c)):
        canvas.delete("all")
        fig = 0
        pid_p = 0
        for i in range(index + 1):
            canvas.create_rectangle(fig, 0, fig+ext, 50, fill="#eab676")    
            tup = g_c[i]
            if (tup[2]==1):    
                canvas.create_text(fig + (ext/2), 25, text=f"P{pid_list1[pid_p]}", fill="black",font=of)
                pid_p+=1
            else:
                canvas.create_text(fig + (ext/2), 25, text=f"IDLE", fill="black",font=of)

            if(i==(len(g_c)-1)):
                canvas.create_text(990, 75, text=f"{tup[1]}", fill="black",font=sf)
            else:
                if(i==0):
                    canvas.create_text((fig+5), 75, text=f"{tup[0]}", fill="black",font=sf)
                else:
                    canvas.create_text(fig, 75, text=f"{tup[0]}", fill="black",font=sf)
                canvas.create_text(fig+ext, 75, text=f"{tup[1]}", fill="black",font=sf)
            fig += ext
        fcfs_w.update()
        fcfs_w.after(2000)
        index += 1
def c_bb(opt):
    if opt == "FCFS":
        fcfs()
    if opt == "SJF":
        sjf()
    if opt == "SRTF":
        srtf()
    if opt == "RR":
        rr()
    if opt == "LJF":
        ljf()
    if opt == "LRTF":
        lrtf()
    if opt == "HRRN":
        hrrn()
    if opt == "Non Preemptive Priority":
        npp()
    if opt == "Preemptive Priority":
        pp()
def a_p():
    global pid_inp, at_inp, bt_inp, prio_inp, io_inp, bt1_inp, tq_inp, time_q
    pid = pid_inp.get() if pid_inp else ""
    at = at_inp.get() if at_inp else ""
    bt = bt_inp.get() if bt_inp else ""
    prio = prio_inp.get() if prio_inp else ""
    io = io_inp.get() if io_inp else ""
    bt1 = bt1_inp.get() if bt1_inp else ""
    tq = tq_inp.get() if tq_inp else ""
    if tq:
        time_q = int(tq)
    if pid:
        pid_list.append(pid)
        pid_inp.focus_set()
    if at:
        at_list.append(at)
    if bt:
        bt_list.append(bt)
    if prio:
        prio_list.append(prio)
    if io:
        io_list.append(io)
    if bt1:
        bt1_list.append(bt1)
    if pid_inp:
        pid_inp.delete(0, tk.END)
    if at_inp:
        at_inp.delete(0, tk.END)
    if bt_inp:
        bt_inp.delete(0, tk.END)
    if prio_inp:
        prio_inp.delete(0, tk.END)
    if io_inp:
        io_inp.delete(0, tk.END)
    if bt1_inp:
        bt1_inp.delete(0, tk.END)
def d_w(ch):
    pid_list.clear()
    at_list.clear()
    bt_list.clear()
    prio_list.clear()
    io_list.clear()
    bt1_list.clear()
    pid_inp.focus_set()
    if(ch==1):
        b.destroy()
def c_b():
    sel = rso.get()
    if sel:
        global b, pid_inp, at_inp, bt_inp, prio_inp, io_inp, bt1_inp, tq_inp
        b = tk.Toplevel(a)
        b.title("Process Details")
        b.state('zoomed')
        b.configure(bg='#eab676')
        b1 = tk.Frame(b,bg='#eab676')
        b1.pack(side = 'top')
        b2 = tk.Frame(b,bg='#eab676')
        b2.pack(pady=50)
        b3 = tk.Frame(b,bg='#eab676')
        b3.pack(side='bottom')  
        algo = tk.Label(b1, text=f"Selected Algorithm: {sel}", font=hf,width=s)
        algo.pack(pady=20)
        if (sel in ("FCFS","SJF","LJF","HRRN","Non Preemptive Priority")) :
            mode = tk.Label(b1, text="Mode: Non-Preemptive", font=of,width=s)
        else:
            mode = tk.Label(b1, text="Mode: Preemptive", font=of,width=s)
        mode.pack()
        if (sel in ("SJF","SRTF","LJF","LRTF","SRTF with I/O Cycle")):
            criteria = tk.Label(b1, text="Criteria: Burst Time", font=of,width=s)
        elif (sel in ("Non Preemptive Priority","Preemptive Priority")):
            criteria = tk.Label(b1, text="Criteria: Priority", font=of,width=s)
        elif sel == "HRRN":
            criteria = tk.Label(b1, text="Criteria: Response Ratio", font=of,width=s)
        elif sel == "FCFS":
            criteria = tk.Label(b1, text="Criteria: Arrival Time", font=of,width=s)
        else:
            criteria = tk.Label(b1, text="Criteria: Time Quantum + Arrival Time", font=of,width=s)
        criteria.pack(pady=20)
        tq = tk.Label(b2, text="Enter Time Quantum",bg="#eab676", font =of)
        tq_inp = tk.Entry(b2)
        if sel == "RR":
            tq.grid(row = 0, column=0,padx=20,pady=10)
            tq_inp.focus_set()
            tq_inp.grid(row  = 0,column = 1,pady=10)
        pid = tk.Label(b2, text="Enter Process ID",bg="#eab676", font =of)
        pid.grid(row = 1, column=0,padx=20,pady=10)
        pid_inp = tk.Entry(b2)
        if sel != "RR":
            pid_inp.focus_set()
        pid_inp.grid(row  = 1,column = 1,pady=10)
        prio = tk.Label(b2, text="Enter Priority",bg="#eab676", font =of)
        prio_inp = tk.Entry(b2)
        if (sel in ("Non Preemptive Priority","Preemptive Priority")):
            prio.grid(row = 2, column=0,padx = 20,pady=10)
            prio_inp.grid(row  = 2,column = 1, pady=10)
        at = tk.Label(b2, text="Enter Arrival Time",bg="#eab676", font =of)
        at.grid(row = 3, column=0,padx=20,pady=10)
        at_inp = tk.Entry(b2)
        at_inp.grid(row  = 3,column = 1,pady=10)
        bt = tk.Label(b2, text="Enter Burst Time",bg="#eab676", font =of)
        bt.grid(row = 4, column=0,padx=20,pady=10)
        bt_inp = tk.Entry(b2)
        bt_inp.grid(row  = 4,column = 1,pady=10)
        io = tk.Label(b2, text="Enter I/O Time",bg="#eab676", font =of)
        io_inp = tk.Entry(b2)
        bt1 = tk.Label(b2, text="Enter Burst Time",bg="#eab676", font =of)
        bt1_inp = tk.Entry(b2)
        if sel == "SRTF with I/O Cycle":
            io.grid(row = 5, column=0,padx=20,pady=10)
            io_inp.grid(row  = 5,column = 1,pady=10)
            bt1.grid(row = 6, column=0,padx=20,pady=10)
            bt1_inp.grid(row  = 6,column = 1,pady=10)
        prio_b1 = tk.Button(b2,text='Higher No.', width=25,bg='white',fg='black', font=bf,command=lambda: set_prio(1))
        prio_b1.bind("<Return>", lambda event=None: prio_b1.invoke())
        prio_b2= tk.Button(b2,text='Lower No.', width=25,bg='white',fg='black', font=bf,command=lambda: set_prio(-1))
        prio_b2.bind("<Return>", lambda event=None: prio_b2.invoke())
        if (sel in ("Non Preemptive Priority","Preemptive Priority")):
            prio_b1.grid(row = 5, column=0,padx = 20)
            prio_b2.grid(row  = 5,column = 1)
        bb1 = tk.Button(b3,text='Add Process', width=25,bg='white',fg='black', font=bf,command=a_p)
        bb1.bind("<Return>", lambda event=None: bb1.invoke())
        bb1.pack(pady=20)
        bb2 = tk.Button(b3,text='Clear Processes', width=25,bg='white',fg='black', font=bf,command=lambda: d_w(0))
        bb2.bind("<Return>", lambda event=None: bb2.invoke())
        bb2.pack()
        bb3 = tk.Button(b3,text='Continue', width=25,bg='white',fg='black', font=bf,command=lambda: c_bb(sel))
        bb3.bind("<Return>", lambda event=None: bb3.invoke())
        bb3.pack(pady=20)
        bb4 = tk.Button(b3, text="Exit", width=25,bg='white',fg='black', font=bf,command=lambda: d_w(1))
        bb4.bind("<Return>", lambda event=None: bb4.invoke())
        bb4.pack()
a = tk.Tk()
a.configure(bg='#eab676')
a.state('zoomed')
a.title('Scheduling Algortihms')
s = a.winfo_screenwidth()
a1 = tk.Frame(a,bg='#eab676')
a1.pack(side = 'top')
a2 = tk.Frame(a,bg='#eab676')
a2.pack(side = 'bottom')
hf = font.Font(family="Helvetica", size=20, weight="bold")
bf = font.Font(family="Helvetica", size=14, weight="bold")
of = font.Font(family="Helvetica", size=16)
sf = font.Font(family="Helvetica", size=12)
rf = font.Font(family="Helvetica", size=14)
head = tk.Label(a1,text='PLEASE CHOOSE A SCHEDULING ALGORITHM', width=s, font=hf)
head.pack(pady=20)
rso = tk.StringVar()
c1 = tk.Radiobutton(a1,text ="First Come First Serve (FCFS)",font=of,bg='#eab676',variable=rso, value="FCFS")
c1.bind("<Return>", lambda event=None: c1.invoke())
c1.pack(pady=5)
c2 = tk.Radiobutton(a1,text ="Shortest Job First (SJF)",font=of,bg='#eab676',variable=rso, value="SJF")
c2.bind("<Return>", lambda event=None: c2.invoke())
c2.pack(pady=10)
c3 = tk.Radiobutton(a1,text ="Shortest Time Remaining First (SRTF)",font=of,bg='#eab676',variable=rso, value="SRTF")
c3.bind("<Return>", lambda event=None: c3.invoke())   
c3.pack(pady=10)
c4 = tk.Radiobutton(a1,text ="Round Robin (RR)",font=of,bg='#eab676',variable=rso, value="RR")
c4.bind("<Return>", lambda event=None: c4.invoke())
c4.pack(pady=10)
c5 = tk.Radiobutton(a1,text ="Longest Job First (LJF)",font=of,bg='#eab676',variable=rso, value="LJF")
c5.bind("<Return>", lambda event=None: c5.invoke())
c5.pack(pady=10)
c6 = tk.Radiobutton(a1,text ="Longest Time Remaining First (LRTF)",font=of,bg='#eab676',variable=rso, value="LRTF")
c6.bind("<Return>", lambda event=None: c6.invoke())
c6.pack(pady=10)
c7 = tk.Radiobutton(a1,text ="Highest Response Ratio Next (HRRN)",font=of,bg='#eab676',variable=rso, value="HRRN")
c7.bind("<Return>", lambda event=None: c7.invoke())
c7.pack(pady=10)
c8 = tk.Radiobutton(a1,text ="Non Preemptive Priority",font=of,bg='#eab676',variable=rso, value="Non Preemptive Priority")
c8.bind("<Return>", lambda event=None: c8.invoke())
c8.pack(pady=10)
c9 = tk.Radiobutton(a1,text ="Preemptive Priortiy",font=of,bg='#eab676',variable=rso, value="Preemptive Priority")
c9.bind("<Return>", lambda event=None: c9.invoke())
c9.pack(pady=10)
b1 = tk.Button(a2,text='Continue', width=25,bg='white',fg='black', font=bf,command=c_b)
b1.bind("<Return>",lambda event=None: b1.invoke())
b2= tk.Button(a2, text="Exit", width=25,bg='white',fg='black', font=bf,command=a.destroy)
b2.bind("<Return>", lambda event=None: b2.invoke())
b1.pack(pady=20)
b2.pack()
a.mainloop()
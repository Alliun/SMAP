import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime
import sys
import subprocess
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import talib as ta
from pandas_datareader import data as pdr
import yfinance as yf
import yahooquery as yq
import mysql.connector as msc
from sklearn.preprocessing import MinMaxScaler
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
yf.pdr_override()



root=tk.Tk()
root.geometry('710x780')
root.resizable(False,False)
root.title("MACHINE GUYS' STOCK MARKET APP")

signinhome=tk.Frame(root)
signinhome.grid(row=0,column=0,sticky='nsew')
signuphome=tk.Frame(root)
signuphome.grid(row=0,column=0,sticky='nsew')
forgothome=tk.Frame(root)
forgothome.grid(row=0,column=0,sticky='nsew')


mainhome=tk.Frame(root)
anlhome=tk.Frame(root)
sughome=tk.Frame(root)
prehome=tk.Frame(root)
helphome=tk.Frame(root)
prehome.grid(row=0,column=0,sticky='nsew')
mainhome.grid(row=0,column=0,sticky='nsew')
anlhome.grid(row=0,column=0,sticky='nsew')
sughome.grid(row=0,column=0,sticky='nsew')
helphome.grid(row=0,column=0,sticky='nsew')

sda=tk.Frame(root)
ssda=tk.Frame(root)
ca=tk.Frame(root)
smaa=tk.Frame(root)
rsia=tk.Frame(root)
adxa=tk.Frame(root)
macda=tk.Frame(root)
csea=tk.Frame(root)
sda.grid(row=0,column=0,sticky='nsew')
ssda.grid(row=0,column=0,sticky='nsew')
ca.grid(row=0,column=0,sticky='nsew')
smaa.grid(row=0,column=0,sticky='nsew')
rsia.grid(row=0,column=0,sticky='nsew')
adxa.grid(row=0,column=0,sticky='nsew')
macda.grid(row=0,column=0,sticky='nsew')
csea.grid(row=0,column=0,sticky='nsew')

signinhome.tkraise()

logo=Image.open('log.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(signinhome,image=logo)
logo_label.image=logo
logo_label.grid(column=2,row=0)



w0=tk.Label(signinhome,text="STOCK MARKET ANALYSIS AND PREDICTION MODEL", font=('Britannic',20),fg='black')
w0.grid(columnspan=3,column=1,row=1)
w1=tk.Label(signinhome,text="USER LOGIN", font=('Britannic',20),fg='black')
w1.grid(columnspan=3,column=1,row=2)

ce=Image.open('closeeye.png')
ce=ImageTk.PhotoImage(ce)

oe=Image.open('openeye.png')
oe=ImageTk.PhotoImage(oe)

def show():
    ce_label.config(image=oe)
    login_password_entry.config(show="")
    ce_label.config(command=hide)

def hide():
    ce_label.config(image=ce)
    login_password_entry.config(show="*")
    ce_label.config(command=show)

def show1():
    ce1_label.config(image=oe)
    registration_password_entry.config(show="")
    ce1_label.config(command=hide1)

def hide1():
    ce1_label.config(image=ce)
    registration_password_entry.config(show="*")
    ce1_label.config(command=show1)

def show2():
    ce2_label.config(image=oe)
    registration_cpassword_entry.config(show="")
    ce2_label.config(command=hide2)

def hide2():
    ce2_label.config(image=ce)
    registration_cpassword_entry.config(show="*")
    ce2_label.config(command=show2)

def show3():
    ce3_label.config(image=oe)
    forgot_password_entry.config(show="")
    ce3_label.config(command=hide3)

def hide3():
    ce3_label.config(image=ce)
    forgot_password_entry.config(show="*")
    ce3_label.config(command=show3)


def show4():
    ce4_label.config(image=oe)
    forgot_cpassword_entry.config(show="")
    ce4_label.config(command=hide4)

def hide4():
    ce4_label.config(image=ce)
    forgot_cpassword_entry.config(show="*")
    ce4_label.config(command=show4)

def signin():
    if login_username_entry.get()=='' or login_password_entry.get()=='' :
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=msc.connect(host='127.0.0.1',user='root',password='root',database='login')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database Connection Interrupted")
            return
        query='select * from userdata where username like %s and password like %s'
        mycursor.execute(query,(login_username_entry.get(),login_password_entry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error',"Invalid Username or Password")
        else:

            messagebox.showinfo("Success","Successful Login")
            
            mainhome.tkraise()

def switch():
    registration_username_entry.delete(0,tk.END)
    registration_email_entry.delete(0,tk.END)
    registration_password_entry.delete(0,tk.END)
    registration_cpassword_entry.delete(0,tk.END)
    signinhome.tkraise()

def switch1():
    login_username_entry.delete(0,tk.END)
    login_password_entry.delete(0,tk.END)
    signuphome.tkraise()

def switch3():
    forgot_username_entry.delete(0,tk.END)
    forgot_password_entry.delete(0,tk.END)
    forgot_cpassword_entry.delete(0,tk.END)
    signinhome.tkraise()
unv=tk.StringVar()                    
login_username_label = tk.Label(signinhome, text="Username:", font=("Helvetica", 18), fg="red")  
login_username_label.grid(columnspan=3,column=1,row=3)
login_username_entry = tk.Entry(signinhome, font=("Helvetica", 16),textvariable=unv)  
login_username_entry.grid(columnspan=3,column=1,row=4)
login_password_label = tk.Label(signinhome, text="Password:", font=("Helvetica", 18), fg="red")
login_password_label.grid(columnspan=3,column=1,row=5)
login_password_entry = tk.Entry(signinhome, show="*", font=("Helvetica", 16))
login_password_entry.grid(columnspan=3,column=1,row=6)
login_button = tk.Button(signinhome, text="Login",cursor='hand2', command=lambda: signin(), font=12, bg="black", fg="red")  
login_button.grid(columnspan=3,column=1,row=7)
forget_password_button = tk.Button(signinhome, text="Forgot Password ?",cursor='hand2', fg="red", bd=0, command=lambda: forgothome.tkraise())  
forget_password_button.grid(columnspan=3,column=1,row=8)
switch_to_registration_button = tk.Button(signinhome, text="NEW USER? Click here to SIGNUP!",cursor='hand2',font=12, fg="red", bd=0, command=lambda: switch1())  
switch_to_registration_button.grid(columnspan=3,column=1,row=9)


ce_label=tk.Button(signinhome,image=ce, cursor='hand2', command=show)
ce_label.place(x=497,y=371)


def signup():
    if registration_username_entry.get()=='' or registration_email_entry.get()=='' or registration_password_entry.get()=='' or registration_cpassword_entry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif registration_password_entry.get() != registration_cpassword_entry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif len(registration_password_entry.get())>10:
        messagebox.showerror('Error','Password must not exceed 10 characters')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        
        try:
            con=msc.connect(host='127.0.0.1',user='root',password='root',database='login')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database Connection Interrupted")
            return
        query='select * from userdata where username=%s'
        mycursor.execute(query,(registration_username_entry.get(),))
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username Already Exists')
        else:
        
            query='INSERT INTO userdata(username,password,emailid) VALUES(%s,%s,%s)'
            mycursor.execute(query,(registration_username_entry.get(),registration_cpassword_entry.get(),registration_email_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Successfully Registered")

            registration_username_entry.delete(0,tk.END)
            registration_email_entry.delete(0,tk.END)
            registration_password_entry.delete(0,tk.END)
            registration_cpassword_entry.delete(0,tk.END)
            signinhome.tkraise()

    


logo1=Image.open('log.png')
logo1=ImageTk.PhotoImage(logo1)
logo1_label=tk.Label(signuphome,image=logo1)
logo1_label.image=logo1
logo1_label.grid(column=2,row=0)

w00=tk.Label(signuphome,text="STOCK MARKET ANALYSIS AND PREDICTION MODEL", font=('Britannic',20),fg='black')
w00.grid(columnspan=3,column=1,row=1)
w01=tk.Label(signuphome,text="USER REGISTRATION", font=('Britannic',20),fg='black')
w01.grid(columnspan=3,column=1,row=2)
  
registration_username_label = tk.Label(signuphome, text="Username:", font=("Helvetica", 18), fg="red")  
registration_username_label.grid(columnspan=3,column=1,row=3)
registration_username_entry = tk.Entry(signuphome, font=("Helvetica", 16))  
registration_username_entry.grid(columnspan=3,column=1,row=4)
registration_email_label = tk.Label(signuphome, text="Email:", font=("Helvetica", 18), fg="red")  
registration_email_label.grid(columnspan=3,column=1,row=5)
registration_email_entry = tk.Entry(signuphome, font=("Helvetica", 16))  
registration_email_entry.grid(columnspan=3,column=1,row=6)
registration_password_label = tk.Label(signuphome, text="Password:", font=("Helvetica", 18), fg="red") 
registration_password_label.grid(columnspan=3,column=1,row=7)
registration_password_entry = tk.Entry(signuphome, show="*", font=("Helvetica", 16))  
registration_password_entry.grid(columnspan=3,column=1,row=8)
registration_cpassword_label = tk.Label(signuphome, text="Confirm Password:", font=("Helvetica", 18), fg="red")
registration_cpassword_label.grid(columnspan=3,column=1,row=9)
registration_cpassword_entry = tk.Entry(signuphome, show="*", font=("Helvetica", 16))  
registration_cpassword_entry.grid(columnspan=3,column=1,row=10)
registration_button = tk.Button(signuphome, text="Register!", command=lambda: signup(),cursor='hand2', font=12, bg="black", fg="red") 
registration_button.grid(columnspan=3,column=1,row=12)
switch_to_login_button = tk.Button(signuphome, text="ALREADY AN USER? Click here to SIGN IN!",cursor='hand2',font=12, fg="red", bd=0, command=lambda: switch() )  
switch_to_login_button.grid(columnspan=3,column=1,row=13)


ce1_label=tk.Button(signuphome,image=ce, cursor='hand2', command=show1)
ce1_label.place(x=497,y=428)
ce2_label=tk.Button(signuphome,image=ce, cursor='hand2', command=show2)
ce2_label.place(x=497,y=488)
check=tk.IntVar()
tacb=tk.Checkbutton(signuphome,text='I agree to the Terms & Conditions',variable=check,font=10,cursor='hand2')
tacb.grid(columnspan=3,column=1,row=11)

def changepass():
    if forgot_username_entry.get()=='' or forgot_password_entry.get()=='' or forgot_cpassword_entry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif forgot_password_entry.get() != forgot_cpassword_entry.get():
        messagebox.showerror('Error','Password Mismatch')
    else:
        try:
            con=msc.connect(host='127.0.0.1',user='root',password='root',database='login')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database Connection Interrupted")
            return
        query='select * from userdata where username like %s'
        mycursor.execute(query,(forgot_username_entry.get(),))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error',"Incorrect Username")
        else:
            query="update userdata set password=%s where username=%s"
            mycursor.execute(query,(forgot_cpassword_entry.get(),forgot_username_entry.get(),))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Password Successfully Changed")
            forgot_username_entry.delete(0,tk.END)
            
            forgot_password_entry.delete(0,tk.END)
            forgot_cpassword_entry.delete(0,tk.END)
            signinhome.tkraise()
            

logo2=Image.open('log.png')
logo2=ImageTk.PhotoImage(logo2)
logo2_label=tk.Label(forgothome,image=logo1)
logo2_label.image=logo1
logo2_label.grid(column=2,row=0)
w011=tk.Label(forgothome,text="STOCK MARKET ANALYSIS AND PREDICTION MODEL", font=('Britannic',20),fg='black')
w011.grid(columnspan=3,column=1,row=1)

w02=tk.Label(forgothome,text="FORGOT PASSWORD", font=('Britannic',20),fg='black')
w02.grid(columnspan=3,column=1,row=2)
  
forgot_username_label = tk.Label(forgothome, text="Username:", font=("Helvetica", 18), fg="red")  
forgot_username_label.grid(columnspan=3,column=1,row=3)
forgot_username_entry = tk.Entry(forgothome, font=("Helvetica", 16))  
forgot_username_entry.grid(columnspan=3,column=1,row=4)

forgot_password_label = tk.Label(forgothome, text="New Password:", font=("Helvetica", 18), fg="red") 
forgot_password_label.grid(columnspan=3,column=1,row=5)
forgot_password_entry = tk.Entry(forgothome, show="*", font=("Helvetica", 16))  
forgot_password_entry.grid(columnspan=3,column=1,row=6)
forgot_cpassword_label = tk.Label(forgothome, text="Confirm Password:", font=("Helvetica", 18), fg="red")
forgot_cpassword_label.grid(columnspan=3,column=1,row=7)
forgot_cpassword_entry = tk.Entry(forgothome, show="*", font=("Helvetica", 16))  
forgot_cpassword_entry.grid(columnspan=3,column=1,row=8)
forgot_button = tk.Button(forgothome, text="CHANGE!",command=changepass,cursor='hand2', font=12, bg="black", fg="red") 
forgot_button.grid(columnspan=3,column=1,row=9)
switch_to_login_button = tk.Button(forgothome, text="Back to Sign In",cursor='hand2',font=12, fg="red", bd=0, command=lambda: switch3() )  
switch_to_login_button.grid(columnspan=3,column=1,row=10)
ce3_label=tk.Button(forgothome,image=ce, cursor='hand2', command=show3)
ce3_label.place(x=497,y=370)
ce4_label=tk.Button(forgothome,image=ce, cursor='hand2', command=show4)
ce4_label.place(x=497,y=430)


#HOMEPAGE

w=tk.Label(mainhome,text="WELCOME!", font=('Britannic',20),fg='black')
w.grid(columnspan=3,column=0,row=0)
huv=tk.Label(mainhome,textvariable=unv,font=('Britannic',20),fg='red')
huv.place(x=380,y=0)

logo=Image.open('log.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(mainhome,image=logo)
logo_label.image=logo
logo_label.grid(column=2,row=1)


w1=tk.Label(mainhome,text="STOCK MARKET ANALYSIS AND PREDICTION MODEL", font=('Britannic',20),fg='black')
w1.grid(columnspan=3,column=1,row=2)
a=tk.Label(mainhome,text="SELECT AN ACTION TO EXECUTE", font='Raleway',fg='red')
a.grid(columnspan=3,column=1,row=3)


    

anl_txt=tk.StringVar()
anl_btn=tk.Button(mainhome,textvariable=anl_txt,bg='black',fg='red',height=2,width=40,command=lambda: anlhome.tkraise(), cursor='hand2')
anl_txt.set("ANALYSIS")
anl_btn.grid(column=2,row=4)
pre_txt=tk.StringVar()
pre_btn=tk.Button(mainhome,textvariable=pre_txt,bg='black',fg='red',height=2,width=40,command=lambda: prehome.tkraise(), cursor='hand2')
pre_txt.set("PREDICTION AND COMPARISON")
pre_btn.grid(column=2,row=5)
sug_txt=tk.StringVar()
sug_txt.set("STOCK ADVICE")
sug_btn=tk.Button(mainhome,textvariable=sug_txt,bg='black',fg='red',height=2,width=40,command=lambda: sughome.tkraise(), cursor='hand2')
sug_btn.grid(column=2,row=6)
H_txt=tk.StringVar()
H_txt.set("HELP")
H_btn=tk.Button(mainhome,textvariable=H_txt,bg='black',fg='red',height=2,width=40,command=lambda: helphome.tkraise(), cursor='hand2')
H_btn.grid(column=2,row=7)

def eb():
    login_username_entry.delete(0,tk.END)
    login_password_entry.delete(0,tk.END)
    signinhome.tkraise()
    
e_btn=tk.Button(mainhome,text='LOGOUT',command=eb,bg='black',fg='red',height=2,width=40, cursor='hand2')
e_btn.grid(column=2,row=8)


try:
    requests.get("http://www.google.com/")
except requests.ConnectionError:
    messagebox.showerror("Error","No Internet Connection,\n Connect to internet to download stocks")


#ANALYSIS MODEL

logoa=Image.open('log.png')
logoa=ImageTk.PhotoImage(logoa)
logoa_label=tk.Label(anlhome,image=logoa)
logoa_label.image=logoa
logoa_label.pack()

analysis=tk.Label(anlhome,text="STOCK MARKET ANALYSIS", font=('Britannic',20),fg='black')
analysis.pack()
si=tk.Label(anlhome,text="SELECT AN INDICATOR TO ANALYSE STOCK", font='Britannic',fg='blue')
si.pack()


a0_txt=tk.StringVar()
a0_btn=tk.Button(anlhome,textvariable=a0_txt,bg='black',fg='red',height=3,width=50,command=lambda: sda.tkraise(), cursor='hand2')
a0_txt.set("STOCK DATA")
a0_btn.pack()
a1_txt=tk.StringVar()
a1_btn=tk.Button(anlhome,textvariable=a1_txt,bg='black',fg='red',height=3,width=50,command=lambda: ca.tkraise(), cursor='hand2')
a1_txt.set("CLOSING PRICE")
a1_btn.pack()

a2_txt=tk.StringVar()
a2_btn=tk.Button(anlhome,textvariable=a2_txt,bg='black',fg='red',height=3,width=50,command=lambda: smaa.tkraise(), cursor='hand2')
a2_txt.set("SIMPLE MOVING AVERAGE OVER 100 AND 200 DAYS")
a2_btn.pack()

a3_txt=tk.StringVar()
a3_btn=tk.Button(anlhome,textvariable=a3_txt,bg='black',fg='red',height=3,width=50,command=lambda: rsia.tkraise(), cursor='hand2')
a3_txt.set("RELATIVE STRENGTH INDEX")
a3_btn.pack()

a4_txt=tk.StringVar()
a4_btn=tk.Button(anlhome,textvariable=a4_txt,bg='black',fg='red',height=3,width=50,command=lambda: macda.tkraise(), cursor='hand2')
a4_txt.set("MOVING AVERAGE CONVERGENCE DIVERGENCE")
a4_btn.pack()

a5_txt=tk.StringVar()
a5_btn=tk.Button(anlhome,textvariable=a5_txt,bg='black',fg='red',height=3,width=50,command=lambda: adxa.tkraise(), cursor='hand2')
a5_txt.set("AVERAGE DIRECTIONAL INDEX")
a5_btn.pack()
a6_txt=tk.StringVar()
a6_btn=tk.Button(anlhome,textvariable=a6_txt,bg='black',fg='red',height=3,width=50,command=lambda: csea.tkraise(), cursor='hand2')
a6_txt.set("CANDLESTICK CHART WITH ENGULFING PATTERN")
a6_btn.pack()

a7_txt=tk.StringVar()
a7_btn=tk.Button(anlhome,textvariable=a7_txt,bg='black',fg='red',height=3,width=50,command=lambda: mainhome.tkraise(), cursor='hand2')
a7_txt.set("BACK TO MAIN HOME")
a7_btn.pack()



def cin():
    window1=tk.Toplevel()
    window1.title('INTERPRETATION')
    cin_txt=tk.Text(window1,height=15,width=150)
    cin_txt.pack()
    cin_txt.insert(1.0,"Closing Price -\nThis is the last price of the stock at the end of the day. If this keeps going upside, it is a good sign, if it is going down, not so much.")

def smain():
    window2=tk.Toplevel()
    window2.title('INTERPRETATION')
    smain_txt=tk.Text(window2,height=30,width=150)
    smain_txt.pack()
    smain_txt.insert(1.0,"Simple Moving Average -\nIt is the average market price of any security over a specified period.\n It is referred to as the ‘moving’ average since it is plotted on a chart bar by bar and forms a line that moves along the chart as the average price changes.\n This is calculated by adding the price of a security over a period and then dividing that figure by the number of periods.\n Features of Simple Moving Average are as follows: \n \
a.	It is Customizable: Simple moving averages may be customized for different periods. A short-term investor may use a 10-day simple moving average to analyze short-term trends. On the contrary, a long-term investor may use a 200-day simple moving average. Typically, short-term simple moving averages respond faster to price fluctuations of the underlying security in comparison to long-term moving averages.\n \
b.	Volatility: A simple moving average also smooths out volatility. The longer the time horizon for the moving average, the smoother the simple moving average. The short-term moving average tends to be more volatile but the average is closer to the data source.\n \
c.	Lagging Indicator: A simple moving average is a lagging indicator since it is based on past price movements. The lag is directly proportional to the period of SMA. The longer the time of SMA, the higher the lag.")

def rsiin():
    window3=tk.Toplevel()
    window3.title('INTERPRETATION')
    rsiin_txt=tk.Text(window3,height=30,width=150)
    rsiin_txt.pack()
    rsiin_txt.insert(1.0,"Relative Strength Index -\nIt is the speed and magnitude of a security's recent price changes to evaluate overvalued or undervalued conditions in the price \
of that security. \nThe RSI is displayed as an oscillator (a line graph) on a scale of zero to 100. As a momentum indicator, the relative strength index compares a \
security's strength on days when prices go up to its strength on days when prices go down.\n Relating the result of this comparison to price action can give traders \
an idea of how a security may perform. The RSI, used in conjunction with other technical indicators, can help traders make better-informed trading decisions.\n \
An asset is usually considered overbought when the RSI is above 70 and oversold when it is below 30.\n An RSI divergence occurs when price moves in the opposite \
direction of the RSI. In other words, a chart might display a change in momentum before a corresponding change in price.\n A bullish divergence occurs when the RSI \
displays an oversold reading followed by a higher low that appears with lower lows in the price. This may indicate rising bullish momentum, and a break above oversold \
territory could be used to trigger a new long position.\n A bearish divergence occurs when the RSI creates an overbought reading followed by a lower high that appears \
with higher highs on the price.")

def macdin():
    window4=tk.Toplevel()
    window4.title('INTERPRETATION')
    macdin_txt=tk.Text(window4,height=30,width=150)
    macdin_txt.pack()
    macdin_txt.insert(1.0,"Moving Average Convergence Divergence -\nThe moving average convergence divergence (MACD) indicator helps traders see the trend direction, as well as the momentum of that trend. It also provides a number of trade signals. \
When the MACD is above zero, the price is in an upward phase. If the MACD is below zero, it has entered a bearish period. \n \
The indicator is composed of two lines: the MACD line and a signal line, which moves slower. When MACD crosses below the signal line, it indicates that the price is falling. When the MACD line crosses above the signal line, the price is rising. \n \
MACD is often displayed with a histogram (see the chart below) that graphs the distance between MACD and its signal line. If MACD is above the signal line, the histogram will be above the MACD’s baseline, or zero line. If MACD is below its signal line, the histogram will be below the MACD’s baseline. Traders use the MACD’s histogram to identify when bullish or bearish momentum is high—and possibly for overbought/oversold signals. \n \
The Moving Average Convergence Divergence (MACD) indicator is used to determine trend direction, its strength as well as a possible reversal. When the MACD and ADX are combined, the former is best utilised to detect reversals, with the latter qualifying them. \n \
Investors following MACD crossovers and divergences should double-check with the ADX before making a trade on an MACD signal. For example, while MACD may be showing a bearish divergence, a check of the ADX may tell you that a trend higher is in place—in which case you would avoid the bearish MACD trade signal and wait to see how the market develops over the next few days. \n \
On the other hand, if MACD is showing a bearish crossover and the ADX is in non-trending territory (<25) and has likely shown a peak and reversal on its own, you could have good cause to take the bearish trade.")
    

def adxin():
    window5=tk.Toplevel()
    window5.title('INTERPRETATION')
    adxin_txt=tk.Text(window5,height=30,width=100)
    adxin_txt.pack()
    adxin_txt.insert(1.0,"Average Directional Index -\nThe average directional index (ADX) is a trend indicator used to measure the strength and momentum of a trend. When the ADX is above 40, the trend is considered to have a lot of directional strength, either up or down, depending on the direction the price is moving. \n \
When the ADX indicator is below 20, the trend is considered to be weak or non-trending. The Moving Average Convergence Divergence (MACD) indicator is used to determine trend direction, its strength as well as a possible reversal. When the MACD and ADX are combined, the former is best utilised to detect reversals, with the latter qualifying them. \n \
Investors following MACD crossovers and divergences should double-check with the ADX before making a trade on an MACD signal. For example, while MACD may be showing a bearish divergence, a check of the ADX may tell you that a trend higher is in place—in which case you would avoid the bearish MACD trade signal and wait to see how the market develops over the next few days. \n \
On the other hand, if MACD is showing a bearish crossover and the ADX is in non-trending territory (<25) and has likely shown a peak and reversal on its own, you could have good cause to take the bearish trade. \
")

def csein():
    window6=tk.Toplevel()
    window6.title('INTERPRETATION')
    csein_txt=tk.Text(window6,height=40,width=100)
    csein_txt.pack()
    csein_txt.insert(1.0,"CandleStick Chart Analysing Engulfing Pattern - \n Candlestick charts are a technical tool that packs data for multiple time frames into single price bars.\n This makes them more useful than traditional open, high, low, and close (OHLC) bars or simple lines that connect the dots of closing prices. \n \
Candlesticks build patterns that may predict price direction once completed. Proper color coding adds depth to this technical tool, which dates back to 18th-century Japanese rice traders. A daily candlestick represents a market’s opening, high, low, and closing (OHLC) prices. \n \
The rectangular real body, or just body, is colored with a dark color (red or black) for a drop in price and a light color (green or white) for a price increase. The lines above and below the body are referred to as wicks or tails, and they represent the day’s maximum high and low. \n \
Taken together, the parts of the candlestick can frequently signal changes in a market’s direction or highlight significant potential moves that frequently must be confirmed by the next day’s candle. \n \
There are various patterns in candlestick statistics, in our project we show the engulfing pattern. \n \
An engulfing line is a strong indicator of a directional change. A bearish engulfing line is a reversal pattern after an uptrend. The key is that the second candle’s body 'engulfs' the prior day’s body in the opposite direction. This suggests that, in the case of an uptrend, the buyers had a brief attempt higher but finished the day well below the close of the prior candle. This suggests that the uptrend is stalling and has begun to reverse lower. \n \
A bullish engulfing line is the corollary pattern to a bearish engulfing line, and it appears after a downtrend. Also, a double bottom, or tweezers bottom, is the corollary formation that suggests a downtrend may be ending and set to reverse higher. \n \
Bearish Engulfing Pattern \n \
A bearish engulfing pattern develops in an uptrend when sellers outnumber buyers. This action is reflected by a long red (black) real body engulfing a small green (white) real body. The pattern indicates that sellers are back in control and that the price could continue to decline. \n \
Bullish Engulfing Pattern\n \
An engulfing pattern on the bullish side of the market takes place when buyers outpace sellers. This is reflected in the chart by a long white real body engulfing a small black real body. With bulls having established some control, the price could head higher.")


def b1(t):
    anlhome.tkraise()
    t.delete(0,tk.END)
    d_txt.delete(1.0,tk.END)

def bsa(t,d):
    sda.tkraise()
    t.delete(0,tk.END)
    dsda_txt.delete(1.0,tk.END)
    d.delete(0,tk.END)
    
    

def back(t,s,e):
    anlhome.tkraise()
    t.delete(0,tk.END)
    s.delete(0,tk.END)
    e.delete(0,tk.END)
    

def df():
    ticker=T.get()
    if not ticker.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock=pdr.DataReader(ticker)
        d_txt.delete(1.0,tk.END)

        d_txt.insert(tk.END,stock)

def gsdsa():
    tickersda=Tsda.get()
    sdsda=Tsdta.get()
    if not tickersda.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif tickersda.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    elif not sdsda.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    else:
        date_object = datetime.datetime.strptime(sdsda, "%Y-%m-%d")
        new_date_object = date_object + datetime.timedelta(days=1)
        new_date_string = datetime.datetime.strftime(new_date_object, "%Y-%m-%d")
        stock=pdr.DataReader(tickersda,sdsda,new_date_string)
        dsda_txt.delete(1.0,tk.END)

        dsda_txt.insert(tk.END,stock)
    
        
        
        

w0=tk.Label(sda,text="STOCK DATA ANALYSIS", font=('Britannic',20),fg='black')
w0.pack()
a_=tk.Label(sda,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a_.pack()
T=tk.Entry(sda,width=30)
T.pack()
s_btn=tk.Button(sda,text="SUBMIT!",command=lambda: df(),bg='black',fg='red',height=1,width=10, cursor='hand2')
s_btn.pack()
e_btn=tk.Button(sda,text='BACK',command=lambda: b1(T),bg='black',fg='red',height=1,width=10, cursor='hand2')
e_btn.pack()
d_lbl1=tk.Label(sda,text="\n\nSTOCKS AVAILABLE FROM THE BELOW GIVEN-\n",fg="red",font=15)
d_lbl1.pack()
d_txt=tk.Text(sda,height=15,width=80)
d_txt.pack()
d_lbl2=tk.Label(sda,text="\nSTOCKS AVAILABLE TILL THE ABOVE GIVEN (UPTO DATE) -",fg="red",font=15)
d_lbl2.pack()
g_label=tk.Label(sda,text="STOCK DATA ON A SPECIFIC DATE", font='Britannic',fg='black')
g_label.pack()
g_btn=tk.Button(sda,text="CLICK HERE!",command=lambda: ssda.tkraise(),bg='black',fg='red',height=1,width=15, cursor='hand2')
g_btn.pack()

gw0=tk.Label(ssda,text="STOCK DATA ANALYSIS", font=('Britannic',20),fg='black')
gw0.pack()
ssmda_=tk.Label(ssda,text="ENTER STOCK TICKER", font='Raleway',fg='red')
ssmda_.pack()
Tsda=tk.Entry(ssda,width=30)
Tsda.pack()
ssmdDa_=tk.Label(ssda,text="ENTER DATE (YYYY-MM-DD)", font='Raleway',fg='red')
ssmdDa_.pack()
Tsdta=tk.Entry(ssda,width=30)
Tsdta.pack()
s_btn=tk.Button(ssda,text="SUBMIT!",command=lambda: gsdsa(),bg='black',fg='red',height=1,width=10, cursor='hand2')
s_btn.pack()
e_btn=tk.Button(ssda,text='BACK',command=lambda: bsa(Tsda,Tsdta),bg='black',fg='red',height=1,width=10, cursor='hand2')
e_btn.pack()
dsda_txt=tk.Text(ssda,height=10,width=80)
dsda_txt.pack()

def close():
    ticker1=T1.get()
    sd1=S1.get()
    ed1=E1.get()
    if not ticker1.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not sd1.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not ed1.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker1.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock1=pdr.DataReader(ticker1,sd1,ed1)
        g=tk.Frame(root)
        g.grid(row=0,column=0,sticky='nsew')
        g.tkraise()
        fig, axs=plt.subplots()
        axs.plot(stock1['Close'],label='CLOSING PRICE')
        plt.title("CLOSING PRICE ANALYSIS")
        plt.legend()
        canvas1 = FigureCanvasTkAgg(fig,master=g)   
        canvas1.get_tk_widget().pack() 

        toolbar1 = NavigationToolbar2Tk(canvas1,g,pack_toolbar=False) 
        toolbar1.update() 
        toolbar1.pack(anchor='w',fill=tk.X)
        canvas1.draw()
        c1_btn=tk.Button(g,text="INTERPRET!",command=lambda: cin(), bg='black',fg='red',height=1,width=10, cursor='hand2')
        c1_btn.place(x=400,y=550)
        eg1_btn=tk.Button(g,text='BACK!',command=lambda: ca.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
        eg1_btn.place(x=500,y=550)

        
w1=tk.Label(ca,text="CLOSING PRICE ANALYSIS", font=('Britannic',20),fg='black')
w1.pack()
a1_=tk.Label(ca,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a1_.pack()
T1=tk.Entry(ca,width=30)
T1.pack()
b1_=tk.Label(ca,text="ENTER START DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
b1_.pack()
S1=tk.Entry(ca,width=30)
S1.pack()
c1_=tk.Label(ca,text="ENTER END DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
c1_.pack()
E1=tk.Entry(ca,width=30)
E1.pack()
s1_btn=tk.Button(ca,text="PLOT!",command=close,bg='black',fg='red',height=1,width=10, cursor='hand2')
s1_btn.pack()

e1_btn=tk.Button(ca,text='BACK!',command=lambda: back(T1,S1,E1),bg='black',fg='red',height=1,width=10, cursor='hand2')
e1_btn.pack()

def SMA():
    ticker2=T2.get()
    sd2=S2.get()
    ed2=E2.get()
    if not ticker2.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not sd2.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not ed2.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker2.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock2=pdr.DataReader(ticker2,sd2,ed2)
        g0=tk.Frame(root)
        g0.grid(row=0,column=0,sticky='nsew')
        g0.tkraise()
        fig, axs = plt.subplots()
        stock2['SMA_100'] = ta.SMA(stock2['Close'],100)
        stock2['SMA_200'] = ta.SMA(stock2['Close'],200)
        axs.plot(stock2['Close'],label='CLOSING PRICES')
        axs.plot(stock2['SMA_200'],label='SMA_200')
        axs.plot(stock2['SMA_100'],label='SMA_100')
        plt.title("CLOSE VS SIMPLE MOVING AVERAGE OVER 100 DAYS VS SMA OVER 200 DAYS")
        plt.legend()
        canvas2 = FigureCanvasTkAgg(fig,master=g0)   
        canvas2.get_tk_widget().pack() 

        toolbar2 = NavigationToolbar2Tk(canvas2,g0,pack_toolbar=False) 
        toolbar2.update() 
        toolbar2.pack(anchor='w',fill=tk.X)
        canvas2.draw()
        c2_btn=tk.Button(g0,text="INTERPRET!",bg='black',fg='red',height=1,width=10, cursor='hand2', command=smain)
        c2_btn.place(x=400,y=550)
        eg2_btn=tk.Button(g0,text='BACK!',command=lambda: smaa.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
        eg2_btn.place(x=500,y=550)

        
w2=tk.Label(smaa,text="SIMPLE MOVING AVERAGE ANALYSIS", font=('Britannic',20),fg='black')
w2.pack()
a2_=tk.Label(smaa,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a2_.pack()
T2=tk.Entry(smaa,width=30)
T2.pack()
b2_=tk.Label(smaa,text="ENTER START DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
b2_.pack()
S2=tk.Entry(smaa,width=30)
S2.pack()
c2_=tk.Label(smaa,text="ENTER END DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
c2_.pack()
E2=tk.Entry(smaa,width=30)
E2.pack()
s2_btn=tk.Button(smaa,text="PLOT!",command=SMA,bg='black',fg='red',height=1,width=10, cursor='hand2')
s2_btn.pack()

e2_btn=tk.Button(smaa,text='BACK!',command=lambda: back(T2,S2,E2),bg='black',fg='red',height=1,width=10, cursor='hand2')
e2_btn.pack()

def RSI():
    ticker3=T3.get()
    sd3=S3.get()
    ed3=E3.get()
    if not ticker3.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not sd3.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not ed3.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker3.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock3=pdr.DataReader(ticker3,sd3,ed3)
        stock3['RSI']=ta.RSI(stock3['Close'])
        g1=tk.Frame(root)
        g1.grid(row=0,column=0,sticky='nsew')
        g1.tkraise()
        fig, axs=plt.subplots(2,1,gridspec_kw={"height_ratios":[4,3]}, figsize=(7,7))
        axs[0].plot(stock3['Close'],color='k',label='CLOSING PRICES')
        axs[1].axhline(y=70,color='r')
        axs[1].axhline(y=30,color='g')
        axs[1].plot(stock3['RSI'],label='RSI')
        plt.title("RELATIVE STRENGTH INDEX ANALYSIS")
        plt.legend()
        canvas3 = FigureCanvasTkAgg(fig,master=g1)   
        canvas3.get_tk_widget().pack() 

        toolbar3 = NavigationToolbar2Tk(canvas3,g1,pack_toolbar=False) 
        toolbar3.update() 
        toolbar3.pack(anchor='w',fill=tk.X)
        canvas3.draw()
        c3_btn=tk.Button(g1,text="INTERPRET!",bg='black',fg='red',height=1,width=10, cursor='hand2',command=rsiin)
        c3_btn.place(x=400,y=700)
        eg3_btn=tk.Button(g1,text='BACK!',command=lambda: rsia.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
        eg3_btn.place(x=500,y=700)

        
w3=tk.Label(rsia,text="RELATIVE STRENGTH INDEX ANALYSIS", font=('Britannic',20),fg='black')
w3.pack()
a3_=tk.Label(rsia,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a3_.pack()
T3=tk.Entry(rsia,width=30)
T3.pack()
b3_=tk.Label(rsia,text="ENTER START DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
b3_.pack()
S3=tk.Entry(rsia,width=30)
S3.pack()
c3_=tk.Label(rsia,text="ENTER END DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
c3_.pack()
E3=tk.Entry(rsia,width=30)
E3.pack()
s3_btn=tk.Button(rsia,text="PLOT!",command=RSI,bg='black',fg='red',height=1,width=10, cursor='hand2')
s3_btn.pack()
e3_btn=tk.Button(rsia,text='BACK!',command=lambda: back(T3,S3,E3),bg='black',fg='red',height=1,width=10, cursor='hand2')
e3_btn.pack()


def MACD():
    ticker4=T4.get()
    sd4=S4.get()
    ed4=E4.get()
    if not ticker4.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not sd4.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not ed4.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker4.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock4=pdr.DataReader(ticker4,sd4,ed4)
        macd, macd_signal, macd_hist = ta.MACD(stock4['Close'])
        g2=tk.Frame(root)
        g2.grid(row=0,column=0,sticky='nsew')
        g2.tkraise()
        fig, axs=plt.subplots(2,1,gridspec_kw={"height_ratios":[4,3]}, figsize=(7,7))
        x=['red' if i<0 else 'green' for i in macd_hist]
        axs[0].plot(stock4['Close'],color='k',label='CLOSING PRICES')
        axs[1].plot(macd,label='MACD')
        axs[1].plot(macd_signal,'--',label='MACD_SIGNAL')
        axs[1].bar(macd_hist.index,macd_hist,color=x,label='MACD_HIST')
        plt.title("MOVING AVERAGE CONVERGENCE DIVERGENCE ANALYSIS")
        plt.legend(loc='best')
        canvas4 = FigureCanvasTkAgg(fig,master=g2)   
        canvas4.get_tk_widget().pack() 

        toolbar4 = NavigationToolbar2Tk(canvas4,g2,pack_toolbar=False) 
        toolbar4.update() 
        toolbar4.pack(anchor='w',fill=tk.X)
        canvas4.draw()
        c4_btn=tk.Button(g2,text="INTERPRET!",bg='black',fg='red',height=1,width=10, cursor='hand2',command=macdin)
        c4_btn.place(x=400,y=700)
        eg4_btn=tk.Button(g2,text='BACK!',command=lambda: macda.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
        eg4_btn.place(x=500,y=700)

        
w4=tk.Label(macda,text="MOVING AVERAGE CONVERGENCE DIVERGENCE ANALYSIS", font=('Britannic',16),fg='black')
w4.pack()
a4_=tk.Label(macda,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a4_.pack()
T4=tk.Entry(macda,width=30)
T4.pack()
b4_=tk.Label(macda,text="ENTER START DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
b4_.pack()
S4=tk.Entry(macda,width=30)
S4.pack()
c4_=tk.Label(macda,text="ENTER END DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
c4_.pack()
E4=tk.Entry(macda,width=30)
E4.pack()
s4_btn=tk.Button(macda,text="PLOT!",command=lambda: MACD(),bg='black',fg='red',height=1,width=10, cursor='hand2')
s4_btn.pack()
e4_btn=tk.Button(macda,text='BACK!',command=lambda: back(T4,S4,E4),bg='black',fg='red',height=1,width=10, cursor='hand2')
e4_btn.pack()


def ADX():
    ticker5=T5.get()
    sd5=S5.get()
    ed5=E5.get()
    if not ticker5.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not sd5.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not ed5.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker5.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock5=pdr.DataReader(ticker5,sd5,ed5)
        adx= ta.ADX(stock5['High'],stock5['Low'],stock5['Close'])
        g3=tk.Frame(root)
        g3.grid(row=0,column=0,sticky='nsew')
        g3.tkraise()
        fig, axs=plt.subplots(2,1,gridspec_kw={"height_ratios":[4,3]}, figsize=(7,7))
        axs[0].plot(stock5['Close'],color='k',label='CLOSING PRICES')
        axs[1].axhline(y=40,color='r')
        axs[1].axhline(y=20,color='g')
        axs[1].plot(adx,label='ADX')
        plt.title("AVERAGE DIRECTIONAL INDEX ANALYSIS")
        plt.legend()
        canvas5 = FigureCanvasTkAgg(fig,master=g3)   
        canvas5.get_tk_widget().pack() 

        toolbar5 = NavigationToolbar2Tk(canvas5,g3,pack_toolbar=False) 
        toolbar5.update() 
        toolbar5.pack(anchor='w',fill=tk.X)
        canvas5.draw()
        c5_btn=tk.Button(g3,text="INTERPRET!",bg='black',fg='red',height=1,width=10, cursor='hand2',command=adxin)
        c5_btn.place(x=400,y=700)
        eg5_btn=tk.Button(g3,text='BACK!',command=lambda: adxa.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
        eg5_btn.place(x=500,y=700)

        
w5=tk.Label(adxa,text="AVERAGE DIRECTIONAL INDEX ANALYSIS", font=('Britannic',20),fg='black')
w5.pack()
a5_=tk.Label(adxa,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a5_.pack()
T5=tk.Entry(adxa,width=30)
T5.pack()
b5_=tk.Label(adxa,text="ENTER START DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
b5_.pack()
S5=tk.Entry(adxa,width=30)
S5.pack()
c5_=tk.Label(adxa,text="ENTER END DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
c5_.pack()
E5=tk.Entry(adxa,width=30)
E5.pack()
s5_btn=tk.Button(adxa,text="PLOT!",command=ADX,bg='black',fg='red',height=1,width=10, cursor='hand2')
s5_btn.pack()


e5_btn=tk.Button(adxa,text='BACK!',command=lambda: back(T5,S5,E5),bg='black',fg='red',height=1,width=10, cursor='hand2')
e5_btn.pack()



def CSE():
    ticker6=T6.get()
    sd6=S6.get()
    ed6=E6.get()
    if not ticker6.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not sd6.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif not ed6.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    elif ticker6.islower():
        messagebox.showerror("Error", "Entry cannot contain all lower case letters.")
        return False
    else:
        stock6=pdr.DataReader(ticker6,sd6,ed6)
        stock6['ENGULFING']=ta.CDLENGULFING(stock6['Open'],stock6['Close'],stock6['High'],stock6['Low'])
        g4=tk.Frame(root)
        g4.grid(row=0,column=0,sticky='nsew')
        g4.tkraise()
        fig, axs=plt.subplots(2,1,gridspec_kw={"height_ratios":[4,3]}, figsize=(7,7))
        c=mpf.make_marketcolors(up='green',down='red')
        mpf_style=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=c)
        mpf.plot(stock6,type='candle',style=mpf_style,ax=axs[0])
        axs[1].plot(stock6['ENGULFING'],label='ENGULFING')
        plt.title("CANDLESTICK CHART WITH ENGULFING PATTERN ANALYSIS")
        plt.legend()
        canvas6 = FigureCanvasTkAgg(fig,master=g4)   
        canvas6.get_tk_widget().pack() 

        toolbar6 = NavigationToolbar2Tk(canvas6,g4,pack_toolbar=False) 
        toolbar6.update() 
        toolbar6.pack(anchor='w',fill=tk.X)
        canvas6.draw()
        c4_btn=tk.Button(g4,text="INTERPRET!",bg='black',fg='red',height=1,width=10, cursor='hand2',command=csein)
        c4_btn.place(x=400,y=700)
        eg4_btn=tk.Button(g4,text='BACK!',command=lambda: csea.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
        eg4_btn.place(x=500,y=700)

        
w6=tk.Label(csea,text="CANDLESTICK CHART WITH ENGULFING PATTERN ANALYSIS", font=('Britannic'),fg='black')
w6.pack()
d1_txt=tk.Text(csea,height=3,width=70,fg='yellow',bg='black')
d1_txt.insert(1.0,'WARNING: IF YOU PROVIDE A LARGE TIME PERIOD OF DATA IT MAY NOT BE\n POSSIBLE TO SEE DETAILS OF THE CANDLES ')
d1_txt.pack()
a6_=tk.Label(csea,text="ENTER STOCK TICKER", font='Raleway',fg='red')
a6_.pack()
T6=tk.Entry(csea,width=30)
T6.pack()
b6_=tk.Label(csea,text="ENTER START DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
b6_.pack()
S6=tk.Entry(csea,width=30)
S6.pack()
c6_=tk.Label(csea,text="ENTER END DATE(YYYY-MM-DD) OF STOCKS TO BE TAKEN", font='Raleway',fg='red')
c6_.pack()
E6=tk.Entry(csea,width=30)
E6.pack()
s6_btn=tk.Button(csea,text="PLOT!",command=CSE,bg='black',fg='red',height=1,width=10, cursor='hand2')
s6_btn.pack()


e6_btn=tk.Button(csea,text='BACK!',command=lambda: back(T6,S6,E6),bg='black',fg='red',height=1,width=10, cursor='hand2')
e6_btn.pack()




#PREDICTION AND COMPARISON MODEL

def prefu():
    subprocess.call(['streamlit', 'run', 'MG_STOCK_FORCAST_MODEL.py'])

def pc():
    subprocess.call(['streamlit', 'run', 'MG_STOCK_COMPARISON_MODEL.py'])

logop=Image.open('log.png')
logop=ImageTk.PhotoImage(logop)
logop_label=tk.Label(prehome,image=logop)
logop_label.image=logop
logop_label.pack()

precom=tk.Label(prehome,text="STOCK MARKET PREDICTION", font=('Britannic',20),fg='black')
precom.pack()
pi=tk.Label(prehome,text="SELECT AN OPTION TO EXECUTE", font='Britannic',fg='blue')
pi.pack()

p1_btn=tk.Button(prehome,text="PREDICT FUTURE PRICES",command=lambda: prefu(),bg='black',fg='red',height=3,width=50, cursor='hand2')
p1_btn.pack()
p2_btn=tk.Button(prehome,text="COMPARE PREDICTIONS",bg='black',fg='red',height=3,width=50,command=lambda: pc(), cursor='hand2')
p2_btn.pack()

p7_txt=tk.StringVar()
p7_btn=tk.Button(prehome,textvariable=a7_txt,bg='black',fg='red',height=3,width=50,command=lambda: mainhome.tkraise(), cursor='hand2')
p7_txt.set("BACK TO MAIN HOME")
p7_btn.pack()


#HELP - GET STOCK TICKER

logoh=Image.open('log.png')
logoh=ImageTk.PhotoImage(logoh)
logoh_label=tk.Label(helphome,image=logoh)
logoh_label.image=logoh
logoh_label.pack()

def b2(x):
    mainhome.tkraise()
    x.delete(0,tk.END)
    dh_txt.delete(1.0,tk.END)

def gett():
    quotes=HE5.get()
    if not quotes.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    else:
        preferred_exchange='AMS'

        try:
            data = yq.search(quotes)
        except ValueError:
            print(query)
        else:
            quotes = data['quotes']
            if len(quotes) == 0:
                print('No Symbol Found')

            symbol = quotes[0]['symbol']
            for quote in quotes:
                if quote['exchange'] == preferred_exchange:
                    symbol = quote['symbol']
                    break
            dh_txt.delete(1.0,tk.END)

            dh_txt.insert(tk.END,symbol)
            
            

hla=tk.Label(helphome,text="GET STOCK TICKER!", font=('Britannic',20),fg='black')
hla.pack()

H5_=tk.Label(helphome,text="ENTER COMPANY'S FULL NAME", font='Raleway',fg='red')
H5_.pack()
HE5=tk.Entry(helphome,width=40)
HE5.pack()

HE_btn=tk.Button(helphome,text="SUBMIT!",command=lambda: gett(),bg='black',fg='red',height=1,width=10, cursor='hand2')
HE_btn.pack()
eH_btn=tk.Button(helphome,text='BACK',command=lambda: b2(HE5),bg='black',fg='red',height=1,width=10, cursor='hand2')
eH_btn.pack()
H6_=tk.Label(helphome,text="STOCK TICKER:",fg='red')
H6_.pack()
dh_txt=tk.Text(helphome,height=2,width=20)
dh_txt.pack()


def back1(t):
    mainhome.tkraise()
    t.delete(0,tk.END)
    dsa_txt.delete(1.0,tk.END)

def sugrec():
    tickersug=Ts3.get()
    if not tickersug.strip():
        messagebox.showerror("Error", "Entry cannot be empty.")
        return False
    else:
        data=pdr.DataReader(tickersug,'2021-01-01')
        def calculate_moving_average(data, window):
            return data['Close'].rolling(window=window).mean()
        short_window = calculate_moving_average(data, 50)
        long_window = calculate_moving_average(data, 200)
        def plot_stock_data(data, short_window, long_window):
            gsa=tk.Frame(root)
            gsa.grid(row=0,column=0,sticky='nsew')
            gsa.tkraise()
            fig, axs = plt.subplots()
            axs.plot(data['Close'], label='Close Price', alpha=0.5)
            axs.plot(short_window, label='Short Term Moving Average')
            axs.plot(long_window, label='Long Term Moving Average')
            axs.fill_between(short_window.index, short_window, long_window, where=(short_window >= long_window), alpha=0.3, label='Buy Signal')
            axs.fill_between(short_window.index, short_window, long_window, where=(short_window <= long_window), alpha=0.3, label='Sell Signal')
            plt.title(f'Stock Recommendation')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend(loc='best')
            canvassa = FigureCanvasTkAgg(fig,master=gsa)   
            canvassa.get_tk_widget().pack() 

            toolbarsa = NavigationToolbar2Tk(canvassa,gsa,pack_toolbar=False) 
            toolbarsa.update() 
            toolbarsa.pack(anchor='w',fill=tk.X)
            canvassa.draw()
            egsa_btn=tk.Button(gsa,text='BACK!',command=lambda: sughome.tkraise(),bg='black',fg='red',height=1,width=10, cursor='hand2')
            egsa_btn.place(x=500,y=550)
        def recommend_stock(data, short_window, long_window):
            if short_window[-1] > long_window[-1]:
                return 'Buy'
            elif short_window[-1] < long_window[-1]:
                return 'Sell'
            else:
                return 'Hold'
        plot_stock_data(data, short_window, long_window)
        dsa_txt.delete(1.0,tk.END)

        dsa_txt.insert(tk.END,recommend_stock(data, short_window, long_window))
    
    

logosa=Image.open('log.png')
logosa=ImageTk.PhotoImage(logosa)
logosa_label=tk.Label(sughome,image=logoa)
logosa_label.image=logosa
logosa_label.pack()

suggestion=tk.Label(sughome,text="STOCK MARKET ANALYSIS", font=('Britannic',20),fg='black')
suggestion.pack()
sir=tk.Label(sughome,text="RECOMMENDATION MODEL", font='Britannic',fg='blue')
sir.pack()
sa3_=tk.Label(sughome,text="ENTER STOCK TICKER", font='Raleway',fg='red')
sa3_.pack()
Ts3=tk.Entry(sughome,width=30)
Ts3.pack()

sa2_btn=tk.Button(sughome,text="SUGGEST!",command= lambda: sugrec(), bg='black',fg='red',height=1,width=10, cursor='hand2')
sa2_btn.pack()

e2_btn=tk.Button(sughome,text='BACK!',command=lambda: back1(Ts3),bg='black',fg='red',height=1,width=10, cursor='hand2')
e2_btn.pack()
sir2=tk.Label(sughome,text="RECOMMENDATION :", font='Britannic',fg='black')
sir2.pack()
dsa_txt=tk.Text(sughome,height=2,width=20)
dsa_txt.pack()


root.mainloop()

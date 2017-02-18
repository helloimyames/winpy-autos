import os
import pywinauto
import time

file = open('H:/python/p.txt','r')

user = file.readlines()[1]
password = file.readlines()[3]
g_password = file.readlines()[2]
os.startfile('C:/Users/jxdeani/Downloads/receiverconfig.cr')


w = pywinauto.findwindows.find_windows(title_re = r'Citrix Receiver*')
win_num = int(len(w))
app = pywinauto.application.Application()

while win_num < 1:
    time.sleep(1)
    w = pywinauto.findwindows.find_windows(title_re = r'Citrix Receiver*')
    win_num = int(len(w))

window = app['Citrix Receiver']
window.Click()
window.TypeKeys("{ENTER}")
time.sleep(5)
window.TypeKeys("{TAB 1}")
window.TypeKeys("{ENTER 2}")

app = pywinauto.application.Application()

w = pywinauto.findwindows.find_windows(title_re = r'Gasper Login*')
win_num = int(len(w))
while win_num < 1:
    time.sleep(1)
    w = pywinauto.findwindows.find_windows(title_re = r'Gasper Login*')
    
    win_num = int(len(w))

#print(w)
window = app['Gasper Login - \\Remote']
time.sleep(0.5)
window.TypeKeys("{TAB 1}")
window.TypeKeys(g_password)
time.sleep(0.5)
window.TypeKeys("+{TAB 1}")
window.TypeKeys(user)
window.TypeKeys("{ENTER 2}")


w = pywinauto.findwindows.find_windows(title_re = r'Citrix Receiver*')
app = pywinauto.application.Application().connect(handle=w[0])
app.kill_()




import IEC
import time
import imp

file = open('H:/python/p.txt','r')

notes = imp.load_source('util', 'H:/python/notes.py')
user = file.readlines()[0]
password = file.readlines()[4]
txtf_user = 'ctl00$ContentPlaceHolder1$MFALoginControl1$ctl00$txtUserid'
btn_launch = 'ctl00$ContentPlaceHolder1$MFALoginControl1$ctl00$btnSubmit'
txtf_pin = 'ctl00$ContentPlaceHolder1$MFALoginControl1$ctl00$txtPasswordID'
txtf_pwd = 'ctl00$ContentPlaceHolder1$MFALoginControl1$ctl00$txtPasswordID'


ie = IEC.IEController()
ie.Navigate('https://secureauthg.diebold.com/secureauth1/secureauth.aspx?Source=/')
ie.PollWhileBusy()
ie.SetInputValue(txtf_user, user)
ie.ClickButton(caption='Submit') 
ie.PollWhileBusy()
time.sleep(10)

from pywinauto.application import Application
app = Application().connect(backend='uia',path=r"C:\Program Files (x86)\Java\jre1.8.0_111\bin\jp2launcher.exe")
dlg = app.window_(title='Security Warning')
dlg.Close()


import re
txt_launch = None
while txt_launch == None:
    time.sleep(2)
    text = ie.GetDocumentText()
    txt_launch = re.search("Launch",text)
print(txt_launch)
ie.ClickButton(caption='Launch') 
ie.PollWhileBusy()
time.sleep(1)
ie.ClickButton(caption='Submit') 


pin = notes.main()
ie.SetInputValue(txtf_pin, pin)
ie.ClickButton(caption='Submit') 
ie.PollWhileBusy()
time.sleep(1)
ie.SetInputValue(txtf_pwd, password)
ie.ClickButton(caption='Submit') 
ie.PollWhileBusy()

ie.Navigate('https://my.diebold.com/us/en/services/service-request-mgmt/Pages/service-requests.aspx')




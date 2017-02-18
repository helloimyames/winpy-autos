from pywinauto.application import Application
import time

title = u'Gasper Workstation - OUTSTANDING SCREEN - [Cash Low or Out] - \\\\Remote'
class_name = 'Transparent Windows Client'
def winWait(title,class_name):
    global app
    try:
        app = Application().Connect(title=title, class_name=class_name)
    except:
        time.sleep(1)
        print('waiting...')
        winWait(title,class_name)
    
    return app[class_name]
    
#transparentwindowsclient = winWait(title,class_name)     

#transparentwindowsclient.ClickInput()
#transparentwindowsclient.TypeKeys("{SPACE}")
#transparentwindowsclient.TypeKeys("SUS25241")
#transparentwindowsclient.TypeKeys("{ENTER}")
atmid = 'SUS28026'
t2 = u'Gasper Workstation - OUTSTANDING SCREEN - [ Object: {}:8 - \\\\Remote'.format(atmid)

trans2 = winWait(title=t2,class_name=class_name)
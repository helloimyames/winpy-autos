from pywinauto.application import Application
import time


def winWait(atmid):
    global app
    mid = atmid[4:5]
    class_name = u'Transparent Windows Client'
    g_fault_windows = ['Needs Attention', 'Out of Service', 'Prodigy BF', 'Cash Low or Out', 'Lost Communications']
    g_windows_arr = {'S':u'Gasper Workstation - OUTSTANDING SCREEN - [ Object: {}:{} - \\\\Remote'.format(atmid,mid), 
                    'main':u'Gasper Workstation - OUTSTANDING SCREEN - \\\\Remote',
                    'remote':u'Gasper Workstation             - \\\\Remote',
                    'Ticket Options':u'Ticket Options - \\\\Remote',
                    }
    
    my_dict = dict.fromkeys(g_fault_windows,
                            u'Gasper Workstation - OUTSTANDING SCREEN - [{}] - \\\\Remote'.format(atmid))                    
    my_dict.update(g_windows_dict) 
    g_title = my_dict[atmid]
   
    try:
        app = Application().Connect(title=g_title, class_name=class_name)
    except:
        time.sleep(2)
        print('waiting...')
        winWait(atmid)
    return app[class_name]
    

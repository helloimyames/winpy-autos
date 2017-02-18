import win32com.client
import time 

def main():
    if login():
        pin = parseInbox()
        print(pin)
    return pin 
        
def login():
    global db
   
    file = open('H:/python/p.txt','r')
    session = win32com.client.Dispatch("Lotus.NotesSession")
    session.Initialize("")
    
    server = file.readlines()[5]
    mail_nsf = file.readlines()[6]
    db = session.GETDATABASE(server, mail_nsf)
    return db.IsOpen

def parseInbox():
    pin = 'abcd'
    test_subject = 'MFC SecureAuth One Time Registration Code'
    s = ''
    while s != test_subject:
        doc = db.GetView("($Inbox)").GetLastDocument()
        #need to have at least 1 iten in the mailbox
        #or else GetFirstItem doesn't exist
        s = doc.GetFirstItem( "Subject" ).Text
        
        if s == test_subject:
            b = doc.GetFirstItem( "Body" ).Text
            import re
            pin = re.search(r"\d{4}",b).group(0)
            doc.remove(True)
        else:
            print('waiting 3 seconds')
            time.sleep(3)
            
    return pin
    
if __name__ == "__main__":
    main()
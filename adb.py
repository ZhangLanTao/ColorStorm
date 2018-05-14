from subprocess import*

def screencap(name):
    CREATE_NO_WINDOW = 0x08000000
    call('adb shell screencap /sdcard/'+name, creationflags=CREATE_NO_WINDOW)
    call('adb pull /sdcard/'+name, creationflags=CREATE_NO_WINDOW)
    call('adb shell rm /sdcard/'+name, creationflags=CREATE_NO_WINDOW)
    call('adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/'+name, creationflags=CREATE_NO_WINDOW)

def tap(x,y):
    CREATE_NO_WINDOW = 0x08000000
    call('adb shell input tap '+str(x)+" "+str(y), creationflags=CREATE_NO_WINDOW)





    

from mega import Mega
from datetime import datetime
import time,shutil,os,schedule

login="" #сюда почту с которой залогинился в мегу #login from mega
password="" #сюда пароль от акка меги #password from mega 
dirtobu='' #сюда название или путь до директории,которую бекапать #repository to backup
twhenbu="22:00" #time when backup
foldertobu='' #in which folder on mega.nz save backups
#--------------------Script-----------------------#
mega = Mega()
m = mega.login(login,password) #логинюсь
folder = m.find(foldertobu) #задаю папку,куда сохранять
space = m.get_storage_space(mega=True) #получаю количество места

def archivefile():
    x=str(datetime.now())[:10]
    y=str(datetime.now())[11:16]
    filename="Backup"+x+"-"+y 
    shutil.make_archive(filename,'zip',root_dir=dirtobu)
    return uploadfile(filename)

def uploadfile(x):
    file = m.upload(x+'.zip',folder[0])
    os.remove(x+'.zip')
    z= "space left:"+str(space)
    return z
schedule.every().day.at(twhenbu).do(app1.archivefile)

while True:
    schedule.run_pending()
    time.sleep(1)
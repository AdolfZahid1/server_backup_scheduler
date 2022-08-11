# Server backup scheduler
## dependencies
```
pip install Mega.py
```
By default script makes backup every day at 22:00 your system local time
Inside py code change this strings:
```
login="" #сюда почту с которой залогинился в мегу #login from mega
password="" #сюда пароль от акка меги #password from mega 
dirtobu='' #сюда название или путь до директории,которую бекапать #repository to backup
twhenbu="22:00" #time when backup
foldertobu='' #in which folder on mega.nz save backups
```
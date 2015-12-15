import os, time
cmd = "wmic useraccount where name='%username%' get sid"
os.system(cmd)

time.sleep(30)


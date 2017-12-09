import os

print("""
本升级脚本仅适用于使用JSON格式配置文件的用户，会执行git pull拉取代码并将bot_constant-json.py重命名。
如果您使用py格式的配置文件，执行本脚本会使您丢失全部配置。
""")
i=input("键入[y]继续，[n]退出>")

if i.upper()=='Y':
    os.chdir('..')
    os.system('git reset --hard && git pull')
    os.remove('bot_constant.py')
    os.rename('bot_constant-json.py','bot_constant.py')
else:
    print("什么都没有发生...")
    exit()
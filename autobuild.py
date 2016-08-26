import commands
import os


print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JPush/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JMessage/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/JSMS/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/opt/push/jpush-docs/jpush-docs/zh/Index/"))
print (commands.getstatusoutput("mkdocs build --clean"))





import os
#config the dir of the mkdocs docs dir
conf={}

conf["mkdocs"]="/opt/push/jpush-docs/syndocs/jpush-docs/zh/"

conf["zip"]="/opt/push/jpush-docs/syndocs/download-zip/"

#jpush dir
conf["jpush_dir"]=os.path.join(conf["mkdocs"],"JPush")
conf["jpush_docs"]=os.path.join(conf["jpush_dir"],"docs")
#conf["jmessage"]=os.path.join(conf["jiguang_docs"],"jmessage")

conf["jpush"]={}

#jpush -> server dir
conf["jpush_server"]=os.path.join(conf["jpush_docs"],"server")
conf["jpush_server"]=os.path.join(conf["jpush_server"],"3rd")
conf["jpush"]["server"]={}
conf["jpush"]["server"]["jpush-api-csharp-client"]=os.path.join(conf["jpush_server"],"csharp_sdk.md")
conf["jpush"]["server"]["jpush-api-python-client"]=os.path.join(conf["jpush_server"],"python_sdk.md")
conf["jpush"]["server"]["jpush-api-php-client"]=os.path.join(conf["jpush_server"],"php_sdk.md")
conf["jpush"]["server"]["jpush-api-nodejs-client"]=os.path.join(conf["jpush_server"],"nodejs_sdk.md")
conf["jpush"]["server"]["jpush-api-java-client"]=os.path.join(conf["jpush_server"],"java_sdk.md")
conf["jpush"]["server"]["jpush-api-ruby-client"]=os.path.join(conf["jpush_server"],"ruby_sdk.md")


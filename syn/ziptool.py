import requests
import os
import zipfile
import dirconfig
import shutil
import logging


class ZipTool():
    exist_flag = None

    def __init__(self):
        self.exist_flag=0

    def is_zip_exist(self,zip_dir):
        if os.path.exists(zip_dir):
            logging.info(zip_dir +" "+"exist.")
            logging.info("exist_flag is " + " " + str(self.exist_flag))
            return True
        else:
            logging.info(zip_dir + " " + "not exist.")
            self.exist_flag = self.exist_flag + 1
            logging.info("exist_flag is " + " " + str(self.exist_flag))
            return False

    def zip_download(self,zip_dir,release_version,url):
        with open(zip_dir, "wb") as code:
            download_url = url + "/archive/" + release_version + ".zip"
            try:
                download_response = requests.get(download_url)
                logging.info("download " + download_url)
            except:
                logging.info("download "+ download_url +" failed")
            try:
                code.write(download_response.content)
                logging.info("save " + download_url)
            except:
                logging.info("save " + download_url +" failed")

    def unzip_file(self,name,release_version):
        filename = os.path.join(dirconfig.conf["zip"], name)
        filename = os.path.join(filename, release_version+".zip")
        filedir = os.path.join(dirconfig.conf["zip"], name)
        filedir = os.path.join(filedir, 'data/')

        fz = zipfile.ZipFile(filename)
        if fz:
            fz = zipfile.ZipFile(filename, 'r')
            for file in fz.namelist():
                fz.extract(file, filedir)
            logging.info(filename + " " +'unzip')
        else:
            logging.info(filename +" " +'unzip failed')


    def replace_readme(self,name,release_version):
        file_dir = os.path.join(dirconfig.conf["zip"], name)
        file_dir = os.path.join(file_dir, 'data')
        release_dir=name+"-"+release_version[1:]
        file_dir=os.path.join(file_dir, release_dir)
        file_dir=os.path.join(file_dir, "README.md")
        logging.info(file_dir+" " +"this is the new file")
        readme_dir=dirconfig.conf["jpush"]["server"][name]
        logging.info(readme_dir+" " +"this is the old file")
        try:
            shutil.copyfile(file_dir,readme_dir)
            logging.info(name +" " + release_version + " " +"the file is replaced")
        except:
            logging.info(name +" " + release_version + " " +"the file is not replaced")
































import logging
import os
import sys
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

logs_dir = os.path.join(os.getcwd(),"logs") # logs is the folder and joinning with LOG_FIle. 
                                   #os.getcwd() will locate the directory where the error has come.
os.makedirs(logs_dir, exist_ok= True) # This command will ensure that once the folder is created, it 
# will not be deleted. If the folder is already created, it will not create again.
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)


logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = '[%(asctime)s] %(lineno)d  %(name)s - %(levelname)s - %(message)s'
    )


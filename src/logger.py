import logging
import os
from datetime import datetime

Logfile=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Log_Path=os.path.join(os.getcwd(),"logs",Logfile)
os.makedirs(Log_Path,exist_ok=True)

LogFilePath=os.path.join(Log_Path,Logfile)

logging.basicConfig(
    filename=LogFilePath,
    format="[%(asctime)s]%(lineno)d %(name)s-%(levelname)s-%(message)s",
    level=logging.INFO
)
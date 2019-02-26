#coding=utf-8
import  logging

class LogIni():
    def log(self,log_content):
        # 定义文件
        logFile = logging.FileHandler('../Logs/logInfo.log', 'a')
        # log格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)
        # 定义日志
        logger1 = logging.Logger('logTest', level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)


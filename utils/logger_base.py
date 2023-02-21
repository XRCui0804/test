import logging as lg

# 取出logger对象
# 此函数也可进行设置记录人员信息，记录最低层级等 # logger = lg.getLogger('root',level=lg.INFO)
logger = lg.getLogger()

# 创建一个handler对象，用于写入日志文件
fh = lg.FileHandler('main.log')

# 再创建一个handler，用于输出到控制台
ch = lg.StreamHandler()

# 标准输出格式对象
formatter = lg.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s')

# 文件输出调取日志标准输出格式
fh.setFormatter(formatter)
# 控制台输出调取日志标准输出格式
ch.setFormatter(formatter)

# logger 增加日志文件输出方式
logger.addHandler(fh)
# logger 增肌日志控制台输出方式
logger.addHandler(ch)

# 设置最低记录级别
logger.setLevel(lg.DEBUG)

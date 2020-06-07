import logging 
import logging.config 
import logging.handlers
logger = logging.getLogger()
handler = logging.handlers.SysLogHandler(address='/var/run/syslog')
logger.addHandler(handler)
logger.info('Test')

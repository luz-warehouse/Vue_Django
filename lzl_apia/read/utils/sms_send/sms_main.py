from qcloudsms_py import SmsSingleSender
from . import settings
import random
from read.utils.loggins import get_logger
logger=get_logger()
# 生成code函数，四位数字
def get_code():
    s=''
    for i in range(4):
        num=random.randrange(0,9)
        s+=str(num)
    return s

from celery_task import app

@app.task
def send_sms(mobile, code):
    ssender = SmsSingleSender(settings.APPID, settings.APPKEY)
    params = [code,settings.TIME ]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, mobile,
                                         settings.TEMPLATE_ID, params, sign=settings.SMS_SIGN, extend="", ext="")
        if result.get('result')==0:
            return True
        else:
            # 发送失败，记录日志
            logger.error('手机号为：%s，发送短信失败'%mobile)
            return False
    except Exception as e:
        logger.error('发送短信出异常，异常手机号为：%s' % mobile)
        return False
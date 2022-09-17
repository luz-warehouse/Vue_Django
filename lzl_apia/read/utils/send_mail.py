from celery_task import app


# 异步发送邮箱  #######
#####################
@app.task
def send_emaila(email,msg,time):

    title  = '密码重置'
    message = '你的验证码为：%s,请尽快修改,%s分钟内有效' % (msg,time)# 发送普通的消息使用的时候message

    from django.core.mail import send_mail
    from django.conf import settings
    # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
    send_mail(title,
              message,
              settings.EMAIL_HOST_USER,
              [email, ],
              fail_silently=False)
    return '发送邮箱了吧'
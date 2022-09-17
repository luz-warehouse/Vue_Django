
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE","read.settings.dev")
# django.setup()
#
# from django.core.mail import send_mail
# # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
# send_mail('邮件的标题', '这是邮件的内容', 'liu245424389xu@163.com',
#     ['1471678863@qq.com',], fail_silently=False)

from read.utils.send_mail import send_emaila

# send_emaila.delay()
#
send_emaila('1307434047@qq.com')
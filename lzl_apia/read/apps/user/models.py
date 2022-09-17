from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


# 用户表
class User(AbstractUser):

    gender = ((0,'男'),(1,'女'))

    sex = models.IntegerField(verbose_name='性别',choices=gender,default=0)
    nickname = models.CharField(verbose_name='昵称',max_length=16,default='大帅比')

    mobile =  models.CharField(verbose_name='联系号码',unique=True,blank=True,max_length=32)

    icon = models.ImageField(verbose_name='头像',upload_to='icon', default='icon/man.png')

    coin = models.IntegerField(verbose_name='屋币',default=500)
    # userdetail = models.OneToOneField(to='UserDetail',db_constraint=False,on_delete=models.CASCADE)

    choose_list = [
        (1,'普通'),
        (2,'高级'),
    ]

    level = models.IntegerField(verbose_name='等级',choices=choose_list,default=1)

    level_experience = models.IntegerField(verbose_name='经验',default=0)

    is_superuser  = models.BooleanField(verbose_name='是否是管理员',default=0)

    class Meta:

        db_table = 'read_user'  # 表明
        verbose_name = '用户表'  # 后台admin中显示的名字
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.username
    @property
    def gender(self):
        return self.get_sex_display()

class Order(models.Model):
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    subject = models.CharField(max_length=150, verbose_name="订单标题")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价", default=0)
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True) #必须唯一
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")
    user = models.ForeignKey(to='User', related_name='order_user', on_delete=models.DO_NOTHING, db_constraint=False, verbose_name="下单用户")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")





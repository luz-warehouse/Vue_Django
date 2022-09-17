
from rest_framework import serializers
from .models import User,Order
from read.libs.alipay import alipay,GATEWAY


# 获取所有
class UserallModelserializer(serializers.ModelSerializer):


    class Meta:

        model = User

        fields = '__all__'

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.cache import cache
from .models import User
# from django.conf import settings
from read.utils.sms_send import settings

# 用户登录
class UserModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):

        # 获取用户
        user = self._get_user(attrs)
        self.user = user
        # 签发token
        token = self._get_token(user)
        self.context['token'] = token
        self.context['username'] = user.username
        self.context['icon'] = str(user.icon)
        self.context['user_id'] = user.id
        self.context['nickname']=user.nickname
        return attrs

    def _get_user(self, attrs):
        # print(attrs)
        import re
        username = attrs.get('username')
        # print(username)
        if re.match(r'^1[3-9][0-9]{9}$', username):
            user = User.objects.filter(mobile=username).first()
        # elif re.match(r'^[a-z0-9A-Z]+[- | a-z0-9A-Z . _]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$', username):
        elif re.match(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', username):
            user = User.objects.filter(email=username).first()
            # print('youxiang')
        else:
            user = User.objects.filter(username=username).first()

        if not user:
            raise ValidationError({'detail': '用户不存在'})

        password = attrs.get('password')

        if not user.check_password(password):  # 用了auth的User表
            raise ValidationError({'detail': '密码错误'})

        # user.email_user()

        return user

    # def create(self, validated_data):
    #     print('我根本没有保存')
    #     return self.user

    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


class UserMobileModelSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField()
    # code不是User表的字段，所以要重写
    code = serializers.CharField()

    class Meta:
        model = User
        fields = ['mobile', 'code']

    def validate(self, attrs):

        # 校验code是否正确
        self._check_code(attrs)

        # 获取用户
        user = self._get_user(attrs)
        # 签发token
        token = self._get_token(user)

        self.context['token'] = token
        self.context['username'] = user.username
        self.context['user_id'] = user.id
        self.context['icon'] = str(user.icon)
        self.context['nickname'] = user.nickname
        return attrs

    def _check_code(self, attrs):
        code = attrs.get('code')
        mobile = attrs.get('mobile')

        # 有可能有的公司，测试阶段，有万能验证码
        # 获取放在缓存中的code
        old_code = cache.get(settings.SMS_CACHE % mobile)
        # 删除缓存中的code
        if not (old_code and code == old_code):
            raise ValidationError({'detail': '验证码校验失败'})

    def _get_user(self, attrs):
        mobile = attrs.get('mobile')
        user = User.objects.filter(mobile=mobile).first()
        if not user:
            raise ValidationError({'detail': '用户不存在'})
        return user

    def _get_token(self, user):
        from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


class RegisterModelSerializer(serializers.ModelSerializer):
    # code = serializers.CharField(max_length=4, min_length=4,write_only=True)
    code = serializers.CharField(max_length=4, min_length=4)
    username = serializers.CharField(allow_blank=True,allow_null=True)

    class Meta:
        model = User
        fields = ['mobile', 'code', 'password','email','username']
        extra_kwargs = {
            'password': {'max_length': 16, 'min_length': 3},
        }

    # def validate_mobile(self, mobile):
    #     # 手机号是否在库中了
    #     import re
    #     return mobile

    # def save(self, *args, **kwargs):
    #     self.name = f'模拟练习{datetime.now().strftime("%Y%m%d")}{random.randint(1000, 9999)}'
    #     super().save(*args, **kwargs)

    def validate(self, attrs):
        # 验证码是否正确
        self._check_code(attrs)
        # 直接返回attrs
        # code 剔除
        attrs.pop('code')
        return attrs

    def _check_code(self, attrs):
        code = attrs.get('code')
        mobile = attrs.get('mobile')

        # 有可能有的公司，测试阶段，有万能验证码
        # 获取放在缓存中的code
        old_code = cache.get(settings.SMS_CACHE % mobile)
        # 删除缓存中的code
        if not (old_code and code == old_code):
            raise ValidationError({'detail': '验证码校验失败'})

    def create(self, validated_data):


        # username创建出来，使用手机号作为用户名
        if not validated_data['username']:

            validated_data['username'] = validated_data.get('mobile')
        # 使用User表的create_user方法新增用户（密码是密文的）
        user = User.objects.create_user(**validated_data)
        return user


# 邮箱更改密码
class EmailModel(serializers.ModelSerializer):

    code = serializers.CharField()
    newpwd = serializers.CharField()
    repwd = serializers.CharField()
    email = serializers.CharField()

    class Meta:

        model = User
        fields = ['code','newpwd','repwd','email']

    def validate(self, attrs):
        # print(attrs)
        code = attrs.get('code')
        newpwd = attrs.get('newpwd')
        repwd = attrs.get('repwd')
        email = attrs.get('email')

        if newpwd != repwd or newpwd is None or repwd is  None or code is None:

            raise ValidationError({'detail': '校验失败！'})

        cache_code = cache.get(settings.SMS_CACHE%email)

        if cache_code != code:
            raise ValidationError({'detail': '请重新发送验证信息！'})

        user = User.objects.all().filter(email=email).first()

        user.set_password(newpwd)
        user.save()

        return attrs

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname','icon','gender','sex','coin']
        extra_kwargs = {
            'sex':{'write_only':True},
            'coin':{'read_only':True},
        }

class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField()
    re_password = serializers.CharField()

    class Meta:
        model = User
        fields = ['password','new_password','re_password']

    def validate(self, attrs):

        user = self._get_user()
        self._check_pwd(user,attrs)
        return attrs

    def _get_user(self):
        return self.context.get('request').user


    def _check_pwd(self,user,attrs):
        # print(user,type(user))
        usera = User.objects.filter(username=user).first()
        # print(usera)
        # print(usera,type(usera))
        password = attrs.get('password')
        new_password = attrs.get('new_password')
        re_password = attrs.get('re_password')
        # print(password)
        # print(new_password)
        # print(re_password)
        if password:
            if usera.check_password(password):
                if new_password and re_password:
                    if new_password == re_password:
                        return usera
                    raise ValidationError({'detail': '两次密码输入不一致！'})
                raise ValidationError({'detail': '新密码不能为空！'})
            raise ValidationError({'detail': '原密码输入有误！'})
        raise ValidationError({'detail': '原密码不能为空！'})

    def update(self, instance, validated_data):
        # print(instance,type(instance))
        new_password = validated_data.get('new_password')
        instance.set_password(new_password)
        instance.save()

        return instance

# 更改头像
class Updateicon(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['icon']

    def validate(self, attrs):

        # print(attrs)
        return  attrs


class UserUpdateCnin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['coin']

    def validate(self, attrs):

        trade_no = self._get_out_trade_no()  # 支付链接
        subject = self.context.get('request').user.username  # 主题
        coin = attrs.get('coin')  # 价格
        total_amount = coin/100
        pay_url = self.api_alipay_trade_page_pay(total_amount,subject,trade_no)
        self.context['pay_url'] = pay_url
        # 支付前数据处理
        self._perform_save(attrs,trade_no, subject)
        return attrs

    # 生成支付链接
    def _get_out_trade_no(self):
        import uuid
        return str(uuid.uuid4()).replace('-', '')


    def api_alipay_trade_page_pay(self,total_amount,subject,trade_no):
        from django.conf import settings
        res = alipay.api_alipay_trade_page_pay(
            total_amount=total_amount,  # 价格
            subject=subject,  # 主题
            out_trade_no=trade_no,  # 支付链接
            return_url=settings.RETURN_URL,  # 前端回调
            notify_url=settings.NOTIFY_URL  # 后端回调

        )

        return GATEWAY+res

    def _perform_save(self,attrs, trade_no, subject):
        attrs['out_trade_no'] = trade_no  # 支付连接
        attrs['subject'] = subject  # 主题


    def update(self, instance, validated_data):
        old_coin = instance.coin
        new_coin = validated_data.get('coin')
        coin = old_coin+new_coin
        # print(instance.pk)
        total_amount = new_coin / 100
        subject = validated_data.get('subject')
        trade_no = validated_data.get('out_trade_no')
        User.objects.filter(pk=instance.pk).update(coin=coin)
        # print(total_amount)
        Order.objects.create(subject = subject,total_amount = total_amount,out_trade_no=trade_no,user=instance,order_status=1)

        return instance




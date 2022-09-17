# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from user.UserSerializers import UserModelSerializer, UserMobileModelSerializer, UserallModelserializer, \
    RegisterModelSerializer, EmailModel, PersonalSerializer, ChangePasswordSerializer, Updateicon, UserUpdateCnin
from rest_framework.exceptions import APIException
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from user.models import User
from read.utils.response import APIResponse
from django.core.cache import cache
from read.utils.sms_send import get_code, settings, send_sms
from read.utils.send_mail import send_emaila

# 生成token使用的
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


# from django.conf import settings

#############################################
# 用户的增删改查，后期加入权限，只能超级用户增删改查 #
#############################################
class SuperUser(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserallModelserializer


class UserView(ViewSet):

    # 多方式登录
    @action(methods=['POST'], detail=False)
    def login(self, request):
        ser = UserModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        # ser.save()
        token = ser.context.get('token')
        username = ser.context.get('username')
        icon = ser.context.get('icon')
        user_id = ser.context.get('user_id')
        nickname = ser.context.get('nickname')
        return APIResponse(token=token, username=username, icon=icon, user_id=user_id, nickname=nickname)

    # 校验手机是否存在
    @action(methods=['GET'], detail=False)
    def check_mobile(self, request):
        mobile = request.query_params.get('mobile', None)
        if mobile:
            user = User.objects.filter(mobile=mobile).first()

            if user:
                return APIResponse(exisit=True)
            else:
                return APIResponse(exisit=False)

        else:
            # return APIResponse(code=101,msg='手机号没有传')
            raise APIException({'detail': '手机号没有传'})

    # 发送短信
    @action(methods=['GET'], detail=False)
    def send_sms(self, request):
        mobile = request.query_params.get('mobile', None)
        if mobile:
            # 手机号存在，发送短信
            code = get_code()
            print(code)
            # 发送短信（同步发送：等着腾讯发送成功或失败的返回，可能等很长时间）
            # 异步发送短信（不用等腾讯是否成功，直接给用户返回）
            # 现在拿到的一个ID
            res = send_sms.delay(mobile, code)
            # res = True

            # print(res)
            if res:
                # 发送成功后，短信验证码，放到缓存中(默认放内存中，实际项目要放到redis中)

                cache.set(settings.SMS_CACHE % mobile, code, 60 * settings.TIME)

                # # 取出验证码
                # code=cache.get(settings.SMS_CACHE%mobile)
                # return HttpResponse('ok')
                # return APIResponse(aa='短信发送成功')
                return APIResponse(msg='短信发送成功')
            else:
                raise APIException({'detail': '短信发送失败'})
        else:
            # return APIResponse(code=101,msg='手机号没有传')
            raise APIException({'detail': '手机号没有传'})

    # 手机登录
    @action(methods=['POST'], detail=False)
    def mobile_login(self, request):
        ser = UserMobileModelSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        token = ser.context.get('token')
        username = ser.context.get('username')
        icon = ser.context.get('icon')
        user_id = ser.context.get('user_id')
        nickname = ser.context.get('nickname')
        return APIResponse(token=token, username=username, icon=icon, user_id=user_id, nickname=nickname)

    # 发送邮箱找回密码
    @action(methods=['POST'], detail=False)
    def email_pwd(self, request):
        # print(request.data)
        email = request.data.get('email')
        # print('邮箱这个:',email)
        # print(len(email))
        if not email:
            raise APIException({'detail': '请输入邮箱'})

        user = User.objects.all().filter(email=email)

        if not user:
            raise APIException({'detail': '请检查邮箱是否输入有误'})

        import uuid

        # 作为验证信息
        token_msg = str(uuid.uuid4())
        print('随机码', token_msg)
        cache.set(settings.SMS_CACHE % email, token_msg, settings.TIME * 60)
        print('缓存中随机码', cache.get(settings.SMS_CACHE % email))

        #############
        # 发送邮箱验证码#
        #############
        send_emaila.delay(email, token_msg, settings.TIME)
        # send_emaila(email,token_msg,settings.TIME)

        return APIResponse(token=token_msg, msg='邮箱发送成功，请及时修改')

    # 校验邮箱的验证码

    # 邮箱修改密码保存
    @action(methods=['POST'], detail=False)
    def eamil_edit_pwd(self, request):
        # print(request.data)

        ser = EmailModel(data=request.data)

        ser.is_valid(raise_exception=True)

        return APIResponse(msg='密码修改成功，请登录')

    # 校验用户名是否已经存在
    @action(methods=['post', ], detail=False)
    def check_username(self, request):
        username = request.data.get('username')

        user = User.objects.all().filter(username=username) or User.objects.all().filter(mobile=username)

        if user:
            raise APIException({'detail': '当前用户名已存在，请修改用户名'})

        return APIResponse()

    # 校验邮箱是否已经存在
    @action(methods=['post', ], detail=False)
    def check_email(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise APIException({'detail': '当前邮箱已存在，请修改邮箱'})

        return APIResponse()

    # 校验验证码是否通过
    @action(methods=['post', ], detail=False)
    def check_code(self, request):
        email = request.data.get('email')
        code = request.data.get('code')

        if not code:
            raise APIException({'detail': '请输入验证码'})

        if not email:
            raise APIException({'detail': '校验有误，请返回上一步重新发送验证码'})

        cache_code = cache.get(settings.SMS_CACHE % email)

        if cache_code != code:
            raise APIException({'detail': '验证码有误，请再次确认验证码'})

        return APIResponse(msg='验证通过！')


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin


class UserRegisterView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

    # setattr(getattr(RegisterModelSerializer,'Meta'),'model','biao')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return APIResponse(msg='注册成功')


from read.utils.authentication import JWTMyUserAuthentication


# 更新个人中心
class PersonalCenter(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    authentication_classes = [JWTMyUserAuthentication]

    queryset = User.objects.all()
    serializer_class = PersonalSerializer


# 修改密码
class ChangePasswordView(UpdateModelMixin, GenericViewSet):
    authentication_classes = [JWTMyUserAuthentication]

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return APIResponse(msg='密码修改成功!')


# 更新头像

class SetIcon(UpdateModelMixin, GenericViewSet):

    def update(self, request, *args, **kwargs):
        res = request.FILES.get('file')

        pk = request.data.get('pk')

        user_obj = User.objects.filter(pk=pk).first()
        user_obj.icon = res
        user_obj.save()
        # print(user_obj.icon)
        return APIResponse(icon=str(user_obj.icon))


class SetCoin(UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserUpdateCnin
    # 认证类（可以自己写）
    authentication_classes = [JWTMyUserAuthentication]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        pay_url = serializer.context.get('pay_url')
        return APIResponse(pay_url=pay_url)


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from read.utils.loggins import get_logger


class SuccessView(APIView):
    def get(self, request):
        # vue的前端来调用的
        out_trade_no = request.query_params.get('out_trade_no')
        order = Order.objects.filter(out_trade_no=out_trade_no).first()
        if order.order_status == 1:
            # 订单支付成功，
            return APIResponse(msg='支付成功')
        else:
            return APIResponse(msg='我们还没有收到该订单的付款，请稍后刷新页面再试')

    def post(self, request):
        # 支付宝来调用，用来修改订单状态
        import json
        try:
            result_data = request.data.dict()  # 把querydic转成字典对象，否则，不允许改值
            logger = get_logger()
            logger.warning(json.dumps(result_data))
            out_trade_no = result_data.get('out_trade_no')
            signature = result_data.pop('sign')
            ###一定要验证签名，如果不验证签名，不能修改订单状态
            from libs.alipay import alipay
            result = alipay.verify(result_data, signature)
            if result and result_data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
                # 完成订单修改：订单状态、流水号、支付时间
                Order.objects.filter(out_trade_no=out_trade_no).update(order_status=1)
                # 完成日志记录
                logger.warning('%s订单支付成功' % out_trade_no)
                return Response('success')  # 支付宝要求的格式
            else:
                logger.error('%s订单支付失败' % out_trade_no)
        except:
            pass
        return Response('failed')

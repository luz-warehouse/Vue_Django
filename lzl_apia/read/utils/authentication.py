from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.settings import api_settings
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
from rest_framework.exceptions import AuthenticationFailed
import jwt
from user.models import User
class JWTMyUserAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # print(request.META)
        # token=request.query_params.get('HTTP_AUTHORIZATION',None)
        token = request.META.get('HTTP_AUTHORIZATION', None)
        # print(token)
        if token:
            # 校验token是不是过期了，是不是合法，
            try:
                payload = jwt_decode_handler(token)
                # print(payload)
            except jwt.ExpiredSignature:

                raise AuthenticationFailed('token过期')
            except jwt.DecodeError:

                raise AuthenticationFailed('token认证失败')
            except jwt.InvalidTokenError:
                raise AuthenticationFailed('token不合法')
        else:
            raise AuthenticationFailed('token没有携带')

        '''
        # 三种方案得到user
            -继承BaseJSONWebTokenAuthentication，self.authenticate_credentials
            -直接把BaseJSONWebTokenAuthentication，authenticate_credentials方法拿出来，放到自己类中
            -完全自己写

        '''
        user = User.objects.get(pk=payload.get('user_id'))
        # user=User(id=payload.get('user_id'),username=payload.get('username'))
        # 优化，减少数据库压力（）
        # user={'id':payload.get('user_id'),'username':payload.get('username')}
        return (user, token)
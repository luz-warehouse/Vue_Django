from rest_framework.views import exception_handler
from rest_framework.response import Response

from .loggins import get_logger

logger = get_logger()


def common_exception_handler(exc, context):
    # print(str(context.get('view')))
    # print(context.get('request').Meta.get('REMOTE_ADDR'))
    # 只要出异常，就要记录日志
    logger.error('ip为%s的用户，访问%s视图类出错,错误信息是%s' % (
    context.get('request').META.get('REMOTE_ADDR'), str(context.get('view')), str(exc)))
    response = exception_handler(exc, context)
    if response:  # drf的异常:未认证通过，没有权限。。。
        return Response({'code': 999, 'msg': response.data.get('detail', '服务器异常，请联系系统管理员')})
    else:  # django的异常
        return Response({'code': 999, 'msg': '服务器异常，请联系系统管理员'})
        # return Response({'code': 999, 'msg': str(exc)})

def get_result(request):
    from .celery import app  # 自己写的app
    from celery.result import AsyncResult  # celery模块下的
    id_uuid=request.GET.get('id') or request

    a = AsyncResult(id=id_uuid, app=app)
    print(a.__dict__)
    if a.successful():
        result = a.get()
        print(result)
        return result
    elif a.failed():
        result = '任务失败'
        print('任务失败')
        return result
    elif a.status == 'PENDING':
        result = '任务等待中被执行'
        print('任务等待中被执行')
        return result
    elif a.status == 'RETRY':
        result = '任务异常后正在重试'
        print('任务异常后正在重试')
        return result
    elif a.status == 'STARTED':
        result = '任务已经开始被执行'
        print('任务已经开始被执行')
        return result
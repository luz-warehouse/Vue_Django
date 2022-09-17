from celery_task.celery import app

@app.task
def update_banner():
    from home.models import Banner
    from home.serializer import SerializerBanner
    from django.core.cache import cache
    queryset = Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = SerializerBanner(instance=queryset,many=True)
    for item in serializer_class.data:
        item['image'] = 'http://127.0.0.1:8000' + item['image']
    cache.set('banner_list',serializer_class.data)
    return True
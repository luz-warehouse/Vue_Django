from alipay import AliPay
from . import settings
alipay = AliPay(
    appid=settings.APP_ID,
    app_notify_url=None,
    app_private_key_string=settings.APP_PRIVATE_KEY_STRING,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
    sign_type=settings.SIGN,  # RSA 或者 RSA2
    debug=settings.DEBUG , # 默认 False
)

# 有参装饰器
def auth(mode):
    def deco(func):
        def wrapper(*args,**kwargs):
            name = input('username: ').strip()
            pwd = input('password: ').strip()
            if mode == 'file':
                if name == 'pig' and pwd == '123':
                    res = func(*args,**kwargs)
                    return res
                else:
                    print('账号密码错')
            elif mode == 'mysql':
                print('基于mysql认证')
            elif mode == 'ldap':
                print('基于ldap认证')
            else:
                print('无效认证')
        return wrapper
    return deco

# @auth('file')
# def index():
#     print('form index')
# index()

@auth('ldap')
def home(name):
    print('傻子')
home('egon')
# import threading
# import time
#
# class Singletion:
#     instance = None
#     lock = threading.RLock()
#     def __int__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         # 返回空对象
#         if cls.instance:
#             return cls.instance
#         with cls.lock:
#             if cls.instance:
#                 return cls.instance
#             time.sleep(0.1)
#             cls.instance = object.__new__(cls) # 创建空对象
#         return cls.instance
#
# obj1 = Singletion('luz')
# obj2 = Singletion('luz')
# print(obj1)
# print(obj2)

import multiprocessing
count = multiprocessing.cpu_count()
print(count)
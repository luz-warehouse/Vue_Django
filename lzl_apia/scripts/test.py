# from multiprocessing import Process
# from threading import Thread
# import time
#
#
# def task1():
#     res = 0
#     for i in range(9999999):
#         res += i
#
#
# def task2():
#     time.sleep(2)
#
#
# def get_time(work, category, num):
#     task_list = []
#     start = time.time()
#     for i in range(num):
#         p = category(target=work)
#         p.start()
#         task_list.append(p)
#     for i in task_list:
#         i.join()
#     stop = time.time()
#     print(f'{category.__name__}共用时 %s' % (stop - start))
#
#
# if __name__ == '__main__':
#     print('计算密集型多进程和多线程的耗时：')
#     get_time(task1, Process, 10)
#     get_time(task1, Thread, 10)
#     print('IO密集型多进程和多线程的耗时：')
#     get_time(task2, Process, 300)
#     get_time(task2, Thread, 300)

# def func1(val):
#     val = '2'
#     print(val)
# a = '1'
# func1(a)
# print(a)
#
# def func2(val_list):
#     val_list.append(1)
#     print(val_list)
# val_list = []
# func2(val_list)
# print(val_list)
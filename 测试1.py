# from threading import Thread
# def plus():
#     global  num
#     for i in range(100000000):
#         num+=2
# def sub():
#     global num
#     for i in range(100000000):
#         num-=1
# num = 0
# if __name__ == "__main__":
#     t1 = Thread(target = plus)
#     t2 = Thread(target = sub)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(num)

class A:
    def __call__(self):
        print(1)
    def __iter__(self):
        print(2)
    def __getitem__(self):
        print(3)
    def __contains__(self):
        print(4)
a = A()
a()
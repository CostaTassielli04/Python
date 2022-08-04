class QueueError(IndexError):
    def __init__(self):
        IndexError.__init__(self)
        raise IndexError

class Queue:
    def __init__(self):
        self.__coda_list=[]

    def put(self, elem):
        self.__coda_list.append(elem)

    def get(self):
        val=self.__coda_list[0]
        del self.__coda_list[0]
        return val

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except IndexError:
    print("Queue error")

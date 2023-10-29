class Node():
    def __init__(self, elem, link):
        self.data = elem
        self.link = link

https://gurumee92.tistory.com/113
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None and self.rear == None

    def enqueue(self, elem):
        node = Node(elem, None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.isEmpty():
            return "큐가 비어있습니다. 언더플로우가 발생합니다."
        else:
            data = self.front.data
            self.front = self.front.link
            if self.front == None:
                self.rear = None
            return data

    def peek(self):
        if self.isEmpty():
            return "큐가 비어있습니다. peek 요소를 반환할 수 없습니다."
        else:
            return self.front.data

    def size(self):
        link = self.front
        length = 0
        while link != None:
            link = link.link
            length += 1

        return length

    def display(self, ment):
        print(ment, end="")
        link = self.front
        while link != None:
            print(link.data, end=" ")
            link = link.link


def main():
    print("연결된 구조의 큐 구현\n")
    queue = LinkedQueue()
    for i in range(10):
        queue.enqueue(i)
    queue.display("큐 enqueue 9회: ")
    print("\n")

    print("dequeue() --> ", queue.dequeue())
    print("dequeue() --> ", queue.dequeue())
    print("dequeue() --> ", queue.dequeue())
    queue.display('큐 dequeue 3회: ')
    print("\n")

    queue.enqueue("수퍼맨")
    queue.enqueue("배트맨")
    queue.enqueue("원더우먼")
    queue.enqueue("아쿠아맨")
    queue.display("큐 enqueue 4회: ")
    print("\n")

    print("dequeue() --> ", queue.dequeue())
    queue.display("큐 dequeue 1회: ")
    print("\n")

    print("size: ", queue.size())
    print("\n")

    print("peek() -->", queue.peek())


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def append(self, value):
        """
        Append Value
        :param value:
        :return:
        """
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1

    def search(self, value) -> tuple:
        """
        :param value: int|str
        :return: (value, index)
        """
        index = 0
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return value, index
            temp = temp.next
            index += 1

    def pop(self, index: int = None):
        if self.head is None:
            raise IndexError("pop from empty link list")

        index = index - 1 if index is not None else self.length - 1

        if index < 0 or index > self.length-1:
            raise IndexError("pop index out of range")

        if index == 0:
            temp = self.head
            self.head = temp.next
            self.length -=1
            if self.length == 0:
                self.tail = None
            return temp.value

        last = self.head
        second_last = None
        for _ in range(index):
            second_last = last
            last = last.next

        second_last.next = last.next
        if index == self.length-1:
            self.tail = second_last
        return last.value

    def reverse(self):
        if self.length == 0:
            raise IndexError("Empty link list")

        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.tail, self.head = self.head, self.tail

    def __str__(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(str(temp.value))
            temp = temp.next
        return " -> ".join(result)

    def __eq__(self, other):
        if isinstance(other, LinkList):

            if other.length != self.length:
                return "No"

            temp = self.head
            other_temp = other.head
            result = "Yes"
            while temp is not None:
                if temp.value != other_temp.value:
                    result = "No"
                    break
                temp = temp.next
                other_temp = other_temp.next
            return result

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return

        previous = self.head
        temp = self.head.next
        while temp is not None:
            if temp.value == value:
                if temp.next == None:
                    self.tail = previous
                previous.next = temp.next
                return
            previous = temp
            temp = temp.next
        raise ValueError("LinkList.remove(x): x not in LinkList")


if __name__ == "__main__":
    l_list = LinkList()

    l_list.append(5)
    l_list.append(6)
    l_list.append(7)
    l_list.append(8)

    # l_list.remove(8)
    # l_list.remove(8)

    l_list.reverse()
    print(l_list)
    print("->",getattr(l_list.head, 'next'))

    # print(f"{l_list.search(7)=}")
    # other_l_list = LinkList()
    # other_l_list.append(5)
    # other_l_list.append(6)
    # other_l_list.append(7)
    # other_l_list.append(8)
    # print(other_l_list)
    # print(l_list == other_l_list)
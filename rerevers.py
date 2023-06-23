class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        another = self.head
        while another is not None:
            next = another.next
            another.next = prev
            prev = another
            another = next
        self.head = prev

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" ")
            node = node.next


# создаем экземпляр связного списка
my_list = LinkedList()

# добавляем элементы
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(4)

# выводим связный список до изменения
print("До изменения:")
my_list.print_list()

# изменяем связный список
my_list.reverse()
# выводим сенова связный список
print("\nПосле изменения:")
my_list.print_list()

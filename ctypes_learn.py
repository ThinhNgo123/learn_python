import ctypes
# print(ctypes.windll.kernel32)
# print(ctypes.cdll.msvcrt)
class Node(ctypes.Structure):
	pass

Node._fields_ = [("value", ctypes.c_int), ("next", ctypes.POINTER(Node))]
c1 = Node()
c1.value = 1
c2 = Node()
c2.value = 2
c1.next = ctypes.pointer(c2)
c2.next = ctypes.pointer(c1)
p = c1
for i in range(8):
	print(p.value, end=" ")
	print(p.next[0])
	p = p.next[0]
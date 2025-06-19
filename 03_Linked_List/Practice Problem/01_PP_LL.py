# Q.3. What is the output of following function when head node of following linked list is passed as input?
# 1->2->3->4->5
def fun(head):
    if(head==None):
        return
    if head.next.next!= None:
        print(head.data," ",end="")
        fun(head.next)
    print(head.data," ",end="")

# 1 2 3 4 3 2 1
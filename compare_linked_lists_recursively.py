def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 1
    elif headA is None or headB is None:
        return 0

    if headA.data == headB.data:
        return CompareLists(headA.next, headB.next)
    else:
        return 0
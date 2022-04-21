#!/usr/bin/python3
""" You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
""" Write a method that determines if all the boxes can be opened.
@boxes is a list of lists
"""
keys = [0]
for n in keys:
    for key in boxes[n]:
        if key not in keys and key < len(boxes):
            keys.append(key)
<<<<<<< HEAD:0x01-lockboxes/0-lockboxes.py
return len(keys) == len(boxes)
=======
return len(keys) == len(boxes)
>>>>>>> 70bc6f77236a28e00a818cb1a48e005b13e5027e:0x01-lockboxes/    0-lockboxes.py

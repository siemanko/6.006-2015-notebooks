# n * log n solution

from bintrees import FastAVLTree

# read in the first line of input
k, n = [int(x) for x in raw_input().split(' ')]
# read in the second line of input
A    = [int(x) for x in raw_input().split(' ')]
assert len(A) == n

# check all the subsequences and keep the length
best_sequence_length = 0


min_tree = FastAVLTree()
max_tree = FastAVLTree()

def ok():
    if max_tree.is_empty():
        return True
    else:
        difference = max_tree.max_item()[0][0] \
                     - min_tree.min_item()[0][0]
        return  difference <= k

start, end = 0, 0

while end < len(A):
    # extend the sequence until violation reached.
    while end < len(A) and ok():
        best_sequence_length = max(best_sequence_length,
                                   end - start)
        min_tree.insert((A[end], end), None)
        max_tree.insert((A[end], end), None)
        end += 1

    if ok():
        best_sequence_length = max(best_sequence_length,
                           end - start)

    # move starting position by 1.
    min_tree.remove((A[start], start))
    max_tree.remove((A[start], start))
    start += 1

print best_sequence_length

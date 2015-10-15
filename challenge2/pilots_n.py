# n solution

from collections import deque

# read in the first line of input
k, n = [int(x) for x in raw_input().split(' ')]
# read in the second line of input
A    = [int(x) for x in raw_input().split(' ')]
assert len(A) == n

# check all the subsequences and keep the length
best_sequence_length = 0


min_extravaganza = deque()
max_extravaganza = deque()

def ok():
    if len(min_extravaganza) == 0:
        return True
    else:
        difference = A[max_extravaganza[0]] - A[min_extravaganza[0]]
        return  difference <= k

start, end = 0, 0

while end < len(A):
    while end < len(A) and ok():
        best_sequence_length = max(best_sequence_length,
                                   end - start)

        while len(min_extravaganza) > 0 and \
                A[min_extravaganza[-1]] >= A[end]:
            min_extravaganza.pop()
        min_extravaganza.append(end)

        while len(max_extravaganza) > 0 and \
                A[max_extravaganza[-1]] <= A[end]:
            max_extravaganza.pop()
        max_extravaganza.append(end)

        end += 1

    if ok():
        best_sequence_length = max(best_sequence_length,
                                   end - start)

    if min_extravaganza[0] == start:
        min_extravaganza.popleft()
    if max_extravaganza[0] == start:
        max_extravaganza.popleft()
    start += 1

print best_sequence_length

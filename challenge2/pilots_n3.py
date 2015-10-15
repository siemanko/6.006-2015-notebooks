# n^3 solution

# read in the first line of input
k, n = [int(x) for x in raw_input().split(' ')]
# read in the second line of input
A    = [int(x) for x in raw_input().split(' ')]
assert len(A) == n

# check all the subsequences and keep the length
best_sequence_length = 0

for start in range(0, n):
    for end in range(start + 1, n + 1):
        current_seq = A[start:end]
        # line below is O(n)
        difference =  max(current_seq) - min(current_seq)
        if difference <= k:
            best_sequence_length = max(best_sequence_length,
                                       len(current_seq))

print best_sequence_length

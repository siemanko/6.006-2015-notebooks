# n^3 solution

# read in the first line of input
k, n = [int(x) for x in raw_input().split(' ')]
# read in the second line of input
A    = [int(x) for x in raw_input().split(' ')]
assert len(A) == n

# check all the subsequences and keep the length
best_sequence_length = 0

for start in range(0, n):
    minimum_so_far = A[start]
    maximum_so_far = A[start]
    for end in range(start + 1, n + 1):
        minimum_so_far = min(minimum_so_far, A[end - 1])
        maximum_so_far = max(maximum_so_far, A[end - 1])
        # line below is O(n)
        difference =  maximum_so_far - minimum_so_far
        if difference <= k:
            best_sequence_length = max(best_sequence_length,
                                       end - start)
        else:
            # smartness (difference will newer decrease!)
            break

print best_sequence_length

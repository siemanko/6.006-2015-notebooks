# OVERALL COMPLEXITY: O(n)
# here we use a dictionary

def main():
    # n - number of coins
    # k - we need k as many tails as heads
    n, k = [int(v) for v in raw_input().split()]
    # coins - buffer to hold all the characters
    coins = list(raw_input())
    assert len(coins) == n
    coins_as_numbers = []
    for coin in coins:
        if coin == 'R':
            coins_as_numbers.append(k)
        elif coin == 'O':
            coins_as_numbers.append(-1)
        else:
            assert False
    # NEW PROBLEM: find longest contiguous subsequence of
    # sum 0 (sum zero implies k times as many heads)


    # for prefix sums it is important to add an extra element
    # for empty sequence at the beginning.
    prefix_sums = [0]

    # compute the prefix sums
    for coin in coins_as_numbers:
        prefix_sums.append(prefix_sums[-1] + coin)

    # new problem: find a pair of elements in the array,
    # that have the same value and that are furthest
    # away possible.

    # this dictionary maps from array values,
    # to the index of prefix_sums, where the value
    # occurs for the first time
    # Specifically leftmost_index_of_value[S]
    # is equal to smallest such i that prefix_sums[i] = S
    # NOTE: it is build iteratively left to right
    leftmost_index_of_value = {}
    for s_idx, s in enumerate(prefix_sums):
        if s not in leftmost_index_of_value:
            leftmost_index_of_value[s] = s_idx

    res = 0
    for s_idx, s in enumerate(prefix_sums):
        res = max(res, s_idx - leftmost_index_of_value[s])

    print(res)

if __name__ == '__main__':
    main()

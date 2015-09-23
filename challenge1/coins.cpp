#include <algorithm>
#include <cstdio>

// OVERALL COMPLEXITY: O(n lg n)
// (due to sorting)

// maximum number of coins
const int MAXN = 1000005;

// n - number of coins
// k - we need k as many tails as heads
int n, k;
// c - buffer to hold all the characters
char c[MAXN];
// array of (prefix_sum[i], i) values
std::pair<long long, int> seq_and_index[MAXN];

int main() {
    scanf("%d%d", &n, &k);
    scanf("%s", c);
    // for prefix sums it is important to add an extra element
    // for empty sequence at the beginning.
    // this is so that when we compute
    //
    //     seq_and_index[n].second - seq_and_index[0].second
    //
    // we get sum of elements for indexes 1 <= i <= n

    // We reuse seq_and_index for two things
    // initially it just stores values k and -1
    // later we compute prefix sum
    seq_and_index[0] = std::make_pair(0,0);
    for (int i=0; i <n; ++i) {
        // we convert R to k and O to -1
        if (c[i] == 'R') {
            seq_and_index[i + 1].first = k;
        } else {
            seq_and_index[i + 1].first = -1;
        }
        seq_and_index[i+1].second = i + 1;
    }

    // NEW PROBLEM: find longest contiguous subsequence of
    // sum 0 (sum zero implies k times as many heads)

    // compute the prefix sum
    for (int i=1; i <=n; ++i) {
        seq_and_index[i].first += seq_and_index[i-1].first;
    }

    // new problem: find a pair of elements in the array,
    // that have the same value and that are furthest
    // away possible.

    int res = 0;

    // sort by value.
    std::sort(seq_and_index, seq_and_index + n + 1);

    // for all groups with the same value
    // compute max and min index in that group.
    // update result with the difference between those indexes

    int min_index, max_index;
    for (int i=0; i <=n; ++i) {
        if ( i == 0 || seq_and_index[i].first != seq_and_index[i - 1].first) {
            min_index = seq_and_index[i].second;
            max_index = seq_and_index[i].second;
        }
        min_index = std::min(min_index, seq_and_index[i].second);
        max_index = std::max(max_index, seq_and_index[i].second);
        res = std::max(res, max_index - min_index);
    }
    printf("%d\n", res);
}

#include <bits/stdc++.h>

using namespace std;

const int mxN = int(1e6) + 11;

int n = 1000000;
double arr[mxN];

void Modify(int pos, int sz){
    int left = pos*2, right = pos*2 + 1, val = pos;

    if (left <= sz && arr[val] < arr[left]) val = left;
    if (right <= sz && arr[val] < arr[right]) val = right;

    if (arr[val] != arr[pos]){
        swap(arr[val], arr[pos]);
        Modify(val, sz);
    }
}

void HeapSort(){
    for (int i = n / 2; i >= 1; --i) Modify(i, n);

    for (int t = 1; t < n; ++t){
        swap(arr[1], arr[n - t + 1]);
        Modify(1, n - t);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> arr[i];

    HeapSort();

    return 0;
}

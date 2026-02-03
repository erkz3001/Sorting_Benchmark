#include <bits/stdc++.h>

using namespace std;

const int mxN = int(1e6) + 11;

int n;
int arr[mxN], tmp[mxN];

void Merge(int l, int r, int L, int R){
    int id = l, pos = l;
    while (l <= r || L <= R){
        if (l > r) tmp[id++] = arr[L++];
        else if (L > R) tmp[id++] = arr[l++];
        else{
            if (arr[l] < arr[L]) tmp[id++] = arr[l++];
            else tmp[id++] = arr[L++];
        }
    }
    for (int i = pos; i <= R; ++i) arr[i] = tmp[i];
}

void MergeSort(int l, int r){
    if (l > r || l == r) return ;
    int mid = (l + r) >> 1;
    MergeSort(l, mid);
    MergeSort(mid + 1, r);
    Merge(l, mid, mid + 1, r);
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> arr[i];

    MergeSort(1, n);

    return 0;
}

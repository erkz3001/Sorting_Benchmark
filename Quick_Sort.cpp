#include <bits/stdc++.h>

using namespace std;

const int mxN = int(1e6) + 11;

int n = 1000000;
double arr[mxN];

int Partition(int l, int r){
    if (l == r) return r;

    int pivot = rand()%(r - l + 1) + l, p = l;
    swap(arr[pivot], arr[r]);

    pivot = arr[r];

    for (int i = l; i < r; ++i){
        if (arr[i] <= pivot) swap(arr[i], arr[p++]);
    }

    swap(arr[r], arr[p]);

    return p;
}

void QuickSort(int l, int r){
    if (l == r || l > r) return ;
    int pos = Partition(l, r);
    QuickSort(l, pos - 1);
    QuickSort(pos + 1, r);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    srand(unsigned(time(NULL)));

    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> arr[i];

    QuickSort(1, n);

    return 0;
}

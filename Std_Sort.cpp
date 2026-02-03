#include <bits/stdc++.h>
using namespace std;

const int mxN = int(1e6) + 11;

int n;
double arr[mxN];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> arr[i];

    sort(arr + 1, arr + 1 + n);

    return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    long long m, n;
    cin >> n >> m;
    bool* h = new bool[n+1];
    for (long long i = 1; i <= n; i++)
    {
        h[i] = false;
    }
    for (long long i = 1; i <= m; i++)
    {
        long long ocu;
        cin >> ocu;
        h[ocu] = true;
    }
    long long q; cin >> q;
    vector<int> output;
    for (long long i = 0; i < q; i++)
    {
        int opt; cin >> opt;
        if (opt == 1)
        {
            long long idhabitacion; cin >> idhabitacion;
            h[idhabitacion] = false; 
        }
        else if (opt == 2)
        {
            for (long long i = 1; i <=  n; i++)
            {
                if (!h[i])
                {
                    h[i] = true;
                    output.push_back(i);
                    break;
                }
            }
        }
    }
	for(long long i = 0; i < output.size(); i++)
    {
        cout << output[i] << endl;
    }
	return 0;
}
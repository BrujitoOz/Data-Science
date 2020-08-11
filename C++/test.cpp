#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
string twostring(string s1, string s2)
{
	for (int i = 0; i < s1.size(); i++)
	{

		for (int j = 0; j < s2.size(); j++)
		{
			if (s1[i] == s2[j])
			{
				return "YES";
			}
		}
	}
	return "NO";
}
int main()
{
	int n; cin >> n;
	for (int i = 0; i < n; i++)
	{
		string s1; cin >> s1;
		string s2; cin >> s2;
		cout << twostring(s1, s2) << endl;
	}
	
	return 0;
}
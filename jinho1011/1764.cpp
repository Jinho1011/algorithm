#include <cstdio> 
#include <set> 
#include <string> 
#include <iostream> 
#include <vector> 
using namespace std; 
set<string> s1; 
set<string> s2; 
int n, m; 
int main() 
{ 
    scanf("%d %d", &n, &m); 
    string s; 
    for(int i=0;i<n;i++)
    { 
        cin >> s; s1.insert(s); 
    } 
    for(int i=0;i<m;i++)
    { 
        cin >> s; s2.insert(s); 
    } 
    int cnt = 0; 
    vector<string> vt; 
    set<string>::iterator it; 
    for(auto i=s1.begin();i!=s1.end();i++)
    { 
        it = s2.find(*i); 
        if(it != s2.end())
        { 
            vt.push_back(*it); cnt++;
        } 
    }
    printf("%d\n", cnt); 
    for(int i=0;i<vt.size();i++)
    { 
        cout << vt[i] << '\n'; 
    } 
    return 0;
}


#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin>>s;
    
    int c=0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='<') c+=1;
        else c-=1;
    }
    cout<<c;
    
    return 0;
}


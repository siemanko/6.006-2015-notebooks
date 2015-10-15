
#include <cstdio>
#include <algorithm>
#include <queue>
#define ST first
#define ND second
using namespace std;
typedef pair<int,int> PI;


int t,n,T[3000007]; //12 MB
deque<int> MX, MN; // wartosc,pozycja
//TOTAL: 12 MB

bool test(int x) {	
	//printf("%d..\n", x);
	MX.clear(); MN.clear();
	for(int i=0; i<n; ++i) {
		while(!MN.empty() && T[MN.back()]>=T[i]) MN.pop_back();
		MN.push_back(i);
		while(i>=x && MN.front()<=(i-x)) MN.pop_front();
		
		while(!MX.empty() && T[MX.back()]<=T[i]) MX.pop_back();
		MX.push_back(i);
		while(i>=x && MX.front()<=(i-x)) MX.pop_front();
		if(i>=x-1 && T[MX.front()]-T[MN.front()]<=t) return 1;
		//if(i>=x-1) printf("   %d: %d, %d\n", i, T[MN.front()], T[MX.front()]);
	}
	return 0;
} 
	




int main() {
	scanf("%d%d", &t,&n);
	for(int i=0; i<n; ++i) scanf("%d", T+i);
	int l=1,r=n,sr,wyn;
	while(l<=r) {
		sr=(l+r)/2;
		if(test(sr)) { wyn=sr; l=sr+1; }
		else r=sr-1;
	}
	printf("%d\n", wyn);
}

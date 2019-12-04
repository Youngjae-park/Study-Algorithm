#include <stdio.h>
#include <string.h>

int arr[10000];
int test_T;
int max;
int ans;

int main(void){
    int T;
    int s;
    scanf("%d", &T);
    for(int t = 1; t<T+1; t++){
        max=0;
        ans=0;
        scanf("%d", &test_T);
        for(int i=0; i<test_T; i++){
            scanf("%d", &s);
            ans += s+1;
            if(max<s)
            {
                max = s;
            }
        }
        ans += max;
        printf("#%d %d\n", t, ans);
    }
}

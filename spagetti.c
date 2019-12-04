#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    int T;
    scanf("%d", &T);
    for(int test_case=1; test_case<T+1; test_case++){
        int N, B, E;
        scanf("%d %d %d", &N, &B, &E);
        int timer[10000];
        memset(timer,0,sizeof(timer));
        int ans = 0;
        for(int i=0; i<N; i++){
            scanf("%d", &timer[i]);
            int min_timer, max_timer;
            min_timer = timer[i]-E;
            max_timer = timer[i]+E;
            if(min_timer<=B&&max_timer>=B){
                ans++;
                continue;
            }
            while(!(min_timer<=B&&max_timer>=B)){
                min_timer += timer[i];
                max_timer += timer[i];
                if(min_timer<=B&&max_timer>=B){
                    ans++;
                    break;
                }
                if(min_timer>B){
                    break;
                }
            }
        }
        printf("#%d %d\n", test_case, ans);


    }
}

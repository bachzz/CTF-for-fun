#include <stdio.h>

int main(){
	volatile int cookie;
	char buf[16];
	cookie = 0;
	printf("cookie: %d",cookie);
	printf("&buf: %p, &cookie: %p \n", buf,&cookie );
	gets(buf);
	printf("%d\n",cookie);
	if (cookie == 0x41424344){
		printf("you_win!\n");
	}
}

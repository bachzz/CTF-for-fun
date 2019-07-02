#include <stdio.h>
#include <stdlib.h>
#include <sys/signal.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
void timeoout()
{
	puts("Bye bye!!!");
	exit(0);
}
void init()
{
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stdin, 0, 2, 0);
	signal(SIGALRM, timeoout);
	
  	alarm(0x3Cu);
}
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("0x%x ...Nah..\n",key);
	}
}
int main()
{
	init();
	func(0xDEADBEEF);
}
//gcc overflowme.c -o overflowme -fno-stack-protector -m32


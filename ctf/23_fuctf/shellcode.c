#include <sys/mman.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
void timeoout(){
	puts("Bye bye");
	exit(0);
}

void init()
{
	setvbuf(stdout, 0, 2, 0);
	setvbuf(stdin, 0, 2, 0);
	signal(SIGALRM, timeoout);
	
  	alarm(0x3Cu);
}
int main(int argc, char** argv) {
    init();
    char* func = mmap(0, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
   	puts("Google /bin/sh x64 shellcode and bring me what you got");
   	read(0,func,0x1000);

    
   	void (*shellcode)();
   	shellcode= (void (*)())func;
   	shellcode();
    
}

//gcc shellcode.c -o shellcode

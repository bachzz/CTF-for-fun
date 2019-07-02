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
   	puts("I'm back.... can you do it again xD ");
   	read(0,func,0x1000);

    
   	memcpy(func,"\x48\x31\xC0\x48\x31\xDB\x48\x31\xD2\x48\x31\xED\x48\x31\xE4\x48\x31\xC9\x4D\x31\xC0\x48\x31\xFF\x48\x31\xF6\x4D\x31\xC9\x4D\x31\xD2\x4D\x31\xDB\x4D\x31\xE4\x4D\x31\xED\x4D\x31\xF6\x4D\x31\xFF",0x30);
   	void (*shellcode)();
   	shellcode= (void (*)())func;
   	shellcode();
    
}
//gcc shellcoderevenge.c -o shellcoderevenge
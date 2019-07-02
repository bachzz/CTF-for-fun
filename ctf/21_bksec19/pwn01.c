#include <stdio.h>
#include <sys/mman.h>

int main (int argc, char *argv[], char *envp[])
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	char *func = mmap(NULL, 0x1000, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, NULL);
	if (!func) {
		puts("Internal Error");
	}
	printf("Shellcode here: ");
	read(0, func, 0x200);
	void (*fun_ptr)() = func;
	fun_ptr();
}

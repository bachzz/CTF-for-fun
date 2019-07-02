#include <stdio.h>


void vuln() {
	char buf[0x80];
	printf("Input: ");
	read(0, buf, 0x100);
}


int main (int argc, char *argv[], char *envp[])
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	vuln();
}

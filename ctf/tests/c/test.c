#include <stdio.h>
#include <string.h>

int main(int argc, char **argv){
	char str[12];
	scanf("%[^\n]", str);
	printf(str);
	return 0;
}

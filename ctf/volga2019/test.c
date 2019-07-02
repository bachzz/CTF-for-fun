#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
	char s[100];	
	gets(s);	
	FILE *fp = fopen(s, "r");
	char line[100];	
	while (fgets(line, 100, fp) != NULL)
		printf("%s",line);
	fclose(fp);
	char *tmp = line;
	strcpy(tmp, "hello there");
	printf("%s\n", line);
	return 0;
}

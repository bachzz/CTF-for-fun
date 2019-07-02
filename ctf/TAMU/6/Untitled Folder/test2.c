#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  
  char buffer[64];
	volatile int modified;
  modified = 0;
  
	printf("&buf=%p\t&modified=%p",buffer,&modified);
	gets(buffer);
	
  if(modified != 0) {
      printf("you have changed the 'modified' variable\n");
  } else {
      printf("Try again?\n");
  }
}

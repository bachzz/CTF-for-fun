#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <inttypes.h>

int64_t read_int_3()
{
  int64_t v1; // [rsp+0h] [rbp-18h]

  read(0LL, (void*)&v1, 0xFuLL);
  return atol((char *)&v1);
}

int main(){
	int64_t v0;
	v0 = read_int_3();
	printf("%ld\n", v0);
	return 0;
}

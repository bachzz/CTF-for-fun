#include <stdio.h>

void lame (void) { char small[30]; gets (small); printf(‘%sn’, small); }
int main() { lame (); return 0; }

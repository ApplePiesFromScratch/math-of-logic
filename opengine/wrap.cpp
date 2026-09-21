#include <cstdint>
#include <cstdio>
int main() {
    uint8_t x = 255;
    x = x + 1;
    int y = 255 + 1;
    std::printf("byte wrap %u host int %d\n", (unsigned)x, y);
    int *p = nullptr;
    std::printf("null pointer letter %p\n", (void*)p);
    return 0;
}

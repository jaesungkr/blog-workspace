__attribute__((noinline))
int add(int a, int b) {
    return a + b;
}

int absolute_value(int x) {
    return x < 0 ? -x : x;
}

int load_plus_one(const int *value) {
    return *value + 1;
}

int add_then_double(int a, int b) {
    return add(a, b) * 2;
}

"""提供fibonacci数列函数的Cython模块"""
cdef long long fibonacci_cc(unsigned int n) nogil:
    if n < 2:
        return n
    else:
        return fibonacci_cc(n - 1) + fibonacci_cc(n - 2)


def fibonacci(unsigned int n):
    # 解放GIL
    with nogil:
        result = fibonacci_cc(n)

    return fibonacci_cc(n)
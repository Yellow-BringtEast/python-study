#include <Python.h>

long long fibonacci(unsigned int n) {
    if (n < 2) {
        return 1;
    } else {
        return fibonacci(n - 2) + fibonacci(n - 1);
    }
}

static PyObject* fibonacci_py(PyObject* self, PyObject* args) {
    PyObject *result = NULL;
    long n;
    long long fib;

    if (PyArg_ParseTuple(args, "l", &n)) {
        // 防止负数在转换为int时过大，导致深度递归，导致堆栈溢出和分段错误
        if (n < 0) {
            // 在python中抛出错误
            PyErr_SetString(PyExc_ValueError, "n must not be less than 0");
        } else {
            // 保存当前线程状态，并释放GIL
            Py_BEGIN_ALLOW_THREADS;
            fib = fibonacci(n);
            // 重新获取GIL并恢复线程状态
            Py_END_ALLOW_THREADS;


            result = Py_BuildValue("L", fibonacci((unsigned int)n));
        }
    }
    return result;
}

static char fibonacci_docs[] =
    "fibonacci(n): Return nth Fibonacci sequence number"
    "computed recursively\n";

static PyMethodDef fibonacci_module_methods[] = {
    {"fibonacci", (PyCFunction)fibonacci_py,
    METH_VARARGS, fibonacci_docs},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibonacci_module_definition = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    "Extension module that provides fibonacci sequence function",
    -1,
    fibonacci_module_methods
};

PyMODINIT_FUNC PyInit_fibonacci(void) {
    Py_Initialize();

    return PyModule_Create(&fibonacci_module_definition);
}
#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type_name);
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *str;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);

    if (size >= 10) {
        printf("  trying string: ");
        str = PyBytes_AsString(p);
        for (i = 0; i < 10; i++) {
            printf("%02x", (unsigned char)str[i]);
            if (i < 9)
                printf(" ");
        }
        printf("\n");
    } else {
        printf("  trying string: ");
        str = PyBytes_AsString(p);
        for (i = 0; i < size; i++) {
            printf("%02x", (unsigned char)str[i]);
            if (i < size - 1)
                printf(" ");
        }
        printf("\n");
    }
}

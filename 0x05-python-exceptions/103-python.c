#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Print information about a Python float object.
 * @p: The PyObject representing the float.
 */
void print_python_float(PyObject *p)
{
    double value;
    char *string;

    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", string);
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: The PyObject representing the bytes.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);
    string = ((PyBytesObject *)p)->ob_sval;
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", size < 10 ? size : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++)
    {
        printf(" %02hhx", string[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Print information about a Python list object.
 * @p: The PyObject representing the list.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size;
    int i = 0;

    printf("[*] Python list info\n");
    if (PyList_CheckExact(p))
    {
        size = PyList_GET_SIZE(p);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        while (i < size)
        {
            PyObject *item = PyList_GET_ITEM(p, i);
            printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
            if (PyBytes_Check(item))
                print_python_bytes(item);
            else if (PyFloat_Check(item))
                print_python_float(item);
            i++;
        }
    }
    else
    {
        printf("  [ERROR] Invalid List Object\n");
    }
}


#include <python.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	 PyObject *obj;

	 size = py_SIZE(p);
	 alloc = ((PyListObject *)p)->allocated;

	 printf("[*] Size of the python List = %d\n", size);
	 printf("[*] Allocated = %d\n", alloc);

	 for (x = 0; x < size; x++)
	 {
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%d\n", Py_TYPE(obj)->tp_name);
	 }
}

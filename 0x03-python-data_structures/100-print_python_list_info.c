#include <python.h>

void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	 PyObject *obj;

	 size = py_SIZE(p);
	 alloc = ((pyListObject *)p)->allocated;

	 printf("[*] size of the python List = %d\n", size);
	 printf("[*] Allocated = %d\n", alloc);

	 for (x = 0; x < size; x++)
	 {
		printf("Element %d: ", x);

		obj = pyList_GetItem(p, x);
		printf("%d\n", py_TYPE(obj)->tp_name);
	 }
}

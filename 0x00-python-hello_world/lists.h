#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>


typedef struct listsint_search
{
	int n;
	struct listsint_search *next;
} listsint_text;

// printList int prototype
size_t printListInt(const listsint_text *h);
// addNode int prototype
listsint_text *addNodeInt(listsint_text **head, const int n);
// freeListInt prototype
void freeListInt(listsint_text *head);
// checkCycle prototype
int checkCycle(listsint_text *list);

#endif


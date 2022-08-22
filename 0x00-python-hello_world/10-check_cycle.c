#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer
 * Return: 0 if yes 1 if no
 */
int check_cycle(listint_t *list)
{
listint_t *p = list;
listint_t *q = list;
while (p != NULL && q != NULL)
{
if (p == q)
return (0);
p = p->next->next;
q = q->next;
}
return (1);
}

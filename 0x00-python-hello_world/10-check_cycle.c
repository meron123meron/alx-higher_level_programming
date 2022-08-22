#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer
 * Return: 1 if yes 0 if no
 */
int check_cycle(listint_t *list)
{
listint_t *p = list;
listint_t *q = list;
if (list == NULL)
return (0);
while (p != NULL && q != NULL && p->next != NULL)
{
if (p == q)
return (1);
p = p->next->next;
q = q->next;
}
return (0);
}

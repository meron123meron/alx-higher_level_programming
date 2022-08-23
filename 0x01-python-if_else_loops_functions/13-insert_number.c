#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - a function that insets a new node in singly linked list
 * @head: double pointer
 * @number: integer
 * Return: address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *p;
listint_t *q;
q = *head;
p = malloc(sizeof(listint_t));
if (p == NULL)
return (NULL);
p->n = number;
if (*head == NULL)
{
p->next = *head;
*head = p;
return (p);
}
while (q->next != NULL)
{
if (q->next->n > number)
{
p->next = q->next;
q->next = p;
return (p);
}
q = q->next;
}
return (p);
}

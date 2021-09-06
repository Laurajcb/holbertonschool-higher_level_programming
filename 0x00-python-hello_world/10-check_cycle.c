#include "lists.h"
/**
 * check_cycle - function that checks if a SLL has a cycle on it
 * @list: singly list
 * Return: 0 if there is no cycle, 1 if there is one
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *tmp = list;

	while (tmp && tmp->next)
	{
		current = current->next;
		tmp = tmp->next->next;
		if (current == tmp)
		{
			return (1);
		}
	}
	return (0);
}

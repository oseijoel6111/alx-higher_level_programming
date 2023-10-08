#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *stack = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1); // An empty list or a list with a single node is considered a palindrome

    // Traverse the list with two pointers: slow and fast
    while (fast != NULL && fast->next != NULL)
    {
        stack_push(&stack, slow->n);
        slow = slow->next;
        fast = fast->next->next;
    }

    // If the length of the list is odd, skip the middle element
    if (fast != NULL)
        slow = slow->next;

    // Compare the remaining elements with the stack
    while (slow != NULL)
    {
        int top = stack_pop(&stack);

        if (top != slow->n)
            return (0); // Not a palindrome

        slow = slow->next;
    }

    return (1); // It is a palindrome
}

/**
 * stack_push - pushes a value onto a stack
 * @stack: double pointer to the top of the stack
 * @value: value to push onto the stack
 */
void stack_push(listint_t **stack, int value)
{
    listint_t *new_node = malloc(sizeof(listint_t));

    if (new_node == NULL)
    {
        perror("Unable to allocate memory");
        exit(EXIT_FAILURE);
    }

    new_node->n = value;
    new_node->next = *stack;
    *stack = new_node;
}

/**
 * stack_pop - pops a value from a stack
 * @stack: double pointer to the top of the stack
 *
 * Return: the value popped from the stack
 */
int stack_pop(listint_t **stack)
{
    int value;
    listint_t *temp;

    if (*stack == NULL)
    {
        perror("Stack is empty");
        exit(EXIT_FAILURE);
    }

    value = (*stack)->n;
    temp = *stack;
    *stack = (*stack)->next;
    free(temp);

    return value;
}


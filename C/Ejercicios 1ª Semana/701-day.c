/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   701-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/16 22:14:09 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/16 22:14:09 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strcmp(char *str1, char *str2)
{
	if (!str1 || !str2)
		return (-1);
	while (*str1 && (*str1 == *str2))
	{
		str1++;
		str2++;
	}
	return (*str1 - *str2);
}

float	ft_calculator(float num1, float num2, char operation[12])
{
	float	resoult;

	if (ft_strcmp(operation, "suma") == 0 ||
	ft_strcmp(operation, "Suma") == 0)
	{
		resoult = num1 + num2;
		return (resoult);
	}
	else if (ft_strcmp(operation, "resta") == 0 ||
	ft_strcmp(operation, "Resta") == 0)
	{
		resoult = num1 - num2;
		return (resoult);
	}
	else if (ft_strcmp(operation, "multiplicacion") == 0 ||
	ft_strcmp(operation, "Multiplicacion") == 0)
	{
		resoult = num1 * num2;
		return (resoult);
	}
	else if (ft_strcmp(operation, "division") == 0 ||
	ft_strcmp(operation, "Division") == 0)
	{
		resoult = num1 / num2;
		return (resoult);
	}
	else
	{
		printf("No encuentro operación\n");
		return (1);
	}
}

int	main(void)
{
	float	num1;
	float	num2;
	char	operation[15];
	float	resoult;

	printf("Introduce el primer valor\n");
	scanf("%f", &num1);
	printf("Introduce el segundo valor\n");
	scanf("%f", &num2);
	printf("¿Que operación deseas realizar?\n");
	scanf("%s", operation);
	if (num2 == 0 && (ft_strcmp(operation, "division") == 0 ||
	ft_strcmp(operation, "Division") == 0))
	{
		printf("División entre 0 es invalido\n");
		return (1);
	}
	else
	{
		resoult = ft_calculator(num1, num2, operation);
		printf("El resultado de la %s es %.2f\n", operation, resoult);
		return (0);
	}
}

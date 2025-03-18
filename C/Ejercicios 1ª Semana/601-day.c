/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   601-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/16 12:27:04 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/16 12:27:04 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	float	num1;
	float	num2;

	printf("Introduce el primer numero:\n");
	scanf("%f", &num1);
	printf("Introduce el segundo numero:\n");
	scanf("%f", &num2);
	if (num1 > num2)
	{
		printf("%.2f es mayor que %.2f\n", num1, num2);
	}
	else if (num1 == num2)
	{
		printf("%.2f y %.2f son iguales\n", num1, num2);
	}
	else
	{
		printf("%.2f es menor que %.2f\n", num1, num2);
	}
	return (0);
}


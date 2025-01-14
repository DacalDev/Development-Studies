/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operadores_aritmrticos.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/14 22:23:14 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/14 22:23:14 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	int	num1, num2;
	int	a, b;
	int	suma, resta;
	int	multiplicacion, division;

	a = 12;
	b = 3;
	printf("Ingrese el primer valor:\n");
	scanf("%d", &num1);
	printf("Ingrese el segundo valor:\n");
	scanf("%d", &num2);
	suma = num1 + num2 + a + b;
	resta = num1 - num2 - a - b;
	multiplicacion = num1 * (a + num2) * num2 * (b + num1);
	division = a / b;
	printf("Los resultados de las operaciones son:\n");
	printf("Suma: %d\n", suma);
	printf("Resta: %d\n", resta);
	printf("Multiplicacion: %d\n", multiplicacion);
	printf("Division: %d\n", division);
	return (0);
}

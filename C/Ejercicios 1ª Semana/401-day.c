/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   401-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/14 22:21:28 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/14 22:21:28 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	int		suma;
	int		resta;
	int		multiplicacion;
	float	division;
	int		a;
	int		b;

	printf("Introduce el primer valor:\n");
	if (scanf("%d", &a) != 1)
	{
		printf("Error en la entrada.\n");
		return (1);
	}
	printf("Introduce el segundo valor:\n");
	if (scanf("%d", &b) != 1)
	{
		printf("Error en la entrada.\n");
		return (1);
	}
	suma = a+b;
	resta = a-b;
	multiplicacion = a*b;
	printf("Suma: %d\n", suma);
	printf("Resta: %d\n", resta);
	printf("Multiplicación: %d\n", multiplicacion);
	if (b != 0)
	{
		division = (float)a / (float)b;
		printf("División: %.2f\n", division);
	}
	else
	{
		printf("Error: División por cero no es posible.\n");
	}
	return (0);
}

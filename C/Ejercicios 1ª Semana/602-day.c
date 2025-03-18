/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   602-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/16 21:50:14 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/16 21:50:14 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	int	age;

	printf("¿Cual es tu edad?\n");
	if (scanf("%d", &age) != 1)
	{
		printf("Error en la entrada.\n");
		return (1);
	}
	if (age < 18)
	{
		printf("Eres menor de edad\n");
	}
	else if (age >= 18 && age <= 60)
	{
		printf("Eres adulto\n");
	}
	else
	{
		printf("Tu cuerpo pide tierra\n");
	}
	return (0);
}

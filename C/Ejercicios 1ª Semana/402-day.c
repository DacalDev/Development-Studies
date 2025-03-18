/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   402-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/15 21:22:24 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/15 21:22:24 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#define PI 3.14159

int	main(void)
{
	float radius;
	float area;

	printf("Introduce el radio del circulo:\n");
	scanf("%f", &radius);
	area = PI * (radius * radius);
	printf("El area del circulo es: %.2f\n", area);
	return (0);
}

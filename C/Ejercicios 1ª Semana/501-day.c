/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   501-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/15 21:12:23 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/15 21:12:23 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	int	number;
	int	i;

	i = 0;
	printf("Introduce el numero del que quieras saber su tabla:\n");
	scanf("%d", &number);
	while (i < 11)
	{
		printf("%d x %d = %d\n", number, i, number * i);
		i++;
	}
	return (0);
}

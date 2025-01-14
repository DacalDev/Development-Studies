/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   301-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/14 22:22:40 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/14 22:22:40 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	float	farenheit;
	float	celsius;

	celsius = 15.33;
	farenheit = ((celsius * 9/5) + 32.0);
	printf("%0.2f grados Celsius, son %0.2f grados Farenheit\n",celsius, farenheit);
	return(0);
}

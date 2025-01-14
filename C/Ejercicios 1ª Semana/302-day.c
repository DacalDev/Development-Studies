/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   302-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/14 22:22:44 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/14 22:22:44 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	main(void)
{
	char	nombre[]="Javier";
	int		edad;
	float	peso;

	edad = 38;
	peso = 78.5;
	printf("Mi nombre es %s, tengo %d años y peso %0.1f Kg\n",nombre, edad, peso);
	return(0);
}

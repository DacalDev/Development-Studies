/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   502-day.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jdacal-a <jdacal-a@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/01/15 21:33:12 by jdacal-a          #+#    #+#             */
/*   Updated: 2025/01/15 21:33:12 by jdacal-a         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int main(void)
{
	char str[15];

	printf("¿Cómo te llamas?\n");
	fgets(str, sizeof(str), stdin); // Leer la línea completa
	printf("Hola, %s, ¡Bienvenido al lenguaje C!\n", str);
	return (0);
}

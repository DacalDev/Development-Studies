/*Toma de decisiones if

Operadores de Igualdad
== X es igual a Y
!= X es diferente de Y

Operadores Relacionales
> X es mayor que Y
< X es menor que Y
>= X es mayor o igual que Y
<= X es menor o igual que Y
*/

#include <stdio.h>

int	main(void)
{
	int	edad;

	printf("Ingrese su edad:\n");
	scanf("%d", &edad);
	if (edad >= 18)
	{
		printf("Eres mayor de edad\n");
	}
	else if (edad == 17)
	{
		printf("Casi eres mayor de edad, pero no\n");
	}
	else
	{
		printf("Eres menor de edad\n");
	}
	return (0);
}

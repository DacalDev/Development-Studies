#include <stdio.h>

int	main(void)
{
	int	num1;
	int	num2;
	int	resultado;

	printf("Ingrese el primer valor\n");
	scanf("%d", &num1);
	printf("Ingrese el segundo valor\n");
	scanf("%d", &num2);
	resultado = num1 + num2;
	printf("El resultado de la suma es: %d\n", resultado);
	return (0);
}

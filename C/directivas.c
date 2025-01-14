/*Directivas del Preprocesador*/

#include <stdio.h> //incluye un archivo de cabecera estándar de entrada y salida
//#include "nombre del archivo" //incluye un archivo de cabecera ubicado en el directorio actual

#define PI 3.14159 //Definir una constante
#define CUBO(a) ((a)*(a)*(a)) //Definir una macro

int	main(void)
{
	float	suma;
	int		a;

	suma = PI + 3;
	a = 3;
	printf("La suma es: %f\n", suma);
	printf("El cubo de %d es: %d\n", a, CUBO(a));
	return (0);
}

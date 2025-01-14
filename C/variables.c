/*Variables*/

#include <stdio.h>

int	main(void)
{
	int					a; // int se usa para enteros, 2 bytes de -32768 a 32767
	float				f; // float se usa para decimales
	char				c; // char se usa para caracteres, 1 byte de -128 a 127 (ASCII) o de 0 a 255
	char				str[] = "Hello"; // Definir una cadena de caracteres (string)
	long				l; // long se usa para enteros largos, 4 bytes de -2147483648 a 2147483647
	unsigned int		u; // unsigned se usa para enteros positivos, 2 bytes de 0 a 65535
	unsigned long		g; // unsigned se usa para enteros positivos, 4 bytes de 0 a 4294967295
	unsigned long long	h; // unsigned se usa para enteros positivos, 8 bytes de 0 a 18446744073709551615
	short				e; // short se usa para enteros cortos, 2 bytes de -32768 a 32767
	double				d; // double se usa para decimales largos, 8 bytes de -1.7E308 a 1.7E308

	// Asignación de valores
	a = 10;
	f = 10.5;
	c = 'x';
	l = 2147483647;
	u = 65535;
	g = 4294967295;
	h = 18446744073709551615;
	e = -32768;
	d = 1.7E308;

	// Impresión de valores
	printf("a = %d\n", a); // Imprimir entero
	printf("f = %.1f\n", f); // Imprimir float
	printf("c = %c\n", c); // Imprimir carácter
	printf("str = %s\n", str); // Imprimir cadena
	printf("l = %ld\n", l); // Imprimir long
	printf("u = %u\n", u); // Imprimir unsigned int
	printf("g = %lu\n", g); // Imprimir unsigned long
	printf("h = %llu\n", h); // Imprimir unsigned long long
	printf("e = %d\n", e); // Imprimir short (int, ya que short se convierte en int en printf)
	printf("d = %f\n", d); // Imprimir double

	return (0);
}

/*
Data types specify the different sizes and values that can 
be stored in the variable. There are two types of data types 
in Java:

1. Primitive data types: The primitive data types include boolean, 
char, byte, short, int, long, float and double.

2. Non-primitive data types: The non-primitive data types include 
Classes, Interfaces, and Arrays.
*/

class DataTypes{
	public static void main(String args[]){
		Boolean a = false; // size cant be defined precisely
		Byte b = 10; // 1 byte, -128 to 127
		Short c = 1000; // 2 bytes, -32,768 to 32,767
		int d = 20000; // 4 bytes, -2^31 to (2^31)-1
		long e = 10000000; // 8 bytes, -2^63 to (2^63)-1
		float f = 2; // 4 bytes, unlimited range single-precision 32bit floating point
		double g = 12.41; // 8 bytes, unlimited range double-precision 64bit floating point
		char h = 'A'; // 2 bytes, 0 to 65,535

		// java uses Unicode system thus has 2 bytes for char

		System.out.println("Boolean: " + a);
		System.out.println("Byte: " + b);
		System.out.println("Short: " + c);
		System.out.println("Int: " + d);
		System.out.println("Long: " + e);
		System.out.println("Float: " + f);
		System.out.println("Double: " + g);
		System.out.println("Char: " + h);

	}
}
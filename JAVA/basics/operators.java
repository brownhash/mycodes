class Operators{

	public static void main(String args[]){
		int x = 10;
		int y = -11;
		boolean b = true;
		boolean c = false;
		System.out.println("x = " + x);

		System.out.println("\n-- postfix and prefix --\n");
		System.out.println(x++); // prints 10 and then increments
		System.out.println(x); // prints 11
		System.out.println(++x); // increments x and then prints 12
		System.out.println(x--); // prints x and then decrements 12
		System.out.println(x); // prints decremented x 11
		System.out.println(--x); // prints 10

		System.out.println("\n-- postfix and prefix in mathematical operations--\n");
		System.out.print("x++ + ++x = ");
		System.out.print((x++ + ++x) + "\n"); // x=10 -> x>11 -> + -> x>12 -> x=12 -> 10 + 12

		System.out.println("\n-- unary operator ~ ! --\n");

		System.out.println("x = " + x);
		System.out.println("y = " + y);
		System.out.println("~x = " + (~x)); // -ve of all values from 0 till x
		System.out.println("~y = " + (~y)); // +ve of all values from -1 till y

		System.out.println("b = " + b);
		System.out.println("c = " + c);
		System.out.println("!b = " + (!b));
		System.out.println("!c = " + (!c));

		System.out.println("\n-- precedence --\n");

		System.out.println("10*10/5+3-1*4/2 = " + (10*10/5+3-1*4/2));

		System.out.println("\n-- Right shift --\n");

		System.out.println("x = " + x);
		System.out.println("x>>2 = " + (x>>2)); // x/2^2
		System.out.println("x>>5 = " + (x>>5)); // x/2^2

		System.out.println("\n-- left shift --\n");

		System.out.println("x = " + x);
		System.out.println("x<<2 = " + (x<<2)); // x*2^2
		System.out.println("x<<5 = " + (x<<5)); // x*2^2

		System.out.println("\n-- >> vs >>> --\n");

		System.out.println("x = " + x);
		System.out.println("y = " + y);
		System.out.println("x>>2 = " + (x>>2)); // x/2^2
		System.out.println("x>>>5 = " + (x>>>5)); // x/2^2
		System.out.println("y>>2 = " + (y>>2)); // y/2^2
		System.out.println("y>>>5 = " + (y>>>5)); // changes parity bit (MSB) to 0

		System.out.println("\n-- terenary operator --\n");

		int e = 5;
		int f = 6;
		int min = (e<f)?e:f;
		int min2 = (e>f)?e:f;
		System.out.println("e = " + e);
		System.out.println("f = " + f);
		System.out.println("min = (e<f)?e:f = " + min); // x/2^2
		System.out.println("min2 = (e>f)?e:f = " + min2); // x/2^2
	}
}
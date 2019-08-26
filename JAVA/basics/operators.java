class Operators{

	public static void main(String args[]){
		int x = 10;

		System.out.println("\n-- postfix and prefix --\n");
		System.out.println(x++); // prints 10 and then increments
		System.out.println(x); // prints 11
		System.out.println(++x); // increments x and then prints 12
		System.out.println(x--); // prints x and then decrements 12
		System.out.println(x); // prints decremented x 11
		System.out.println(--x); // prints 10

		System.out.println("\n-- postfix and prefix in mathematical operations--\n");
		System.out.println(x++ + ++x); // x=10 -> x>11 -> + -> x>12 -> x=12 -> 10 + 12
	}
}
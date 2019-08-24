/*
1) Local Variable -
A variable declared inside the body of the method is called local variable. 
You can use this variable only within that method and the other methods in 
the class aren't even aware that the variable exists.

A local variable cannot be defined with "static" keyword.

2) Instance Variable -
A variable declared inside the class but outside the body of the method, 
is called instance variable. It is not declared as static.

It is called instance variable because its value is instance specific and 
is not shared among instances.

3) Static variable -
A variable which is declared as static is called static variable. It cannot 
be local. You can create a single copy of static variable and share among all 
the instances of the class. Memory allocation for static variable happens 
only once when the class is loaded in the memory.
*/


class Variables{
	char ch = 'H';
	static int dollar = 20;

	// static method (Will run without an object)
	public static void main(String args[]){
		System.out.println("\n-- Local variables --");
		int num = 50;
		float numf = num;
		System.out.println("Number = " + num);
		System.out.println("Float Number = " + numf);
		System.out.println("Multiplication on number = " + (num*2));

		System.out.println("-- --");

		char character = 'A';
		System.out.println("Character = " + character);

		System.out.println("-- --");

		String string = "harshit Sharma";
		System.out.println("String = " + string);

		System.out.println("\n-- Static variables --");

		System.out.println("Static variable = " + dollar);

		// creating an object of the class to call instance method
		Variables myObj = new Variables();
		myObj.myFunction();

	}

	// instance method
	public void myFunction(){
		System.out.println("\n-- Instance variables --");

		System.out.println("Instance variable = " + ch);
	}



}

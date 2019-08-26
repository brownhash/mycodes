class IfElse{
	public static void main(String args[]){
		double maths = 88.5;
		double chem = 53;
		double phy = 85.5;
		double eng = 80;

		double avg = (maths + phy + chem + eng)/4;

		System.out.println("Average = " + avg);

		if(avg > 90){
			System.out.println("Grade: A+");
		}
		else if (avg > 80){
			System.out.println("Grade: A");
		}
		else if (avg > 70){
			System.out.println("Grade: B+");
		}
		else if (avg > 60){
			System.out.println("Grade: B");
		}
		else if (avg > 50){
			System.out.println("Grade: C");
		}
		else if (avg > 40){
			System.out.println("Grade: D");
		}
		else{
			System.out.println("Grade: Fail");
		}
	}
}
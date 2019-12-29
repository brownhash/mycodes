class loops {
    public static void main(String args[]) {
        int a, n;
        a = 10;

        System.out.println("\nFor loop");
        // for loop
        for (n=1; n<=a; n++) {
            System.out.println(n);
        }

        System.out.println("\nWhile loop");
        // while loop
        while (a > 0) {
            System.out.println(a);
            a--;
        }
    }
}
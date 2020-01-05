class loops {
    public static void main(String[] args) {
        int i = 0;
        while(i < 10) {
            System.out.println("i is - " + i);
            i++;
        }

        System.out.println("\n----\n");
        do {
            System.out.println("always executes");
            i++;
        } while(i<10);

        System.out.println("\n----\n");
        for (int a =0, b=10; a<b; a++, b--) { // using comma to separate more than 1 staements in the condition
            System.out.println("a = " + a + " & b = " + b);
        }

        System.out.println("\n----\n");
        boolean done = false;

        // making for to execute while done is not set to true
        // behaving similar to while
        for ( ; !done ; ) {
            System.out.println("Seting done to true");
            done = true;
        }

        System.out.println("\n----\n");
        done = false;

        for ( int j=0 ; !done ; j++ ) {
            System.out.println("Will set done true when j = 5");
            if (j == 5) {
                System.out.println("Setting done to true");
                done = true;
            }
        }

        System.out.println("\n----\n");
        int nums[] = {1,2,3,4,5,6,7,8,9,10};
        int sum = 0;

        for (int x : nums) { // for-each loop
            System.out.println("Value: " + x);
            sum += x;
        }
        System.out.println("Sum = " + sum);

        System.out.println("\n----\n");
        int nums2[][] = new int[5][5];
        int sum2 = 0;

        for (int a=0; a<5; a++){
            for (int b=0; b<5; b++){
                nums2[a][b] = a+b;
            }
        }

        for (int c[] : nums2){ // iterating for-each on multi dimensional arrays
            for (int d : c) {
                sum2 += d;
                System.out.println("Value: " + d);
            }
        }
        System.out.println("Sum = " + sum2);
    }
}
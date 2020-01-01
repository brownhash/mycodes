class operators {
    public static void main(String[] args) {
        int x = 10, y = 20;

        // increment and decrement
        System.out.println("\n----\nIncrement and Decrement - \n----\n");
        System.out.println("++x = " + ++x); //first increment and then print
        System.out.println("x = " + x); // value of x, now
        System.out.println("x++ = " + x++); // first print and then increment
        System.out.println("x = " + x); // value of x, now

        System.out.println("--x = " + --x); //first decrement and then print
        System.out.println("x = " + x); // value of x, now
        System.out.println("x-- = " + x--); // first print and then decrement
        System.out.println("x = " + x); // value of x, now

        // bitwise
        System.out.println("\n----\nNOT - \n----\n");
        System.out.println("x = " + x + ", y = " + y);
        System.out.println("~x = " + ~x); // reverts the bits of the operand

        System.out.println("\n----\nAND - \n----\n");
        System.out.println("x = " + x + " & y = " + y);
        System.out.println(x&y);
        x=20;
        System.out.println("x = " + x + " & y = " + y);
        System.out.println(x&y);
        /*
        AND
        & operator -
        A = 1001110
        B = 0100111
        -----------
        C = 0000110
        -----------
        C = A&B

        returns 1 if both operands are 1
        else 0 in all other cases
         */

        System.out.println("\n----\nOR - \n----\n");
        x = 10;
        System.out.println("x = " + x + " | y = " + y);
        System.out.println(x|y);
        /*
        OR
        | operator -
        x = 00001010  i.e. 10
        y = 00010100  i.e. 20
        ------------
        C = 00011110  i.e. 30
        ------------
        C = x|y

        returns 1 if any operand is 1
        else 0 in other case
         */

        System.out.println("\n----\nXOR - \n----\n");
        x = 40;
        System.out.println("x = " + x + " ^ y = " + y);
        System.out.println(x^y);
        /*
        XOR
        ^ operator -
        x = 00101000  i.e. 40
        y = 00010100  i.e. 20
        ------------
        C = 00111100  i.e. 60
        ------------
        C = x^y

        returns 1 if exactly one operand is 1
        else 0 in other cases
         */

        System.out.println("\n----\nLeft shift - \n----\n");
        x = 2;
        System.out.println("x = " + x);
        System.out.println("x<<1");
        System.out.println(x<<1); // shifting bits to 1 place left
        System.out.println("x = " + x);
        System.out.println("x<<2");
        System.out.println(x<<2); // shifting bits to 2 place left

        System.out.println("\n----\nUnsigned left shift - \n----\n");
        x = -2;
        System.out.println("x = " + x);
        System.out.println("x<<1");
        System.out.println(x<<1); // shifting bits to 1 place left
        System.out.println("x = " + x);
        System.out.println("x<<2");
        System.out.println(x<<2); // shifting bits to 2 place left

        System.out.println("\n----\nRight shift - \n----\n");
        x = 10;
        System.out.println("x = " + x);
        System.out.println("x>>1");
        System.out.println(x>>1); // shifting bits to 1 place right
        System.out.println("x = " + x);
        System.out.println("x>>2");
        System.out.println(x>>2); // shifting bits to 2 place right

        System.out.println("\n----\nUnsigned right shift - \n----\n");
        x = -10;
        System.out.println("x = " + x);
        System.out.println("x>>1");
        System.out.println(x>>1); // shifting bits to 1 place right
        System.out.println("x = " + x);
        System.out.println("x>>2");
        System.out.println(x>>2); // shifting bits to 2 place right
    }
}
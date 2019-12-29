class datatypes {
    public static void main(String[] args) {
        /*
        primitive types -
        1. int
            long (64) -2e63 to 2e63
            int (32)
            short (16)
            byte (8)

        2. float
            double (64) 4.9e-324 to 1.8e+308
            float (32) 1.4e-45 to 3.4e+38

        3. chars 0 to 65536
        4. boolean
         */

        byte b, b2;
        int i, i2;
        long l, l2;
        short s, s2;

        /*
        range of byte is from -128 to 127
         */
        b = 127;
        b2 = -128;
        System.out.println("\nByte:");
        System.out.println(b + " " + b2);

        /*
        range of int is from -2147483648 to 2147483647
         */
        i = 2147483647;
        i2 = -2147483648;
        System.out.println("\nInteger:");
        System.out.println(i + "  " + i2);

        int dyn;
        dyn = i - 10000;
        System.out.println("Dynamic allocated value: " + dyn);

        int oct = 01, oct2 = 07; // octal values
        System.out.println("Octals: " + oct + " " + oct2);

        int hex = 0x1, hex2 = 0xf; // hexadecimal values
        System.out.println("Hexadecimals: " + hex + " " + hex2);

        int bin = 0b01001;
        System.out.println("Binary: " + bin);

        /*
        range of short is from -32768 to 32767
         */
        s = 32767;
        s2 = -32768;
        System.out.println("\nShort:");
        System.out.println(s + " " + s2);

        /*
        range of long is from -9223372036854775808 to 9223372036854775807
         */
        l = 9_223_372_036_854_775_807L; // underscore is used to clearly view large numbers
        l2 = -9_223_372_036_854_775_808L;
        System.out.println("\nLong:");
        System.out.println(l + " " + l2);

        float f, f2;
        f = 2.343f; // standard notation
        f2 = 2.34E10f; // scientific notation
        System.out.println("\nFloating point (float):");
        System.out.println(f + " " + f2);

        double d, d2;
        d = 2.343; // standard notation
        d2 = 2.34E10; // scientific notation
        System.out.println("\nFloating point (double):");
        System.out.println(d + " " + d2);

        char c1, c2, c3 = 22 + 44;

        c1 = 88;
        c2 = 'Y';
        System.out.println("\nCharacters:");
        System.out.println("88 -> " + c1);
        System.out.println(c2);
        System.out.println("22 + 44 -> " + c3);

        char c4, c5, c6;
        System.out.println("\nCharacters (octal and hexa):");
        c4 = '\141';
        System.out.println("octal \'\\141\' -> " + c4);
        c5 = '\u0061';
        System.out.println("hexadecimal \'\\u0061\' -> " + c5);
        c6 = '\ua432';
        System.out.println("hexadecimal \'\\ua432\' -> " + c6 + " (A japanese character)");

        System.out.println("\nEscape sequences:");
        System.out.println("\\\' -> \'");
        System.out.println("\\\" -> \"");
        System.out.println("\\\\ -> \\");
        System.out.println("\\r -> x\ry"); // carriage return
        System.out.println("\\n -> x\ny"); // new line
        System.out.println("\\f -> x\fy"); // form feed
        System.out.println("\\t -> x\ty"); // tab
        System.out.println("\\b -> x\by"); // backspace

        boolean bl = true, bl2 = false;
        System.out.println("\nBoolean:");
        System.out.println(bl + " " + bl2);
    }
}
class type_casting {
    public static void main(String[] args) {
        byte b, c, e;
        int i = 257, j;
        double d = 323.142, f = 2.3, g;

        // type conversion
        System.out.println("\nInt to byte:");
        b = (byte) i;
        System.out.println(i + " -> " + b);

        System.out.println("\nDouble to Int:");
        i = (int) d;
        System.out.println(d + " -> " + i);

        System.out.println("\nDouble to byte:");
        b = (byte) d;
        System.out.println(d + " -> " + b);

        c = 26;
        e = 45;
        /*
        Type promotion-
        as c * e exceeds the range for byte
        thus the result is in int
         */
        j = c * e;
        System.out.println("\nResult byte * byte = int -> " + j);
        g = c * e * f;
        System.out.println("\nResult byte * byte * double = double -> " + g);
    }
}
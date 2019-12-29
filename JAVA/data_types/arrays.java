class arrays{
    public static void main(String[] args) {
        /*
        types of declarations-
        int a[] = new int[5];
        int[] a = new int[5];
         */

        // one dimensional array
        int dates[] = new int[30];
        int i, j;

        for (i=0; i<30; i++) {
            dates[i] = i+1;
        }

        for (i=0; i<30; i++) {
            System.out.println(dates[i]);
        }

        // multi dimensional array

        int month[][] = new int [12][31];
        for (i=0; i<12; i++) {
            for (j=0; j<31; j++) {
                month[i][j] = j+1;
            }
        }

        for (i=0; i<12; i++) {
            for (j=0; j<31; j++) {
                System.out.println(month[i][j]);
            }
        }
    }
}
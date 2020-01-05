class break_as_goto {
    public static void main(String[] args) {
        boolean t = true;
        first: {
            second: {
                third: {
                    System.out.println("Third block");
                    if(t) break second; // >----------------------------------------|
                    System.out.println("Third block second statement"); //          |
                } //                                                                |
                System.out.println("Second block"); // wont execute        X <------|
            } //                                                                    |
            System.out.println("First block"); // <---------------------------------|
        }

        outer: for (int i=0; i<10; i++) {
            inner: for (int j=0; j<5; j++){
                System.out.println(i + " - " + j);
                if (i==(j*2) && j!=0) {
                    break outer;
                }
            }
        }
    }
}
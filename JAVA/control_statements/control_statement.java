class control_statement{
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            switch (i) { // switching on iteration of i
                case 0:
                    System.out.println("Case 0");
                    break;
                case 1:
                    System.out.println("Case 1");
                    break;
                case 2:
                    System.out.println("Case 2");
                    break;
                default:
                    System.out.println("Default case executed for:"+i);
                    break;
            }
        }
    }
}
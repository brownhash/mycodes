class search {
    public static void main(String[] args) {
        int num[] = {2,4,5,43,56,7,8,32,12,32,12};
        int x = 43;
        boolean found = false;

        for (int y : num) {
            if ( x == y){
                found = true;
                break;
            }
        }

        if (found == true) {
            System.out.println(x + " is in the array!");
        }
        else{
            System.out.println(x + " is not in the array!");
        }
    }
}
import java.lang.Math;

class Prime{
    public static void main(String[] args) {
        int num = 2063;
        System.out.println("Input number: " + num);

        Prime obj = new Prime();
        obj.check_prime(num);
    }
    public void check_prime(int num){
        boolean flag = true;
        for(int i = 2; i < Math.sqrt(num)+1 ; i++){
            if(num % i == 0){
                flag = false;
            }
        }
        if(flag == true){
            System.out.println(num + " is Prime");
        }
        else{
            System.out.println(num + " is not Prime");
        }
    }
}
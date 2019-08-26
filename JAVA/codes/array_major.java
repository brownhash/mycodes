// calculating the major elements in an array
// major element is the one which occurs the most in an array

import java.io.*;
import java.util.*;
import java.util.Random;

class ArrayMajor{
    public static void main(String[] args) {
        // int arr[] = new int[100];
        List<Integer> arr = new ArrayList<Integer>();
        List<Integer> arr_count = new ArrayList<Integer>();
        Random rand = new Random();

        for(int i = 0; i < 100; i++){
            arr.add(rand.nextInt(1000));
        }
        for(int i = 0; i < 100; i++){
            int elem = arr.get(i);
            int count = 0;
            for(int j = 0; j < 100; j++) {
                int temp = arr.get(j);
                if(temp == elem){
                    count ++;
                }
            }
            arr_count.add(count);
        }
        int max = arr_count.get(0);
        int index = 0;
        for(int i = 0; i < 100; i++){
            if(arr_count.get(i) > max){
                index = i;
                max = arr_count.get(i);
            }
        }
        System.out.println(arr.get(index));
    }
}
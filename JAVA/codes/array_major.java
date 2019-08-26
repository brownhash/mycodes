// calculating the major elements in an array
// major element is the one divisible by 3 & 7

import java.io.*;
import java.util.*;

class ArrayMajor{
    public static void main(String[] args) {
        // int arr[] = new int[100];
        List<Integer> arr = new ArrayList<Integer>();
        List<Integer> arr_list = new ArrayList<Integer>();

        for(int i = 0; i < 100; i++){
            arr.add(i+1);
        }
        for(int i = 0; i < 100; i++){
            int elem = arr.get(i);
            if((elem % 3 == 0) && (elem % 7 == 0)){
                arr_list.add(elem);
            }
        }
        System.out.println("Major elements");
        System.out.println(arr_list);
    }
}
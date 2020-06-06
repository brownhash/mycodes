import java.util.Arrays;
import java.lang.reflect.Array;

public class InfiniteArray<ArrayType> {
    private ArrayType[] array;

    public InfiniteArray(Class<ArrayType> cls) { // initiate the stack size
        @SuppressWarnings("unchecked")
        final ArrayType[] array = (ArrayType[]) Array.newInstance(cls, 0);
        this.array = array;
    }

    public void append(ArrayType element) {
        ArrayType[] temp_array = Arrays.copyOf(array, array.length + 1);

        temp_array[temp_array.length - 1] = element;
        array = temp_array;
    }

    public void change(int index, ArrayType element) {
        this.array[index] = element;
    }

    public ArrayType show(int index) {
        return array[index];
    }
}

class Runner {
    public static void main(String[] args) {
        InfiniteArray infiArr = new InfiniteArray<String>(String.class);

        for (int i=0; i<100; i++) {
            infiArr.append(Integer.toString(i));
        }

        for (int i=0; i<100; i++) {
            System.out.println(infiArr.show(i));
        }
    }
}

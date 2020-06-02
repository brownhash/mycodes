import java.lang.reflect.Array;

public class Stack<StackType> {
    private StackType[] stack;
    private int StackHead = 0;

    public Stack(Class<StackType> cls, int size) {
        @SuppressWarnings("unchecked")
        final StackType[] stack = (StackType[]) Array.newInstance(cls, size);
        this.stack = stack;
    }

    public void ShowAll() {
        for (int i=0; i<stack.length; i++) {
            System.out.println(i + ": " + stack[i]);
        }
    }

    public StackType ShowOne(int position){
        return this.stack[position];
    }

    public int Size() {
        return stack.length;
    }

    public void Put(StackType element) {
        this.stack[this.StackHead + 1] = element;
        this.StackHead += 1;
    }

    public StackType Pop() {
        StackType element = stack[0];

        for (int i=1; i<stack.length; i++) {
            stack[i-1] = stack[i];
        }

        stack[stack.length - 1] = null;
        this.StackHead -= 1;

        return element;
    }
}

class Main{
    public static void main(String[] args) {
        Stack newStack = new Stack<String>(String.class, 20);
    }
}
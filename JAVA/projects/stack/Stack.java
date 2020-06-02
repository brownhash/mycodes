import java.lang.reflect.Array;

public class Stack<StackType> {

    private StackType[] stack; // declare an empty stack of defined type
    private int StackHead = 0; // initiate the stack header at 0

    public Stack(Class<StackType> cls, int size) { // initiate the stack size
        @SuppressWarnings("unchecked")
        final StackType[] stack = (StackType[]) Array.newInstance(cls, size);
        this.stack = stack;
    }

    public void ShowAll() { // prints data on all indexes
        for (int i=0; i<stack.length; i++) {
            System.out.println(i + ": " + stack[i]);
        }
    }

    public StackType ShowOne(int position){ // returns data at a particular index
        return this.stack[position];
    }

    public int Size() { // returns capacity of stack
        return stack.length;
    }

    public void Put(StackType element) { // places provided data at the top
        this.stack[this.StackHead] = element;
        this.StackHead += 1;
    }

    public StackType Pop() { // returns top element of the stack
        this.StackHead -= 1;
        return this.stack[this.StackHead];
    }
}

class Main{
    public static void main(String[] args) {
        Stack newStack = new Stack<String>(String.class, 20); // stack declaration

        while (true) {
            System.out.println(newStack.Pop());
        }
    }
}
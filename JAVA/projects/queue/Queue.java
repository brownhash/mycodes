import java.lang.reflect.Array;

public class Queue<QueueType> {

    private QueueType[] queue; // declare an empty queue of defined type
    private int QueueTail = 0; // initiate the queue tail at 0

    public Queue(Class<QueueType> cls, int size) { // initiate the queue size
        @SuppressWarnings("unchecked")
        final QueueType[] queue = (QueueType[]) Array.newInstance(cls, size);
        this.queue = queue;
    }

    public void ShowAll() { // prints data on all indexes
        for (int i=0; i<queue.length; i++) {
            System.out.println(i + ": " + queue[i]);
        }
    }

    public QueueType ShowOne(int position){ // returns data at a particular index
        return this.queue[position];
    }

    public int Size() { // returns capacity of queue
        return queue.length;
    }

    public void Push(QueueType element) { // places provided data at the top
        this.queue[this.QueueTail] = element;
        this.QueueTail += 1;
    }

    public QueueType Pull() { // returns first element of the queue
        QueueType element = this.queue[0];

        for (int i=1; i<queue.length; i++) {
            queue[i-1] = queue[i];
            queue[i] = null;
        }
        this.QueueTail -= 1;

        return element;
    }
}

class Main{
    public static void main(String[] args) {
        Queue newQueue = new Queue(String.class, 5); // queue declaration

        newQueue.Push("1st element");
        newQueue.Push("2nd element");
        newQueue.Push("3rd element");
        newQueue.Push("4th element");
        newQueue.Push("5th element");

        newQueue.ShowAll();

        System.out.println(newQueue.Pull());
        System.out.println(newQueue.Pull());
        System.out.println(newQueue.Pull());
        System.out.println(newQueue.Pull());

        newQueue.ShowAll();

        newQueue.Push("new element");

        newQueue.Push("1st element");
        newQueue.Push("2nd element");
        newQueue.Push("3rd element");

        newQueue.ShowAll();
    }
}
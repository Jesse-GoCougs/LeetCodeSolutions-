 #include <queue>

class MyStack {
public:
    MyStack() {
        // No need to declare the queue here, it's already a member variable
    }
    
    void push(int x) {
        myqueue.push(x);
    }
    
    int pop() {
        int size = myqueue.size();
        for (int i = 0; i < size - 1; ++i) {
            int element = myqueue.front();
            myqueue.pop();
            myqueue.push(element);
        }
        int topElement = myqueue.front();
        myqueue.pop();
        return topElement;
    }
    
    int top() {
        int size = myqueue.size();
        for (int i = 0; i < size - 1; ++i) {
            int element = myqueue.front();
            myqueue.pop();
            myqueue.push(element);
        }
        int topElement = myqueue.front();
        myqueue.pop();
        myqueue.push(topElement);
        return topElement;
    }
    
    bool empty() {
        return myqueue.empty();
    }
    
private:
    std::queue<int> myqueue;
};
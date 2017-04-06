    public static int fibonacci(int n) {
        int temp;
        int first = 0;
        int second = 1;
        
        for(int i = 0; i < n; i++){
            temp = second;
            second += first;
            first = temp;
        }
        
        return first;
    }

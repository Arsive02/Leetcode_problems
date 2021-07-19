// Naive approach 

class Solution {
    private int order(int n) {
        int count = 0;
        while(n>0){
            count++;
            n = n/10;
        }
        return count;
    }
    public int addDigits(int num) {
        int d;
        while(order(num) > 1) {
            int sum = 0;
            while(num>0){
                d = num%10;
                sum += d;
                num = num/10;
            }
            num = sum;
        }
        return num;
    }
}


// O(1) solution - Popularly known as digit root problem

class Solution {
    public int addDigits(int num) {
        return 1 + (num - 1) % 9;       // Congruence formula
    }
}

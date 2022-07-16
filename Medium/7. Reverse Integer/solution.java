class Solution {
    public int reverse(int x) {
        int d,temp = 0;
        int pre = temp;
        boolean flag = false;
        if(x < 0){
            flag = true;
            x = -x;
        }
        while(x != 0){
            d = x%10;
            temp = temp*10 + d;
            if((temp - d)/10 != pre){
                return 0;
            }
            x = x/10;
            pre = temp;
        }
        x = flag? -temp: temp;
        return x;
    }
}

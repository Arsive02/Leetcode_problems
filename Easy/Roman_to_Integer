class Solution {
    public int romanToInt(String s) {
        int t = 0;
        for(int i=s.length()-1; i>=0; i--){
            switch(s.charAt(i)) {
                case 'I':
                    t += (t>=5?-1:1);
                    break;
                case 'V':
                    t += 5;
                    break;
                case 'X':
                    t += 10*(t>=50?-1:1);
                    break;
                case 'L':
                    t += 50;
                    break;
                case 'C':
                    t += 100*(t>=500?-1:1);
                    break;
                case 'D':
                    t += 500;
                    break;
                case 'M':
                    t += 1000*(t>=5000?-1:1);
                    break;
            }
        }
        return t;
    }
}

class Solution {
    public String solution(String X, String Y) {
        StringBuilder answer = new StringBuilder();
        int[] x = {0,0,0,0,0,0,0,0,0,0};
        int[] y = {0,0,0,0,0,0,0,0,0,0};
        
        // 아스키코드 0은 48
        for(int i=0; i<X.length();i++){
           x[X.charAt(i)-48] += 1;
        }

        for(int i=0; i<Y.length();i++){
           y[Y.charAt(i)-48] += 1;
        }
        
        // 역순으로 진행해서 가장 큰 수가 앞으로
        for(int i=9; i >= 0; i--){
            for(int j=0; j<Math.min(x[i],y[i]); j++){
                answer.append(i);
            }
        }
        if("".equals(answer.toString())){
           return "-1";
        }else if(answer.toString().charAt(0)==48){
           return "0";
        }else {
            return answer.toString();
        }
    }
}

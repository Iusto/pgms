class Solution {
    public int solution(String s) {
        int answer = 1;

        char[] s1 = s.toCharArray();
        for (int i = 0; i < s1.length; i++) System.out.print(s1[i] + " ");
        char x = s.charAt(0);
        int count = 1;
        for (int i = 1; i < s.length(); i++) {
            if (count == 0) {
                answer++;
                x = s.charAt(i);
            }

            if (x == s.charAt(i)) {
                count++;
            } else {
                count--;
            }
        }


        return answer;
    }
}

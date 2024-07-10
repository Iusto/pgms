import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < moves.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][moves[i]-1] != 0) {
                    stack.add(board[j][moves[i]-1]);
                    board[j][moves[i]-1] = 0;
                    if (stack.size() > 1) {
                        if (stack.get(stack.size() - 2) == stack.lastElement()) {
                            answer+=2;
                            stack.pop();
                            stack.pop();
                        }
                    }
                    break;
                }
            }
        }
        return answer;
    }
}

import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> rank = new HashMap<String, Integer>();		  
		  for (int i = 0; i < players.length; i++) rank.put(players[i], i);
		  
		  for (String player : callings) {
			  int playerRanking = rank.get(player);
			  
			  String frontplayer = players[playerRanking-1];
			  rank.replace(frontplayer, playerRanking);			  
			  rank.replace(player, playerRanking-1);
			  
			  players[playerRanking] = frontplayer;
			  players[playerRanking-1] = player;
		  }
        
        return players;
    }
}

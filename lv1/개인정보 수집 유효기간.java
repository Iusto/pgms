import java.time.*;
import java.time.format.*;
import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList();

        DateTimeFormatter formatter =  DateTimeFormatter.ofPattern("yyyy.MM.dd");
        LocalDate date = LocalDate.parse(today, formatter);

        // 찾기 쉽도록 termsMap 구성
        Map<String, Integer> termsMap = new HashMap<>();

        for(int i=0; i<terms.length; i++) {
            String[] term = terms[i].split(" ");
            termsMap.put(term[0], Integer.valueOf(term[1]));
        }

        for(int i=0; i<privacies.length; i++) {
            String[] privacy = privacies[i].split(" ");
            LocalDate privacyRegisterYmdt = LocalDate.parse(privacy[0], formatter)
                .plusMonths(termsMap.get(privacy[1])).minusDays(1);


            if (privacyRegisterYmdt.isBefore(date)) {
                answer.add(i+1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

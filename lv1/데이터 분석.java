import java.util.*;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        List<int[]> answer = new ArrayList<>();
        String[] arr = {"code", "date", "maximum", "remain"};
        List<String> columnList = Arrays.asList(arr);
        for (int i = 0; i < data.length; i++) {
            int index = columnList.indexOf(ext);
            if (data[i][index] < val_ext) answer.add(data[i]);
        }
        int sortIdx = columnList.indexOf(sort_by);
        answer.sort((a, b) -> Integer.compare(a[sortIdx], b[sortIdx]));
        return answer.stream().toArray(int[][]::new);
    }
}

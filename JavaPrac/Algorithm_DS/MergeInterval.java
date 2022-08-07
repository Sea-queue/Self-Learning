/*
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping i
ntervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

I spend the hours and did it!!!!
Runtime: 2 ms, faster than 99.75% of Java online submissions;
Memory Usage: 41.2 MB, less than 98.34% of Java online submissions;
 */
import java.util.List;
import java.util.ArrayList;

 class MergeInterval {
    public int[][] merge(int[][] intervals) {
        List<int[]> table = new ArrayList<>();
        table.add(intervals[0]);

        for (int i = 1; i < intervals.length; i += 1) {
            table.add(intervals[i]);
            for (int j = table.size() - 1; j > 0; j -= 1) {
                if (table.get(j)[1] < table.get(j - 1)[0]) {
                    int[] temp = {table.get(j - 1)[0], table.get(j - 1)[1]};
                    table.get(j - 1)[0] = table.get(j)[0];
                    table.get(j - 1)[1] = table.get(j)[1];
                    table.get(j)[0] = temp[0];
                    table.get(j)[1] = temp[1];
                }

                else if (table.get(j)[1] == table.get(j - 1)[0]) {
                    table.get(j - 1)[0] = table.get(j)[0];
                    table.remove(j);

                }

                else if (table.get(j)[0] < table.get(j - 1)[0]) {
                    table.get(j - 1)[0] = table.get(j)[0];
                    if (table.get(j)[1] > table.get(j - 1)[1]) {
                        table.get(j - 1)[1] = table.get(j)[1];
                    }
                    table.remove(j);
                }

                else if (table.get(j)[0] <= table.get(j - 1)[1]) {
                    if (table.get(j)[1] > table.get(j - 1)[1]) {
                        table.get(j - 1)[1] = table.get(j)[1];
                    }
                    table.remove(j);
                }
            }
        }

        int[][] result = new int[table.size()][2];
        for (int i = 0; i < table.size(); i += 1) {
            result[i] = table.get(i);
        }

        return result;
    }

    public static void main (String[] args) {
        MergeInterval mi = new MergeInterval();
        int[][] input1 = {
            {2, 3},
            {5, 5},
            {2, 2},
            {3, 4},
            {3, 4}
        };

        int[][] input2 = {
            {1, 3},
            {2, 6},
            {8, 10},
            {15, 18}
        };
        int[][] result = mi.merge(input2);
        for (int i  = 0; i < result.length; i += 1) {
            System.out.println(result[i][0] + " , " + result[i][1]);
        }
    }
}

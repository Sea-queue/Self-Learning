/*
    Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
    Output: [0,2,0,0,0]
    Explanation:
    The user with ID=0 performed actions at minutes 5, 2, and 5 again.
    Hence, they have a UAM of 2 (minute 5 is only counted once).
    The user with ID=1 performed actions at minutes 2 and 3.
    Hence, they have a UAM of 2.
    Since both users have a UAM of 2, answer[2] is 2,
    and the remaining answer[j] values are 0.
 */

class MapSet {
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        int[] result = new int[k];
        Map<Integer, Set<Integer>> acts = new HashMap<>();

        for (int i = 0; i < logs.length; i += 1) {
            if (acts.containsKey(logs[i][0])) {
                acts.get(logs[i][0]).add(logs[i][1]);
            }
            else {
                Set<Integer> minutes = new HashSet<>();
                minutes.add(logs[i][1]);
                acts.put(logs[i][0], minutes);
            }
        }

        for (Map.Entry<Integer, Set<Integer>> map : acts.entrySet()) {
            result[map.getValue().size() - 1] += 1;
        }

        return result;
    }
}

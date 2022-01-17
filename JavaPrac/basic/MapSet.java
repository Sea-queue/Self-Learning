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


//Iterating over Map:
 /*
  Using for loop:
  1: Using entrySet()

  public void forLoopEntrySet(Map<String, Integer> map) {
      for (Map.Entry<String, Integer> entry : map.entrySet()) {
          System.out.println(entry.getKey() + ":" + entry.getValue());
      }
  }

  2: Using keySet()

  public void forLoopKeySet(Map<String, Integer> map) {
      for (String Key : map.keySet()) {
          System.out.println(key + ":" + map.get(key));
      }
  }

  3: Using values()

  public void forLoopValues(Map<String, Integer> map) {
      for (Integer value : map.values()) {
          System.out.println(value);
      }
  }

  Using Iterator:

  1: entrySet():

  public void iteratorEntrySet(Map<String, Integer> map) {
      Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
      while (iterator.hasNext()) {
          Map.Entry(String, Integer) entry = iterator.next();
          System.out.println(entry.getKey() + ":" + entry.getValue());
      }
  }

  2: KeySet()

  public void iteratorKeySet(Map<String, Interger> map) {
      Iterator<String> iterator = map.keySet().iterator();
      while(iterator.hasNext()) {
          String key = iterator.next();
          System.out.println(key + ":" + map.get(key));
      }
  }

  3: values()

  public void iteratorValues(Map<String, Integer> map) {
      Iterator<Integer> iterator = map.values().iterator();
      while (iterator.hasNext()) {
          Integer value = iterator.next();
          System.out.println("value: " + value);
      }
  }

  Using Lambdas

  1: EntrySet

  public void lambdasEntry(Map<String, Integer> map) {
      map.forEach((k, v) -> System.out.println((k + ":" + v)));
  }


  2: keySet

  public void lambdasKeySet(Map<String, Integer> map) {
      map.keySet().forEach(k -> System.out.println((k + ":" + map.get(k))));
  }


  3: values
  public void labmdasValues(Map<String, Integer> map) {
      map.values().forEach(v -> System.out.println(("value: " + v)));
  }

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

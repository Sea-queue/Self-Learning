import java.util.Map;
import java.util.HashMap;

public class Test {
    public void lambdasKeySet(Map<String, Integer> map) {
        map.keySet().forEach(k -> System.out.println((k + ":" + map.get(k))));
    }

    public static void main(String[] args) {
        Test t = new Test();
        Map<String, Integer> map = new HashMap<>();
        map.put("hey", 3);
        map.put("hello", 5);
        map.put("sensational", 11);
        t.lambdasKeySet(map);
        System.out.println("abc".substring(0,1));
    }
}

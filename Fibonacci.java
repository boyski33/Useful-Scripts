import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Fibonacci {

  private static List<Integer> fibonacciSequence(Integer length) {
    List<Integer> result = new ArrayList<>(Arrays.asList(0, 1));

    for (int i = 2; i < length; i++) {
      result.add(result.get(i - 1) + result.get(i - 2));
    }

    return result;
  }

  public static void main(String[] args) {
    System.out.println(fibonacciSequence(30));
  }
}

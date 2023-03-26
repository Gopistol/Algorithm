import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(input);
        double amount = 0;
        Double[] drinks = new Double[n];
        input = br.readLine();
        StringTokenizer st = new StringTokenizer(input, " ");
        for (int i = 0; i < n; i++) {
            drinks[i] = Double.parseDouble(st.nextToken());
        }
        Arrays.sort(drinks, Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                amount += drinks[i];
            } else {
                amount += (drinks[i] / 2);
            }
        }
        System.out.println(amount);
    }
}

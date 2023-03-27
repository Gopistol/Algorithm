import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int n = Integer.parseInt(input); // 문제 수
        input = br.readLine();
        StringTokenizer st = new StringTokenizer(input,"B");
        int min = st.countTokens(); // R을 제외한 문제 수
        StringTokenizer st_2 = new StringTokenizer(input, "R");
        int min_2 = st_2.countTokens();
        if (min < min_2) {
            System.out.println(min + 1);
        } else {
            System.out.println(min_2 + 1);
        }
    }
}

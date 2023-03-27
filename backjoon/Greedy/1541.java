import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int result = 0;
        boolean first = true;
        StringTokenizer st = new StringTokenizer(input, "-");
        while(st.hasMoreTokens()) {
            int sum = 0; // - 와 - 사이의 수들의 합
            StringTokenizer st_2 = new StringTokenizer(st.nextToken(), "+");
            while(st_2.hasMoreTokens()) {
                // 0이 아닌 수를 만날 때까지 앞 자리의 0 지우기
                String token = st_2.nextToken();
                String newToken = "";
                boolean check = false;
                for (int i = 0; i < token.length(); i++) {
                    if (token.charAt(i) != '0') {
                        check = true;
                    }
                    if (check) {
                        newToken += token.charAt(i);
                    }
                }
                sum += Integer.parseInt(newToken);
            }
            if (first) {
                result += sum;
                first = false;
            } else {
                result -= sum;
            }
        }
        System.out.println(result);
    }
}

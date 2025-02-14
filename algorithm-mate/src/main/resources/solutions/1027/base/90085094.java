import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] buildings = new long[N];  // 정밀도를 위해 long으로 변경
        for(int i = 0; i < N; i++) {
            buildings[i] = Long.parseLong(st.nextToken());
        }

        int maxCount = 0;

        // 각 건물마다 보이는 건물 수 계산
        for(int i = 0; i < N; i++) {
            int count = 0;

            // 왼쪽 방향 검사
            if(i > 0) {
                double prevSlope = getSlope(i, buildings[i], i-1, buildings[i-1]);
                count++;

                for(int j = i-2; j >= 0; j--) {
                    double currentSlope = getSlope(i, buildings[i], j, buildings[j]);
                    if(currentSlope < prevSlope) {
                        count++;
                        prevSlope = currentSlope;
                    }
                }
            }

            // 오른쪽 방향 검사
            if(i < N-1) {
                double prevSlope = getSlope(i, buildings[i], i+1, buildings[i+1]);
                count++;

                for(int j = i+2; j < N; j++) {
                    double currentSlope = getSlope(i, buildings[i], j, buildings[j]);
                    if(currentSlope > prevSlope) {
                        count++;
                        prevSlope = currentSlope;
                    }
                }
            }

            maxCount = Math.max(maxCount, count);
        }

        System.out.println(maxCount);
    }

    private static double getSlope(int x1, long y1, int x2, long y2) {
        return (double)(y2 - y1) / (x2 - x1);
    }
}
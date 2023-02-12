import java.io.*;
import java.util.*;

public class Bit {

    static class FastScanner {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer("");
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
        int[] readArray(int n) {
            int[] a=new int[n];
            for (int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }

    static <T> List<List<T>> chopped(List<T> list, final int L) {
        List<List<T>> parts = new ArrayList<List<T>>();
        final int N = list.size();
        for (int i = 0; i < N; i += L) {
            parts.add(new ArrayList<T>(
                    list.subList(i, Math.min(N, i + L)))
            );
        }
        return parts;
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);

        int n = fs.nextInt();
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            String string = fs.next();
            if (string.contains("+")) {
                cnt++;
            } else if (string.contains("-")) {
                cnt--;
            }
        } out.println(cnt);
        out.close();
    }
}
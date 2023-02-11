import java.io.*;
import java.util.*;

public class BoyOrGirl {

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
        // buat set
        Set<String> hs = new HashSet<String>();
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);

        String str = fs.next();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            String str_c = Character.toString(c);
            hs.add(str_c);
        }

        if (hs.size() % 2 == 0) {
            out.println("CHAT WITH HER!");
        } else {
            out.println("IGNORE HIM!");
        }

        out.close();
    }
}
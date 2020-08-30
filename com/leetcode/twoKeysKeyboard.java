class twoKeysKeyboard {

    private static int getFirstFactor(int n) {
        if (n <= 1)
            return n;
        if (n <= 3)
            return n;
        if (n % 2 == 0)
            return n / 2;
        if (n % 3 == 0)
            return n / 3;

        for (int i = 5; i * i <= n; i = i + 6) {
            if (n % i == 0)
                return n / i;
            if (n % (i + 2) == 0)
                return n / (i + 2);
        }
        return n;
    }

    private static int minStepsdp(int n) {
        int[] res = new int[n + 1];
        res[1] = 0;
        for (int i = 2; i <= n; i++) {
            if (getFirstFactor(i) == i) {
                res[i] = i;
            } else {
                res[i] = res[getFirstFactor(i)] + i / getFirstFactor(i);
            }
        }
        return res[n];
    }

    private static int minStepsrecur(int n) {
        if (n == 1)
            return 0;
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return i + minSteps(n / i);
        return n;
    }

    private static int minSteps(int n) {
        int ans = 0, d = 2;
        while (n > 1) {
            while (n % d == 0) {
                ans += d;
                n /= d;
            }
            d++;
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(minSteps(25));
    }
}
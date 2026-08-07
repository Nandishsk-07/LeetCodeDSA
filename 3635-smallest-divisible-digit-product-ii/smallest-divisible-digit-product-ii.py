class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        a = b = c = d = 0
        while temp_t % 2 == 0:
            a += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            b += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            c += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            d += 1
            temp_t //= 7
        if temp_t > 1:
            return "-1"
        MAX_A = 60
        MAX_B = 60
        dp = [[float('inf')] * (MAX_B + 1) for _ in range(MAX_A + 1)]
        dp[0][0] = 0
        transitions = [(1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2)]
        for i in range(MAX_A + 1):
            for j in range(MAX_B + 1):
                if dp[i][j] != float('inf'):
                    for da, db in transitions:
                        ni = min(MAX_A, i + da)
                        nj = min(MAX_B, j + db)
                        if dp[i][j] + 1 < dp[ni][nj]:
                            dp[ni][nj] = dp[i][j] + 1
        for i in range(MAX_A, -1, -1):
            for j in range(MAX_B, -1, -1):
                if i < MAX_A:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j])
                if j < MAX_B:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1])
        def min_digits(rem_a, rem_b, rem_c, rem_d):
            count_5 = max(0, rem_c)
            count_7 = max(0, rem_d)
            cnt_a = min(MAX_A, max(0, rem_a))
            cnt_b = min(MAX_B, max(0, rem_b))
            return count_5 + count_7 + dp[cnt_a][cnt_b]
        def get_factors(ch):
            d_val = int(ch)
            if d_val == 0:
                return (0, 0, 0, 0)
            twos = threes = fives = sevens = 0
            if d_val in (2, 4, 6, 8):
                if d_val == 2: twos = 1
                elif d_val == 4: twos = 2
                elif d_val == 6: twos = 1
                elif d_val == 8: twos = 3
            if d_val in (3, 6, 9):
                if d_val == 3: threes = 1
                elif d_val == 6: threes = 1
                elif d_val == 9: threes = 2
            if d_val == 5: fives = 1
            if d_val == 7: sevens = 1
            return (twos, threes, fives, sevens)
        N = len(num)
        pref_a = [0] * (N + 1)
        pref_b = [0] * (N + 1)
        pref_c = [0] * (N + 1)
        pref_d = [0] * (N + 1)
        first_zero = N
        for idx, ch in enumerate(num):
            if ch == '0' and first_zero == N:
                first_zero = idx
            da, db, dc, dd = get_factors(ch)
            pref_a[idx + 1] = pref_a[idx] + da
            pref_b[idx + 1] = pref_b[idx] + db
            pref_c[idx + 1] = pref_c[idx] + dc
            pref_d[idx + 1] = pref_d[idx] + dd
        if first_zero == N:
            if min_digits(a - pref_a[N], b - pref_b[N], c - pref_c[N], d - pref_d[N]) == 0:
                return num
        for L in range(N - 1, -1, -1):
            if first_zero < L:
                continue
            cur_a, cur_b, cur_c, cur_d = pref_a[L], pref_b[L], pref_c[L], pref_d[L]
            start_digit = int(num[L]) + 1
            for D in range(start_digit, 10):
                da, db, dc, dd = get_factors(str(D))
                rem_a = a - cur_a - da
                rem_b = b - cur_b - db
                rem_c = c - cur_c - dc
                rem_d = d - cur_d - dd
                if min_digits(rem_a, rem_b, rem_c, rem_d) <= N - 1 - L:
                    res = list(num[:L]) + [str(D)]
                    rem_a_cur, rem_b_cur, rem_c_cur, rem_d_cur = rem_a, rem_b, rem_c, rem_d
                    for pos in range(L + 1, N):
                        positions_left = N - 1 - pos
                        for d_next in range(1, 10):
                            nda, ndb, ndc, ndd = get_factors(str(d_next))
                            ra, rb, rc, rd = rem_a_cur - nda, rem_b_cur - ndb, rem_c_cur - ndc, rem_d_cur - ndd
                            if min_digits(ra, rb, rc, rd) <= positions_left:
                                res.append(str(d_next))
                                rem_a_cur, rem_b_cur, rem_c_cur, rem_d_cur = ra, rb, rc, rd
                                break
                    return "".join(res)
        M = min_digits(a, b, c, d)
        L_new = max(N + 1, M)
        res = []
        rem_a_cur, rem_b_cur, rem_c_cur, rem_d_cur = a, b, c, d
        for pos in range(L_new):
            positions_left = L_new - 1 - pos
            for d_next in range(1, 10):
                nda, ndb, ndc, ndd = get_factors(str(d_next))
                ra, rb, rc, rd = rem_a_cur - nda, rem_b_cur - ndb, rem_c_cur - ndc, rem_d_cur - ndd
                if min_digits(ra, rb, rc, rd) <= positions_left:
                    res.append(str(d_next))
                    rem_a_cur, rem_b_cur, rem_c_cur, rem_d_cur = ra, rb, rc, rd
                    break
        return "".join(res)
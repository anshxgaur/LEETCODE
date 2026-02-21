from typing import List
import bisect

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        # --- Segment Tree helpers (defined locally) ---
        def build_segment_tree(xs):
            n = len(xs) - 1
            count = [0] * (4 * n)
            covered = [0] * (4 * n)

            def update(idx, l, r, ql, qr, val):
                if qr <= l or r <= ql:
                    return
                if ql <= l and r <= qr:
                    count[idx] += val
                else:
                    mid = (l + r) // 2
                    update(idx * 2, l, mid, ql, qr, val)
                    update(idx * 2 + 1, mid, r, ql, qr, val)

                if count[idx] > 0:
                    covered[idx] = xs[r] - xs[l]
                else:
                    if l + 1 == r:
                        covered[idx] = 0
                    else:
                        covered[idx] = covered[idx * 2] + covered[idx * 2 + 1]

            return update, covered, n

        # --- Build sweep events ---
        events = []
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)

        # --- First sweep: compute total area ---
        update, covered, n = build_segment_tree(xs)
        prev_y = events[0][0]
        total_area = 0

        for y, delta, xl, xr in events:
            total_area += covered[1] * (y - prev_y)

            l = bisect.bisect_left(xs, xl)
            r = bisect.bisect_left(xs, xr)
            update(1, 0, n, l, r, delta)

            prev_y = y

        half = total_area / 2

        # --- Second sweep: find the separating y ---
        update, covered, n = build_segment_tree(xs)
        prev_y = events[0][0]
        curr_area = 0

        for y, delta, xl, xr in events:
            width = covered[1]
            segment_area = width * (y - prev_y)

            if curr_area + segment_area >= half:
                if width == 0:
                    return float(y)
                return prev_y + (half - curr_area) / width

            curr_area += segment_area

            l = bisect.bisect_left(xs, xl)
            r = bisect.bisect_left(xs, xr)
            update(1, 0, n, l, r, delta)

            prev_y = y

        return float(prev_y)

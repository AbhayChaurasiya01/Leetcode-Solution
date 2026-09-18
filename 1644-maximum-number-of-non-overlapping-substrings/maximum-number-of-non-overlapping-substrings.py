class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Step 1: Record the first and last occurrence of each character
        first = {c: s.index(c) for c in set(s)}
        last = {c: s.rindex(c) for c in set(s)}

        # Step 2: Expand each character's range to include all characters within it
        for c in first:
            start, end = first[c], last[c]
            i = start
            while i <= end:
                start = min(start, first[s[i]])
                end = max(end, last[s[i]])
                i += 1
            first[c], last[c] = start, end

        # Step 3: Collect valid intervals
        intervals = []
        for c in first:
            start, end = first[c], last[c]
            # A valid substring must start exactly at the first occurrence of c
            if start == s.index(c):
                intervals.append((start, end))

        # Step 4: Sort by end position and greedily pick non-overlapping intervals
        intervals.sort(key=lambda x: x[1])
        result = []
        last_end = -1

        for start, end in intervals:
            if start > last_end:
                result.append(s[start:end + 1])
                last_end = end

        return result
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, there's no window to find
        if t == "":
            return ""

        # Create frequency maps for characters in t and current window
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)  # Count occurrences in t

        have, need = 0, len(countT)  # have: how many chars we've satisfied; need: how many to satisfy
        res, resLen = [-1, -1], float("infinity")  # res stores the best window, resLen is the window length
        l = 0  # left pointer of sliding window

        # Expand the right end of the window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)  # Add current char to window count

            # If current char meets target count, increment `have`
            if c in countT and window[c] == countT[c]:
                have += 1

            # When we have all needed characters
            while have == need:
                # Update result if the current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Shrink the window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1  # We no longer satisfy this char's requirement
                l += 1  # Move left pointer

        l, r = res
        # Return the smallest valid window substring, or empty string if no valid window
        return s[l : r + 1] if resLen != float("infinity") else ""
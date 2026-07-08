class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + "#" + s)

        return "".join(encoded)

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1  # Move past '#'

            res.append(s[j:j + length])

            i = j + length

        return res
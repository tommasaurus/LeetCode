class Codec:
    # This solution works for any set of characters, not just ASCII 256
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        hashed = ""
        for each in strs:
            hashed += f"{len(each)}#{each}"

        return hashed


    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        decoded = []
        i = 0
        while i < len(s):
            # Find the next delimiter (which indicates the length)
            j = s.find('#', i)
            length = int(s[i:j])  # Length of the next string
            i = j + 1  # Move past the '#'
            decoded.append(s[i:i+length])  # Extract the string
            i += length  # Move to the next part
        return decoded
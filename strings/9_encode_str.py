'''
659 · Encode and Decode Strings

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

'''


from typing import List


class Solution:

    def encode(self, strs: List[str]):
        encoded = ""
        header = "%%{0}%".format(len(strs))
        encoded += header
        for s in strs:
            encoded += "%{0}%{1}".format(len(s), s)
        return encoded
    
    def decode(self, s:str):

        if s[0:2] != "%%":
           return "" 
        
        i = 2
        while s[i] != '%':
            i += 1

        items = int(s[2:i])
        i+=2 #header terminator '%%'
        tokens = self.tokenize(s[i:])
        output = [] 
        t = 0
        while t < len(tokens):
            item_len = int(tokens[t])
            item = tokens[t+1]
            if item != '': 
                output.append(item)
                t = t + 2
            else:
                spl = ""
                for _ in range(item_len):
                    spl += '%'
                output.append(spl)
                t = t + item_len + 2
            
        return output
            
    def tokenize(self, s):
        if not s:
            return ""
        tokens = []
        token = ""

        for c in s:
            if c == '%':
                tokens.append(token)
                token = ""
            else:
                token += c
        tokens.append(token)
        return tokens
        
                
s = Solution()
input = "%%3%%5%hello%2%%%%2%jo"
#"%%3%%5%hello%2%%%%2%jo"
tokens = s.decode(input)
print(tokens)
'''
input = ['hello', '%%', 'jo']
output = s.encode(input)
print(output)
'''
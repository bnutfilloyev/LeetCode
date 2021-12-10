class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = address.split('.')
        ans = ''
        for i in arr:
            ans += f"{i}[.]"
        return ans[:-3]
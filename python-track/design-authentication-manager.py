class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live=timeToLive
        self.authentication_dict=defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.authentication_dict[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.authentication_dict:
            time=self.authentication_dict[tokenId]
            if currentTime - time <self.time_to_live:
                self.authentication_dict[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for key in self.authentication_dict:
            if currentTime - self.authentication_dict[key] <self.time_to_live:
                count+=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
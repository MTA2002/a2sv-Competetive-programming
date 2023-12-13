class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdomains_dict=defaultdict(int)
    
        for cpdomain in cpdomains:
            value,domain=cpdomain.split()

            for i in range(len(domain)-1,-1,-1):
                if domain[i]=='.':
                    key=domain[i+1:]
                    cpdomains_dict[key] += int(value)
            cpdomains_dict[domain] += int(value)

        answer=[]

        for key in cpdomains_dict:
            answer.append(str(cpdomains_dict[key])+" "+key)

        return answer
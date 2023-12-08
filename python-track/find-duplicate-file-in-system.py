class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths_dictionary=defaultdict(list)

        for path in paths:
            path_to_array=path.split()
            #we are beginning from one since we don't want the root to be iterated
            for index in range(1,len(path_to_array)):
                file_array=path_to_array[index].split('(')
                paths_dictionary[file_array[1]].append(path_to_array[0]+"/"+file_array[0])

        ans=[paths_dictionary[key] for key in paths_dictionary if len(paths_dictionary[key])>1]

        return ans


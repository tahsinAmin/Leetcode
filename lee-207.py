class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)

        print(pre_map)

        # visit_set = All courses along the curr DFS path
        visit_set = set()

        def dfs(crs):
            if crs in visit_set:
                return False
            if not pre_map[crs]:
                return True

            visit_set.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            visit_set.remove(crs)
            pre_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
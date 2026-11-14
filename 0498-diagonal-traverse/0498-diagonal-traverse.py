class Solution(object):
    def findDiagonalOrder(self, mat):
        m,n = len(mat),len(mat[0]) #m rows n columns
        result = []
        for s in range(m+n-1):
            if s%2==0:
                r = min(s,m-1) # rows=r
                c = s-r  #column starting point
                while r>=0 and c<n:
                    result.append(mat[r][c])
                    r-=1
                    c+=1
            else:
                c = min(s,n-1) # column=c
                r = s-c #row starting point
                while c>=0 and r<m:
                    result.append(mat[r][c])
                    r+=1
                    c-=1
        return result

        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
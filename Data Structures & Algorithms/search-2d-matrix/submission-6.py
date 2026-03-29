class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch2D(self,matrix:List[List[int]],target:int,l:int,r:int)->bool:
            while l<=r:
                mean=(l+r)//2
                i,j=mean//n,mean%n
                if matrix[i][j]<target:
                    l=mean+1
                elif matrix[i][j]>target:
                    r=mean-1
                else:
                    return True
            return False
        m=len(matrix)
        n= len(matrix[0])
        q=0
        while 2**q<n*m and matrix[(2**q)//n][(2**q)%n]<target:
            q+=1
        if 2**q>=n*m:
            return binarysearch2D(self,matrix,target,2**q//2,n*m-1)
        else:
            return binarysearch2D(self,matrix,target,2**q//2,2**q)

        
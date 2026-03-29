class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        liste=[]
        for i in nums:
            if(i not in dic):
                dic[i]=1
            else:
                dic[i]+=1
        for (i, num) in dic.items():
            liste.append([num,i])
        liste.sort()
        liste1=[]    
        for i in range (k):
            liste1.append(liste[len(liste)-i-1][1])
               
        return liste1
                
            
        
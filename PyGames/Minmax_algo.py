import math


scores = [3,5,2,9,12,5,23,16]
treeDepth = math.log(len(scores),2)



def minmax(currDepth, nodeIndex, maxTurn, scores, targertDepth):
    #print(scores)
    if(currDepth == targertDepth):
        return scores[nodeIndex]

    if(maxTurn):
        return max(minmax(currDepth+1, nodeIndex*2, False, scores, targertDepth), 
            minmax(currDepth+1, nodeIndex*2+1, False, scores, targertDepth))
    else:
        return min(minmax(currDepth+1, nodeIndex*2, True, scores, targertDepth), 
            minmax(currDepth+1, nodeIndex*2+1, True, scores,targertDepth))
        

print(minmax(0,0,True,scores,treeDepth))

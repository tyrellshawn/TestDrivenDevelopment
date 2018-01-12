def balanced(s):
    '''
    
    :param s: A string containing brackets 
    :return: If the total '(' is equal to ')'
    '''
    pass

def isbuildable(fg,boms):
    '''
    
    :param fg: Finished Goods 
    :param boms: Bill of Materials
    :return:  Return whether or not the list is cyclical
    '''
    stack_visited = []
    for i in range(len(boms)):
        if boms[i][1] in stack_visited:
            return False
        else:
            stack_visited.append(boms[i][0])
    return True
print isbuildable('A',[])
print isbuildable('A',[('A','B'),('B','C')])
print isbuildable('A',[('A','B'),('B','C'),('C','A')])
print isbuildable('A',[('A','B'),('B','C'),('C','D'),('B','E'),('D','B')])
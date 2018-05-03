
"""
求婚者与稳定婚姻问题
David Gale and Lloyd Shapley 1962
...
1.每个未婚男士都必须向他喜欢的但是尚未求过婚的女士求婚
2.每位女士都会（暂时）与自己喜欢的追求者订婚，并拒绝其他求婚
"""

import sys


class Person(object):
    def __init__(self, name, priorities):
        self.name = name
        self.priorities = priorities
        self.parter = parter
        
    def __str__(self):
        return "Name is " + self.name + "\n" + \
               "Parter is currently " + str(self.parter) + "\n" + \
               "Priority list is " + str(self.priorities)
               
               
class Man(Person):
    def __init__(self, name, priorities):
        Person.__init__(self, name, priorities)
        self.proposal_index = 0
        
    def next_proposal(self):
        goal = self.priorities[self.proposal_index]
        self.proposal_index += 1
        return goal
        
    def __str__(self):
        return Person.__str__(self) + '\n' + \
               'next proposal would be to ' + self.priorities[self.proposal_index]
               
               
class Woman(Person):
    def __init__(self, name, priorities):
        Person.__init__(self, name, priorities)
        self.ranking = {}
        for rank in range(len(priorities)):
            self.ranking[priorities[rank]] = rank
            
    def evaluate_proposal(self, suiter):
        return self.parter == None or self.ranking[suitor] < self.ranking[self.parter]
        
        
        
def parse_file(filename):
    people = []
    f = file(filename)
    for line in f:
        pieces = line.split(":")
        name = pieces[0].strip()
        if name:
            priorities = pieces[1].strip().split(",")
            for i in range(len(priorities)):
                priorities[i] = priorities[i].strip()
                
                people.append((name, priorities))
                
    f.close()
    return people
    
    
def print_pairings(men):
    for man in men.values():
    print(man.name, ' is paired with ', str(man.parter))
    
    

if __name__ == "__main__":
    pass
          
    

    
  


"""
求婚者与稳定婚姻问题
David Gale and Lloyd Shapley 1962
...
1.每个未婚男士都必须向他喜欢的但是尚未求过婚的女士求婚
2.每位女士都会（暂时）与自己喜欢的追求者订婚，并拒绝其他求婚

有n位男士n位女士，每位男士对所有女士按照他喜欢的程度进行排名，
同时，每位女士也对所有男士有一个喜爱程度排名，无并列。 
比如我们现在有4位男士：m1，m2，m3，m4，和四位女士w1，w2，w3，w4（m的意思就是man男士，w的意思就是woman女士）。
第一位男士对所有女士的喜爱排名为：’w3’,’w2’,’w1’,’w4’，即他最喜欢的是第三位女士w3，接着是第二位，第一位，
最后是第四位女士w4。 
"""

import sys


class Person(object):
    def __init__(self, name, priorities):
        self.name = name
        self.priorities = priorities
        self.partner = None
        
    def __str__(self):
        return "Name is " + self.name + "\n" + \
               "partner is currently " + str(self.partner) + "\n" + \
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
        return self.partner == None or self.ranking[suiter] < self.ranking[self.partner]
        
        
        
def parse_file(filename):
    people = []
    with open(filename, 'r') as f:
        for line in f:
            pieces = line.split(":")
            name = pieces[0].strip()
            if name:
                priorities = pieces[1].strip().split(",")
                for i in range(len(priorities)):
                    priorities[i] = priorities[i].strip()
                    
                people.append((name, priorities))
                
    return people
    
    
def print_pairings(men):
    for man in men.values():
        print(man.name, ' is paired with ', str(man.partner))
    
    

if __name__ == "__main__":
    pass
    verbose = len(sys.argv)>3
    
    # initialize dictionary of men
    menlist = parse_file(sys.argv[1])
    men = dict()
    for person in menlist:
        men[person[0]] = Man(person[0],person[1])
    unwedMen = list(men.keys())
    
    # initialize dictionary of women
    womenlist = parse_file(sys.argv[2])
    women = dict()
    for person in womenlist:
        women[person[0]] = Woman(person[0], person[1])


    ############################### the real algorithm ##################################
    while unwedMen:
        m = men[unwedMen[0]]             # pick arbitrary unwed man
        w = women[m.next_proposal()]      # identify highest-rank woman to which
                                         #    m has not yet proposed
        if verbose:  
            print(m.name, 'proposes to', w.name)

        if w.evaluate_proposal(m.name):
            if verbose: 
                print('  ', w.name, 'accepts the proposal')
            
            if w.partner:
                # previous partner is getting dumped
                mOld = men[w.partner]
                mOld.partner = None
                unwedMen.append(mOld.name)

            unwedMen.remove(m.name)
            w.partner = m.name
            m.partner = w.name
        else:
            if verbose: 
                print('  ', w.name, 'rejects the proposal')

        if verbose:
            print("Tentative Pairings are as follows:")
            print_pairings(men)
            print()
    #####################################################################################



    # we should be done
    print("Final Pairings are as follows:")
    print_pairings(men)
           

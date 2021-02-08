#!/usr/bin/env python
# coding: utf-8

# In[16]:


print(u"\u25A0"*70)

print("\nData Structures and Algorithm\nSemester III\nProject Title:\t\tSKIP LIST\n")

print(u"\u25A0"*70)

print("\nGroup Member:\nMuhammad Murtaza\t19B-105-SE(B)")

import random

# A Node class to create a node with a given value

class SkipNode:
    def __init__(self,val, lev):
        self.val = val
        self.next = [None]*(lev+1)

# A Skip List class with all the Functions.

class SkipList:
    def __init__(self):
        self.max_lvl = 99
        self.head = SkipNode(-99,self.max_lvl)
        self.lev = 0

    #RandomLevel Function creates Random Levels
    #using random number and a given probab
    
    def __RandomLevel(self):
        lev = 0
        probab = 1
        while random.uniform(0,2) >= probab:
            lev += 1
        return lev


    # The Insert function inserts a node with a given value
    
    def Insert(self,val):
        update = self.__Update(val)
        head = self.head
        head = head.next[0]
        if head == None or head.val != val:
            random_lev = self.__RandomLevel() 
            if random_lev > self.lev: 
                for z in range(self.lev+1, random_lev+1): 
                    update[z] = self.head
                self.lev = random_lev 
            node = SkipNode(val, random_lev)
            for z in range(random_lev+1): 
                node.next[z] = update[z].next[z] 
                update[z].next[z] = node
                
    def __Update(self,val):
        update = [None]*(self.max_lvl+1)
        head = self.head
        for x in reversed(range(len(update))):
            while head.next[x] and head.next[x].val < val:
                head = head.next[x]
            update[x] = head
        return update

    # The Delete function deletes a node with the given value
    
    def Delete(self,val):
        update = [None]*(self.max_lvl+1)
        head = self.head
        for x in reversed(range(len(update))):
            while head.next[x] and head.next[x].val < val:
                head = head.next[x]
            update[x] = head
        head = head.next[0]
        if head != None or head.val == val:
            for z in range(self.lev+1):
                if update[z].next[z] != head:
                    break
                update[z].next[z] = head.next[z]

            while(self.lev>0 and self.head.next[self.lev] == None):
                self.lev -= 1

    # The Search function searches the node with the given value in the list.
    # It returns True if the node is present in the Skip List.
    # It returns False if the node is not in the List.
    
    def Search(self,val):
        update = self.__Update(val)
        head = self.head
        for z in reversed(range(len(update))):
            while head.next[z] and head.next[z].val < val:
                head = head.next[z]
        head = head.next[0]
        if head and head.val == val:
            return True
        return False

    # PrintList Funciton is used to print the Skip List in a sorted way with random levels.

    def PrintList(self):
        print((u"\u25A0")*30+" SKIP LIST " + (u"\u25A0")*30)
        for lev in range(self.lev+1):
            print("Level {}: ".format(lev), end = " ")
            node = self.head.next[lev]
            while node != None:
                print(node.val,end=" ")
                node = node.next[lev]
            print("")


# In[18]:


if __name__ == "__main__":
    
    sklst = SkipList()
    sklst.Insert(3)
    sklst.Insert(6)
    sklst.Insert(8)
    sklst.Insert(9)
    sklst.Insert(2)
    sklst.Insert(4)
    sklst.Insert(5)
    sklst.PrintList()
    print(sklst.Search(4))
    sklst.Delete(4)
    sklst.PrintList()
    print(sklst.Search(4))


# In[ ]:






# coding: utf-8

# In[1]:


import numpy as np 


# In[120]:


class multi_arm_bandit:
    def __init__(self):
        #self.arm_value=np.random.random(10)*0.5    # probalibality of arm
        self.arm_value=[0.05,0.06,0.1,0.5,0.1,0.01,0.1,0.02,0.01,0.1]
        self.reward=np.zeros(10)                   # record the reward 
        self.pull_count=np.zeros(10)               # record the count of arm been pulled 
    def actions(self):
        eplison=0.1
        ran_ep=np.random.random(1)
        if eplison>ran_ep:
            self.arm=np.random.randint(10)
        else:
            self.arm=np.argmax(self.reward)
        return self.arm
    def get_reward(self):
        return np.random.binomial(1,self.arm_value[arm],1)
        
    def update_arm(self,arm,reward):
        #self.reward[arm]=(self.reward[arm]*self.pull_count[arm]+1)/(sefl.pull_count[arm]+1)
        self.pull_count[arm]+=1
        self.reward[arm]=reward/self.pull_count[arm]+self.reward[arm]*(self.pull_count[arm]-1)/self.pull_count[arm]


# In[121]:


les_vegas=multi_arm_bandit();
for i in range(1000):
    arm=les_vegas.actions()
    reward=les_vegas.get_reward()
    les_vegas.update_arm(arm,reward)
    


# In[123]:


les_vegas.pull_count


# In[124]:


les_vegas.reward


# In[125]:


les_vegas.arm_value


# In[ ]:





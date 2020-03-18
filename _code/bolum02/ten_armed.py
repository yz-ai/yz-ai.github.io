
# coding: utf-8

# #DLTR RL Çalışma Grubu
# #Derin Pekiştirmeli Öğrenmede Çok Kollu Haydutlar problemi

# # Yüklemeler

# In[1]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')


# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# #Ana Kod

# In[3]:


class bandit:
    def __init__(self, eps=0, step_size=0., initial=0, variance=1):
        self.epsilon = eps
        self.step_size = step_size
        self.k_arm = 5
        self.variance = variance

        self.q_true = np.asarray([-0.25, 2, 1, -1.5, 3])
        self.q_estimates = np.zeros(self.k_arm) + initial

        self.actions_taken = np.zeros(self.k_arm)

    def action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.k_arm)

        return np.argmax(self.q_estimates)

    def step(self):
        idx = self.action()

        self.actions_taken[idx] += 1

        reward = self.q_true[idx] + np.random.randn() * self.variance

        if self.step_size == 0:
            self.q_estimates[idx] = self.q_estimates[idx] + (1.0 / self.actions_taken[idx]) * (reward - self.q_estimates[idx])
        else:
            self.q_estimates[idx] = self.q_estimates[idx] + self.step_size * (reward - self.q_estimates[idx])

        return reward

    def change_q_true(self):
        self.q_true = np.asarray([1, -0.5, -2, 2, 0.25])

    def take_steps(self, count):
        for _ in np.arange(count):
            self.step()

        self.showdown()

    def plot(self):
        plt.violinplot(positions=np.arange(self.k_arm), dataset=self.q_true + np.random.randn(100,self.k_arm) * self.variance)
        plt.plot(self.q_estimates, color='red', marker='o', linestyle='', markersize=5)
        plt.show()

    def dump(self):
        for i in np.arange(self.k_arm):
            print('Arm #%u: %u times.' % (i, self.actions_taken[i]))

        print('Best Arm: #%u.' % (np.argmax(self.q_true)))

    def showdown(self):
        self.dump()
        self.plot()


# # Greedy Policy 

# In[4]:


bnd=bandit() ## Bu satır her defa çalıştırıldığında sıfırlama yapar.


# Hiç denenmemiş hali.

# In[5]:


bnd.take_steps(0) ## Sıfır durumlarını görmek için.


# In[6]:


bnd.take_steps(1) ## Her çalıştırıldığında 1 adım yapar.


# In[7]:


bnd.take_steps(4) ## Her çalıştırıldığında 4 adım yapar.


# In[8]:


bnd.take_steps(1000) ## Her çalıştırıldığında 1000 adım yapar.


# In[9]:


bnd.take_steps(10000) ## Her çalıştırıldığında 10000 adım yapar.


# #  *Epsilon Greedy Policy*

# In[10]:


bnd=bandit(eps=0.1)  ## Bu satır her defa çalıştırıldığında sıfırlama yapar.


# In[11]:


bnd.take_steps(0)  ## Sıfır durumlarını görmek için.


# In[12]:


bnd.take_steps(1)  ## Her çalıştırıldığında 1 adım yapar.


# In[13]:


bnd.take_steps(4) ## Her çalıştırıldığında 4 adım yapar.


# In[14]:


bnd.take_steps(1000)  ## Her çalıştırıldığında 1000 adım yapar.


# In[15]:


bnd.take_steps(10000)  ## Her çalıştırıldığında 10000 adım yapar.


# In[16]:


bnd.change_q_true() ##Lütfen bu kodu çalıştırın denildiğinde çalıştırınız. Diğer durumlarda çalıştırmayınız. (Durağan Olmayan Durumlar)


# In[17]:


bnd.take_steps(0)


# In[18]:


bnd.take_steps(1)


# In[19]:


bnd.take_steps(4)


# In[20]:


bnd.take_steps(1000)


# In[21]:


bnd.take_steps(10000)


# # Epsilon Greedy StepSize

# In[22]:


bnd=bandit(eps=0.1,step_size=0.1) ## Bu satır her defa çalıştırıldığında sıfırlama yapar.


# In[23]:


bnd.take_steps(0)


# In[24]:


bnd.take_steps(1)


# In[25]:


bnd.take_steps(4)


# In[26]:


bnd.take_steps(1000)


# In[27]:


bnd.take_steps(10000)


# In[28]:


bnd.change_q_true() ##Lütfen bu kodu çalıştırın denildiğinde çalıştırınız. Diğer durumlarda çalıştırmayınız.


# In[29]:


bnd.take_steps(0)


# In[30]:


bnd.take_steps(1)


# In[31]:


bnd.take_steps(4)


# In[32]:


bnd.take_steps(1000)


# In[33]:


bnd.take_steps(10000)


# # Optimistic Initial Values - İyimser Başlanğıç Değerleri

# In[34]:


bnd=bandit(initial=5) ## Bu satır her defa çalıştırıldığında sıfırlama yapar.


# In[35]:


bnd.take_steps(0)


# In[36]:


bnd.take_steps(1)


# In[37]:


bnd.take_steps(4)


# In[38]:


bnd.take_steps(1000) ## Her çalıştırıldığında 1000 adım yapar.


# In[39]:


bnd.take_steps(10000) ## Her çalıştırıldığında 10000 adım yapar.


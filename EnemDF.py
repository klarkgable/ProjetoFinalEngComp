#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados= pd.read_csv('C:\\Users\SOLDADO GABLE\Desktop\sample_df_10000.csv',encoding = "ISO-8859-1",sep =';')


# In[3]:


#FILTRANDO A COLUNA ESPECÍFICA PARA O DF E MEDIA DE NOTAS

#Distrito Federal
DF=dados.loc[dados.SG_UF_RESIDENCIA=="DF"]
 #medias nas 4 partes da prova
mediaDFcn=DF.NU_NOTA_CN.mean()
mediaDFch=DF.NU_NOTA_CH.mean()
mediaDFlc=DF.NU_NOTA_LC.mean()
mediaDFmt=DF.NU_NOTA_MT.mean()


# In[ ]:


DF.NU_NOTA_CN.describe()


# In[ ]:


DF.NU_NOTA_CH.describe()


# In[ ]:


DF.NU_NOTA_LC.describe()


# In[ ]:


DF.NU_NOTA_MT.describe()


# In[ ]:





# In[5]:


DF.NU_NOTA_CN.dropna(inplace=True)


# In[6]:


DF.NU_NOTA_CH.dropna(inplace=True)


# In[7]:


DF.NU_NOTA_LC.dropna(inplace=True)


# In[8]:


DF.NU_NOTA_MT.dropna(inplace=True)


# In[15]:


info1


# In[10]:


binsteste = np.linspace(0,1000,51)


# In[11]:


info1, bins1, lixo = plt.hist(DF.NU_NOTA_CN, color="green",bins=binsteste,density=True,rwidth=0.85,label = "norm")


# In[12]:


info2, bins1, lixo = plt.hist(DF.NU_NOTA_CH, color="red",bins=binsteste,density=True,rwidth=0.85,label = "norm")


# In[13]:


info3, bins1, lixo = plt.hist(DF.NU_NOTA_LC, color="black",bins=binsteste,density=True,rwidth=0.85,label = "norm")


# In[14]:


info4, bins1, lixo = plt.hist(DF.NU_NOTA_MT, color="blue",bins=binsteste,density=True,rwidth=0.85,label = "norm")


# In[ ]:





# In[ ]:





# In[17]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Ciências da Natureza
#plt.hist(DF.NU_NOTA_CN, color="green",bins=50,density=True,rwidth=0.85,align = 'left',stacked = True, alpha = 0.7,label = "norm")#,'b--',linewidth=2.0,marker='.' )
plt.bar(binsteste[:-1], info1*20,17, color="green")
plt.title("Notas em Ciências da Natureza - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[10]:





# In[16]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Ciências Humanas
#plt.hist(DF.NU_NOTA_CH, color="red",bins=50,density=True,rwidth=0.85,align = 'left',stacked = True, alpha = 0.7,label = "norm")#,'b--',linewidth=2.0,marker='.' )
plt.bar(binsteste[:-1], info2*20,17, color="red")
plt.title("Notas em Ciências Humanas - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[12]:





# In[18]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Linguagens e códigos
#plt.hist(DF.NU_NOTA_LC, color="black",bins=50,density=True,rwidth=0.85,align = 'left',stacked = True, alpha = 0.7,label = "norm")#, 'b--',marker='o' )
plt.bar(binsteste[:-1], info3*20,17, color="black")
plt.title("Notas em Linguagens e Códigos - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[14]:





# In[19]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Matemática
#plt.hist(DF.NU_NOTA_MT,color="blue",bins=50,density=True,rwidth=0.85,align = 'left',stacked = True, alpha = 0.7,label = "norm")#,'b--',linewidth=2.0,marker='o')
plt.bar(binsteste[:-1], info4*20,17, color="blue")
plt.title("Notas em Matemática - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





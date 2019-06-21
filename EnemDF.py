#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_csv('C:\\Users\SOLDADO GABLE\Desktop\sample_df_10000.csv',encoding = "ISO-8859-1",sep =';')


# In[ ]:


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





# In[ ]:


DF.NU_NOTA_CN.dropna(inplace=True)


# In[ ]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Ciências da Natureza
plt.hist(DF.NU_NOTA_CN, color="green",bins=30)#,'b--',linewidth=2.0,marker='.' )
plt.title("Notas em Ciências da Natureza - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:


DF.NU_NOTA_CH.dropna(inplace=True)


# In[ ]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Ciências Humanas
plt.hist(DF.NU_NOTA_CH, color="red", bins=20)#,'b--',linewidth=2.0,marker='.' )
plt.title("Notas em Ciências Humanas - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:


DF.NU_NOTA_LC.dropna(inplace=True)


# In[ ]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Linguagens e códigos
plt.hist(DF.NU_NOTA_LC, color="black",bins=20)#, 'b--',marker='o' )
plt.title("Notas em Linguagens e Códigos - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:


DF.NU_NOTA_MT.dropna(inplace=True)


# In[ ]:


#Gráfico de notas para Distrito Federal que é o local da realização do trabalho
#Matemática
plt.hist(DF.NU_NOTA_MT,color="blue",bins=30)#,'b--',linewidth=2.0,marker='o')
plt.title("Notas em Matemática - Distrito Federal")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





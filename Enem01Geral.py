#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

dados= pd.read_excel('C:\\Users\SOLDADO GABLE\Desktop\micros_dados_enem_2017_10000.xls',encoding = "ISO-8859-1",sep =';')


# In[ ]:


#Vetores com respostas e gabaritos das provas

respostaCN=dados.TX_RESPOSTAS_CN #Vetor com as respostas da parte objetiva da prova de Ciências da Natureza(45 itens)
respostaCH=dados.TX_RESPOSTAS_CH    #Vetor com as respostas da parte objetiva da prova de Ciências Humanas(45 itens)
respostaLC=dados.TX_RESPOSTAS_LC    #Vetor com as respostas da parte objetiva da prova de Linguagens e Códigos(50 itens)
respostaMT=dados.TX_RESPOSTAS_MT   #Vetor com as respostas da parte objetiva da prova de Matemática (45 Itens)

escolhaLINGUA=dados.TP_LINGUA          #Qual Língua Estrangeira escolhida(0:inglês e 1:espanhol)

gabaritoCN=dados.TX_GABARITO_CN #Vetor com o gabarito da parte objetiva da prova de Ciências da Natureza
gabaritoCH=dados.TX_GABARITO_CH    #Vetor com o gabarito da parte objetiva da prova de Ciências Humanas
gabaritoLC=dados.TX_GABARITO_LC   #Vetor com o gabarito da parte objetiva da prova de Linguagens e Códigos 
gabaritoMT=dados.TX_GABARITO_MT    #Vetor com o gabarito da parte objetiva da prova de Matemática


# In[ ]:


#Eliminando os campos nulos

#eliminando dados nulos de CN
respostaCN.dropna(inplace=True)
gabaritoCN.dropna(inplace=True)

#eliminando dados nulos de CH
respostaCH.dropna(inplace=True)
gabaritoCH.dropna(inplace=True)

#eliminando dados nulos de LC
respostaLC.dropna(inplace=True)
gabaritoLC.dropna(inplace=True)

#eliminando dados nulos de MT
respostaMT.dropna(inplace=True)
gabaritoMT.dropna(inplace=True)


# In[ ]:


#ROTINA PARA GERAR COLUNAS DE ZEROS E UNS DE ACORDO COM RESPOSTA E GABARITO DE CADA ALUNO NA PROVA DE Ciências da Natureza
#45 questões

resultCNq1=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq2=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq3=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq4=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq5=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq6=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq7=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq8=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq9=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq10=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq11=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq12=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq13=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq14=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq15=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq16=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq17=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq18=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq19=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq20=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq21=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq22=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq23=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq24=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq25=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq26=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq27=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq28=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq29=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq30=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq31=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq32=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq33=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq34=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq35=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq36=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq37=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq38=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq39=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq40=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq41=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq42=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq43=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq44=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCNq45=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas

#q1
for i in respostaCN.index: 
    if(respostaCN[i][0] == gabaritoCN[i][0]):
        resultCNq1[i]=1
    else:
        resultCNq1[i]=0            
#gera a coluna com zeros e uns para cada questao

#q2
for i in respostaCN.index: 
    if(respostaCN[i][1] == gabaritoCN[i][1]):
        resultCNq2[i]=1
    else:
        resultCNq2[i]=0            
#gera a coluna com zeros e uns para cada questao

#q3
for i in respostaCN.index: 
    if(respostaCN[i][2] == gabaritoCN[i][2]):
        resultCNq3[i]=1
    else:
        resultCNq3[i]=0            
#gera a coluna com zeros e uns para cada questao

#q4
for i in respostaCN.index: 
    if(respostaCN[i][3] == gabaritoCN[i][3]):
        resultCNq4[i]=1
    else:
        resultCNq4[i]=0            
#gera a coluna com zeros e uns para cada questao

#q5
for i in respostaCN.index: 
    if(respostaCN[i][4] == gabaritoCN[i][4]):
        resultCNq5[i]=1
    else:
        resultCNq5[i]=0            
#gera a coluna com zeros e uns para cada questao

#q6
for i in respostaCN.index: 
    if(respostaCN[i][5] == gabaritoCN[i][5]):
        resultCNq6[i]=1
    else:
        resultCNq6[i]=0            
#gera a coluna com zeros e uns para cada questao

#q7
for i in respostaCN.index: 
    if(respostaCN[i][6] == gabaritoCN[i][6]):
        resultCNq7[i]=1
    else:
        resultCNq7[i]=0            
#gera a coluna com zeros e uns para cada questao

#q8
for i in respostaCN.index: 
    if(respostaCN[i][7] == gabaritoCN[i][7]):
        resultCNq8[i]=1
    else:
        resultCNq8[i]=0            
#gera a coluna com zeros e uns para cada questao

#q9
for i in respostaCN.index: 
    if(respostaCN[i][8] == gabaritoCN[i][8]):
        resultCNq9[i]=1
    else:
        resultCNq9[i]=0            
#gera a coluna com zeros e uns para cada questao

#q10
for i in respostaCN.index: 
    if(respostaCN[i][9] == gabaritoCN[i][9]):
        resultCNq10[i]=1
    else:
        resultCNq10[i]=0            
#gera a coluna com zeros e uns para cada questao

#q11
for i in respostaCN.index: 
    if(respostaCN[i][10] == gabaritoCN[i][10]):
        resultCNq11[i]=1
    else:
        resultCNq11[i]=0            
#gera a coluna com zeros e uns para cada questao

#q12
for i in respostaCN.index: 
    if(respostaCN[i][11] == gabaritoCN[i][11]):
        resultCNq12[i]=1
    else:
        resultCNq12[i]=0            
#gera a coluna com zeros e uns para cada questao

#q13
for i in respostaCN.index: 
    if(respostaCN[i][12] == gabaritoCN[i][12]):
        resultCNq13[i]=1
    else:
        resultCNq13[i]=0            
#gera a coluna com zeros e uns para cada questao

#q14
for i in respostaCN.index: 
    if(respostaCN[i][13] == gabaritoCN[i][13]):
        resultCNq14[i]=1
    else:
        resultCNq14[i]=0            
#gera a coluna com zeros e uns para cada questao

#q15
for i in respostaCN.index: 
    if(respostaCN[i][14] == gabaritoCN[i][14]):
        resultCNq15[i]=1
    else:
        resultCNq15[i]=0            
#gera a coluna com zeros e uns para cada questao

#q16
for i in respostaCN.index: 
    if(respostaCN[i][15] == gabaritoCN[i][15]):
        resultCNq16[i]=1
    else:
        resultCNq16[i]=0            
#gera a coluna com zeros e uns para cada questao

#q17
for i in respostaCN.index: 
    if(respostaCN[i][16] == gabaritoCN[i][16]):
        resultCNq17[i]=1
    else:
        resultCNq17[i]=0            
#gera a coluna com zeros e uns para cada questao

#q18
for i in respostaCN.index: 
    if(respostaCN[i][17] == gabaritoCN[i][17]):
        resultCNq18[i]=1
    else:
        resultCNq18[i]=0            
#gera a coluna com zeros e uns para cada questao

#q19
for i in respostaCN.index: 
    if(respostaCN[i][18] == gabaritoCN[i][18]):
        resultCNq19[i]=1
    else:
        resultCNq19[i]=0            
#gera a coluna com zeros e uns para cada questao

#q20
for i in respostaCN.index: 
    if(respostaCN[i][19] == gabaritoCN[i][19]):
        resultCNq20[i]=1
    else:
        resultCNq20[i]=0            
#gera a coluna com zeros e uns para cada questao

#q21
for i in respostaCN.index: 
    if(respostaCN[i][20] == gabaritoCN[i][20]):
        resultCNq21[i]=1
    else:
        resultCNq21[i]=0            
#gera a coluna com zeros e uns para cada questao

#q22
for i in respostaCN.index: 
    if(respostaCN[i][21] == gabaritoCN[i][21]):
        resultCNq22[i]=1
    else:
        resultCNq22[i]=0            
#gera a coluna com zeros e uns para cada questao

#q23
for i in respostaCN.index: 
    if(respostaCN[i][22] == gabaritoCN[i][22]):
        resultCNq23[i]=1
    else:
        resultCNq23[i]=0            
#gera a coluna com zeros e uns para cada questao

#q24
for i in respostaCN.index: 
    if(respostaCN[i][23] == gabaritoCN[i][23]):
        resultCNq24[i]=1
    else:
        resultCNq24[i]=0            
#gera a coluna com zeros e uns para cada questao

#q25
for i in respostaCN.index: 
    if(respostaCN[i][24] == gabaritoCN[i][24]):
        resultCNq25[i]=1
    else:
        resultCNq25[i]=0            
#gera a coluna com zeros e uns para cada questao

#q26
for i in respostaCN.index: 
    if(respostaCN[i][25] == gabaritoCN[i][25]):
        resultCNq26[i]=1
    else:
        resultCNq26[i]=0            
#gera a coluna com zeros e uns para cada questao

#q27
for i in respostaCN.index: 
    if(respostaCN[i][26] == gabaritoCN[i][26]):
        resultCNq27[i]=1
    else:
        resultCNq27[i]=0            
#gera a coluna com zeros e uns para cada questao

#q28
for i in respostaCN.index: 
    if(respostaCN[i][27] == gabaritoCN[i][27]):
        resultCNq28[i]=1
    else:
        resultCNq28[i]=0            
#gera a coluna com zeros e uns para cada questao

#q29
for i in respostaCN.index: 
    if(respostaCN[i][28] == gabaritoCN[i][28]):
        resultCNq29[i]=1
    else:
        resultCNq29[i]=0            
#gera a coluna com zeros e uns para cada questao

#q30
for i in respostaCN.index: 
    if(respostaCN[i][29] == gabaritoCN[i][29]):
        resultCNq30[i]=1
    else:
        resultCNq30[i]=0            
#gera a coluna com zeros e uns para cada questao

#q31
for i in respostaCN.index: 
    if(respostaCN[i][30] == gabaritoCN[i][30]):
        resultCNq31[i]=1
    else:
        resultCNq31[i]=0            
#gera a coluna com zeros e uns para cada questao

#q32
for i in respostaCN.index: 
    if(respostaCN[i][31] == gabaritoCN[i][31]):
        resultCNq32[i]=1
    else:
        resultCNq32[i]=0            
#gera a coluna com zeros e uns para cada questao

#q33
for i in respostaCN.index: 
    if(respostaCN[i][32] == gabaritoCN[i][32]):
        resultCNq33[i]=1
    else:
        resultCNq33[i]=0            
#gera a coluna com zeros e uns para cada questao

#q34
for i in respostaCN.index: 
    if(respostaCN[i][33] == gabaritoCN[i][33]):
        resultCNq34[i]=1
    else:
        resultCNq34[i]=0            
#gera a coluna com zeros e uns para cada questao

#q35
for i in respostaCN.index: 
    if(respostaCN[i][34] == gabaritoCN[i][34]):
        resultCNq35[i]=1
    else:
        resultCNq35[i]=0            
#gera a coluna com zeros e uns para cada questao

#q36
for i in respostaCN.index: 
    if(respostaCN[i][35] == gabaritoCN[i][35]):
        resultCNq36[i]=1
    else:
        resultCNq36[i]=0            
#gera a coluna com zeros e uns para cada questao

#q37
for i in respostaCN.index: 
    if(respostaCN[i][36] == gabaritoCN[i][36]):
        resultCNq37[i]=1
    else:
        resultCNq37[i]=0            
#gera a coluna com zeros e uns para cada questao

#q38
for i in respostaCN.index: 
    if(respostaCN[i][37] == gabaritoCN[i][37]):
        resultCNq38[i]=1
    else:
        resultCNq38[i]=0            
#gera a coluna com zeros e uns para cada questao

#q39
for i in respostaCN.index: 
    if(respostaCN[i][38] == gabaritoCN[i][38]):
        resultCNq39[i]=1
    else:
        resultCNq39[i]=0            
#gera a coluna com zeros e uns para cada questao

#q40
for i in respostaCN.index: 
    if(respostaCN[i][39] == gabaritoCN[i][39]):
        resultCNq40[i]=1
    else:
        resultCNq40[i]=0            
#gera a coluna com zeros e uns para cada questao

#q41
for i in respostaCN.index: 
    if(respostaCN[i][40] == gabaritoCN[i][40]):
        resultCNq41[i]=1
    else:
        resultCNq41[i]=0            
#gera a coluna com zeros e uns para cada questao

#q42
for i in respostaCN.index: 
    if(respostaCN[i][41] == gabaritoCN[i][41]):
        resultCNq42[i]=1
    else:
        resultCNq42[i]=0            
#gera a coluna com zeros e uns para cada questao

#q43
for i in respostaCN.index: 
    if(respostaCN[i][42] == gabaritoCN[i][42]):
        resultCNq43[i]=1
    else:
        resultCNq43[i]=0            
#gera a coluna com zeros e uns para cada questao

#q44
for i in respostaCN.index: 
    if(respostaCN[i][43] == gabaritoCN[i][43]):
        resultCNq44[i]=1
    else:
        resultCNq44[i]=0            
#gera a coluna com zeros e uns para cada questao

#q45
for i in respostaCN.index: 
    if(respostaCN[i][44] == gabaritoCN[i][44]):
        resultCNq45[i]=1
    else:
        resultCNq45[i]=0            
#gera a coluna com zeros e uns para cada questao



#definindo coluna de resultado para prova de Ciências da Natureza

dados['TX_Result_CN_questao1']=resultCNq1
dados['TX_Result_CN_questao2']=resultCNq2
dados['TX_Result_CN_questao3']=resultCNq3
dados['TX_Result_CN_questao4']=resultCNq4
dados['TX_Result_CN_questao5']=resultCNq5
dados['TX_Result_CN_questao6']=resultCNq6
dados['TX_Result_CN_questao7']=resultCNq7
dados['TX_Result_CN_questao8']=resultCNq8
dados['TX_Result_CN_questao9']=resultCNq9
dados['TX_Result_CN_questao10']=resultCNq10
dados['TX_Result_CN_questao11']=resultCNq11
dados['TX_Result_CN_questao12']=resultCNq12
dados['TX_Result_CN_questao13']=resultCNq13
dados['TX_Result_CN_questao14']=resultCNq14
dados['TX_Result_CN_questao15']=resultCNq15
dados['TX_Result_CN_questao16']=resultCNq16
dados['TX_Result_CN_questao17']=resultCNq17
dados['TX_Result_CN_questao18']=resultCNq18
dados['TX_Result_CN_questao19']=resultCNq19
dados['TX_Result_CN_questao20']=resultCNq20
dados['TX_Result_CN_questao21']=resultCNq21
dados['TX_Result_CN_questao22']=resultCNq22
dados['TX_Result_CN_questao23']=resultCNq23
dados['TX_Result_CN_questao24']=resultCNq24
dados['TX_Result_CN_questao25']=resultCNq25
dados['TX_Result_CN_questao26']=resultCNq26
dados['TX_Result_CN_questao27']=resultCNq27
dados['TX_Result_CN_questao28']=resultCNq28
dados['TX_Result_CN_questao29']=resultCNq29
dados['TX_Result_CN_questao30']=resultCNq30
dados['TX_Result_CN_questao31']=resultCNq31
dados['TX_Result_CN_questao32']=resultCNq32
dados['TX_Result_CN_questao33']=resultCNq33
dados['TX_Result_CN_questao34']=resultCNq34
dados['TX_Result_CN_questao35']=resultCNq35
dados['TX_Result_CN_questao36']=resultCNq36
dados['TX_Result_CN_questao37']=resultCNq37
dados['TX_Result_CN_questao38']=resultCNq38
dados['TX_Result_CN_questao39']=resultCNq39
dados['TX_Result_CN_questao40']=resultCNq40
dados['TX_Result_CN_questao41']=resultCNq41
dados['TX_Result_CN_questao42']=resultCNq42
dados['TX_Result_CN_questao43']=resultCNq43
dados['TX_Result_CN_questao44']=resultCNq44
dados['TX_Result_CN_questao45']=resultCNq45


# In[ ]:


#ROTINA PARA GERAR COLUNA DE ZEROS E UNS DE ACORDO COM RESPOSTA E GABARITO DE CADA ALUNO NA PROVA DE Ciências Humanas


resultCHq1=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq2=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq3=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq4=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq5=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq6=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq7=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq8=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq9=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq10=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq11=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq12=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq13=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq14=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq15=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq16=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq17=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq18=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq19=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq20=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq21=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq22=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq23=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq24=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq25=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq26=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq27=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq28=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq29=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq30=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq31=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq32=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq33=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq34=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq35=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq36=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq37=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq38=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq39=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq40=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq41=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq42=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq43=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq44=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultCHq45=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas


#q1
for i in respostaCH.index: 
    if(respostaCH[i][0] == gabaritoCH[i][0]):
        resultCHq1[i]=1
    else:
        resultCHq1[i]=0            
#gera a coluna com zeros e uns para cada questao

#q2
for i in respostaCH.index: 
    if(respostaCH[i][1] == gabaritoCH[i][1]):
        resultCHq2[i]=1
    else:
        resultCHq2[i]=0            
#gera a coluna com zeros e uns para cada questao

#q3
for i in respostaCH.index: 
    if(respostaCH[i][2] == gabaritoCH[i][2]):
        resultCHq3[i]=1
    else:
        resultCHq3[i]=0            
#gera a coluna com zeros e uns para cada questao

#q4
for i in respostaCH.index: 
    if(respostaCH[i][3] == gabaritoCH[i][3]):
        resultCHq4[i]=1
    else:
        resultCHq4[i]=0            
#gera a coluna com zeros e uns para cada questao

#q5
for i in respostaCH.index: 
    if(respostaCH[i][4] == gabaritoCH[i][4]):
        resultCHq5[i]=1
    else:
        resultCHq5[i]=0            
#gera a coluna com zeros e uns para cada questao

#q6
for i in respostaCH.index: 
    if(respostaCH[i][5] == gabaritoCH[i][5]):
        resultCHq6[i]=1
    else:
        resultCHq6[i]=0            
#gera a coluna com zeros e uns para cada questao

#q7
for i in respostaCH.index: 
    if(respostaCH[i][6] == gabaritoCH[i][6]):
        resultCHq7[i]=1
    else:
        resultCHq7[i]=0            
#gera a coluna com zeros e uns para cada questao

#q8
for i in respostaCH.index: 
    if(respostaCH[i][7] == gabaritoCH[i][7]):
        resultCHq8[i]=1
    else:
        resultCHq8[i]=0            
#gera a coluna com zeros e uns para cada questao

#q9
for i in respostaCH.index: 
    if(respostaCH[i][8] == gabaritoCH[i][8]):
        resultCHq9[i]=1
    else:
        resultCHq9[i]=0            
#gera a coluna com zeros e uns para cada questao

#q10
for i in respostaCH.index: 
    if(respostaCH[i][9] == gabaritoCH[i][9]):
        resultCHq10[i]=1
    else:
        resultCHq10[i]=0            
#gera a coluna com zeros e uns para cada questao

#q11
for i in respostaCH.index: 
    if(respostaCH[i][10] == gabaritoCH[i][10]):
        resultCHq11[i]=1
    else:
        resultCHq11[i]=0            
#gera a coluna com zeros e uns para cada questao

#q12
for i in respostaCH.index: 
    if(respostaCH[i][11] == gabaritoCH[i][11]):
        resultCHq12[i]=1
    else:
        resultCHq12[i]=0            
#gera a coluna com zeros e uns para cada questao

#q13
for i in respostaCH.index: 
    if(respostaCH[i][12] == gabaritoCH[i][12]):
        resultCHq13[i]=1
    else:
        resultCHq13[i]=0            
#gera a coluna com zeros e uns para cada questao

#q14
for i in respostaCH.index: 
    if(respostaCH[i][13] == gabaritoCH[i][13]):
        resultCHq14[i]=1
    else:
        resultCHq14[i]=0            
#gera a coluna com zeros e uns para cada questao

#q15
for i in respostaCH.index: 
    if(respostaCH[i][14] == gabaritoCH[i][14]):
        resultCHq15[i]=1
    else:
        resultCHq15[i]=0            
#gera a coluna com zeros e uns para cada questao

#q16
for i in respostaCH.index: 
    if(respostaCH[i][15] == gabaritoCH[i][15]):
        resultCHq16[i]=1
    else:
        resultCHq16[i]=0            
#gera a coluna com zeros e uns para cada questao

#q17
for i in respostaCH.index: 
    if(respostaCH[i][16] == gabaritoCH[i][16]):
        resultCHq17[i]=1
    else:
        resultCHq17[i]=0            
#gera a coluna com zeros e uns para cada questao

#q18
for i in respostaCH.index: 
    if(respostaCH[i][17] == gabaritoCH[i][17]):
        resultCHq18[i]=1
    else:
        resultCHq18[i]=0            
#gera a coluna com zeros e uns para cada questao

#q19
for i in respostaCH.index: 
    if(respostaCH[i][18] == gabaritoCH[i][18]):
        resultCHq19[i]=1
    else:
        resultCHq19[i]=0            
#gera a coluna com zeros e uns para cada questao

#q20
for i in respostaCH.index: 
    if(respostaCH[i][19] == gabaritoCH[i][19]):
        resultCHq20[i]=1
    else:
        resultCHq20[i]=0            
#gera a coluna com zeros e uns para cada questao

#q21
for i in respostaCH.index: 
    if(respostaCH[i][20] == gabaritoCH[i][20]):
        resultCHq21[i]=1
    else:
        resultCHq21[i]=0            
#gera a coluna com zeros e uns para cada questao

#q22
for i in respostaCH.index: 
    if(respostaCH[i][21] == gabaritoCH[i][21]):
        resultCHq22[i]=1
    else:
        resultCHq22[i]=0            
#gera a coluna com zeros e uns para cada questao

#q23
for i in respostaCH.index: 
    if(respostaCH[i][22] == gabaritoCH[i][22]):
        resultCHq23[i]=1
    else:
        resultCHq23[i]=0            
#gera a coluna com zeros e uns para cada questao

#q24
for i in respostaCH.index: 
    if(respostaCH[i][23] == gabaritoCH[i][23]):
        resultCHq24[i]=1
    else:
        resultCHq24[i]=0            
#gera a coluna com zeros e uns para cada questao

#q25
for i in respostaCH.index: 
    if(respostaCH[i][24] == gabaritoCH[i][24]):
        resultCHq25[i]=1
    else:
        resultCHq25[i]=0            
#gera a coluna com zeros e uns para cada questao

#q26
for i in respostaCH.index: 
    if(respostaCH[i][25] == gabaritoCH[i][25]):
        resultCHq26[i]=1
    else:
        resultCHq26[i]=0            
#gera a coluna com zeros e uns para cada questao

#q27
for i in respostaCH.index: 
    if(respostaCH[i][26] == gabaritoCH[i][26]):
        resultCHq27[i]=1
    else:
        resultCHq27[i]=0            
#gera a coluna com zeros e uns para cada questao

#q28
for i in respostaCH.index: 
    if(respostaCH[i][27] == gabaritoCH[i][27]):
        resultCHq28[i]=1
    else:
        resultCHq28[i]=0            
#gera a coluna com zeros e uns para cada questao

#q29
for i in respostaCH.index: 
    if(respostaCH[i][28] == gabaritoCH[i][28]):
        resultCHq29[i]=1
    else:
        resultCHq29[i]=0            
#gera a coluna com zeros e uns para cada questao

#q30
for i in respostaCH.index: 
    if(respostaCH[i][29] == gabaritoCH[i][29]):
        resultCHq30[i]=1
    else:
        resultCHq30[i]=0            
#gera a coluna com zeros e uns para cada questao

#q31
for i in respostaCH.index: 
    if(respostaCH[i][30] == gabaritoCH[i][30]):
        resultCHq31[i]=1
    else:
        resultCHq31[i]=0            
#gera a coluna com zeros e uns para cada questao

#q32
for i in respostaCH.index: 
    if(respostaCH[i][31] == gabaritoCH[i][31]):
        resultCHq32[i]=1
    else:
        resultCHq32[i]=0            
#gera a coluna com zeros e uns para cada questao

#q33
for i in respostaCH.index: 
    if(respostaCH[i][32] == gabaritoCH[i][32]):
        resultCHq33[i]=1
    else:
        resultCHq33[i]=0            
#gera a coluna com zeros e uns para cada questao

#q34
for i in respostaCH.index: 
    if(respostaCH[i][33] == gabaritoCH[i][33]):
        resultCHq34[i]=1
    else:
        resultCHq34[i]=0            
#gera a coluna com zeros e uns para cada questao

#q35
for i in respostaCH.index: 
    if(respostaCH[i][34] == gabaritoCH[i][34]):
        resultCHq35[i]=1
    else:
        resultCHq35[i]=0            
#gera a coluna com zeros e uns para cada questao

#q36
for i in respostaCH.index: 
    if(respostaCH[i][35] == gabaritoCH[i][35]):
        resultCHq36[i]=1
    else:
        resultCHq36[i]=0            
#gera a coluna com zeros e uns para cada questao

#q37
for i in respostaCH.index: 
    if(respostaCH[i][36] == gabaritoCH[i][36]):
        resultCHq37[i]=1
    else:
        resultCHq37[i]=0            
#gera a coluna com zeros e uns para cada questao

#q38
for i in respostaCH.index: 
    if(respostaCH[i][37] == gabaritoCH[i][37]):
        resultCHq38[i]=1
    else:
        resultCHq38[i]=0            
#gera a coluna com zeros e uns para cada questao

#q39
for i in respostaCH.index: 
    if(respostaCH[i][38] == gabaritoCH[i][38]):
        resultCHq39[i]=1
    else:
        resultCHq39[i]=0            
#gera a coluna com zeros e uns para cada questao

#q40
for i in respostaCH.index: 
    if(respostaCH[i][39] == gabaritoCH[i][39]):
        resultCHq40[i]=1
    else:
        resultCHq40[i]=0            
#gera a coluna com zeros e uns para cada questao

#q41
for i in respostaCH.index: 
    if(respostaCH[i][40] == gabaritoCH[i][40]):
        resultCHq41[i]=1
    else:
        resultCHq41[i]=0            
#gera a coluna com zeros e uns para cada questao

#q42
for i in respostaCH.index: 
    if(respostaCH[i][41] == gabaritoCH[i][41]):
        resultCHq42[i]=1
    else:
        resultCHq42[i]=0            
#gera a coluna com zeros e uns para cada questao

#q43
for i in respostaCH.index: 
    if(respostaCH[i][42] == gabaritoCH[i][42]):
        resultCHq43[i]=1
    else:
        resultCHq43[i]=0            
#gera a coluna com zeros e uns para cada questao

#q44
for i in respostaCH.index: 
    if(respostaCH[i][43] == gabaritoCH[i][43]):
        resultCHq44[i]=1
    else:
        resultCHq44[i]=0            
#gera a coluna com zeros e uns para cada questao

#q45
for i in respostaCH.index: 
    if(respostaCH[i][44] == gabaritoCH[i][44]):
        resultCHq45[i]=1
    else:
        resultCHq45[i]=0            
#gera a coluna com zeros e uns para cada questao


#definindo coluna de resultado para prova de Ciências Humanas

dados['TX_Result_CH_questao1']=resultCHq1
dados['TX_Result_CH_questao2']=resultCHq2
dados['TX_Result_CH_questao3']=resultCHq3
dados['TX_Result_CH_questao4']=resultCHq4
dados['TX_Result_CH_questao5']=resultCHq5
dados['TX_Result_CH_questao6']=resultCHq6
dados['TX_Result_CH_questao7']=resultCHq7
dados['TX_Result_CH_questao8']=resultCHq8
dados['TX_Result_CH_questao9']=resultCHq9
dados['TX_Result_CH_questao10']=resultCHq10
dados['TX_Result_CH_questao11']=resultCHq11
dados['TX_Result_CH_questao12']=resultCHq12
dados['TX_Result_CH_questao13']=resultCHq13
dados['TX_Result_CH_questao14']=resultCHq14
dados['TX_Result_CH_questao15']=resultCHq15
dados['TX_Result_CH_questao16']=resultCHq16
dados['TX_Result_CH_questao17']=resultCHq17
dados['TX_Result_CH_questao18']=resultCHq18
dados['TX_Result_CH_questao19']=resultCHq19
dados['TX_Result_CH_questao20']=resultCHq20
dados['TX_Result_CH_questao21']=resultCHq21
dados['TX_Result_CH_questao22']=resultCHq22
dados['TX_Result_CH_questao23']=resultCHq23
dados['TX_Result_CH_questao24']=resultCHq24
dados['TX_Result_CH_questao25']=resultCHq25
dados['TX_Result_CH_questao26']=resultCHq26
dados['TX_Result_CH_questao27']=resultCHq27
dados['TX_Result_CH_questao28']=resultCHq28
dados['TX_Result_CH_questao29']=resultCHq29
dados['TX_Result_CH_questao30']=resultCHq30
dados['TX_Result_CH_questao31']=resultCHq31
dados['TX_Result_CH_questao32']=resultCHq32
dados['TX_Result_CH_questao33']=resultCHq33
dados['TX_Result_CH_questao34']=resultCHq34
dados['TX_Result_CH_questao35']=resultCHq35
dados['TX_Result_CH_questao36']=resultCHq36
dados['TX_Result_CH_questao37']=resultCHq37
dados['TX_Result_CH_questao38']=resultCHq38
dados['TX_Result_CH_questao39']=resultCHq39
dados['TX_Result_CH_questao40']=resultCHq40
dados['TX_Result_CH_questao41']=resultCHq41
dados['TX_Result_CH_questao42']=resultCHq42
dados['TX_Result_CH_questao43']=resultCHq43
dados['TX_Result_CH_questao44']=resultCHq44
dados['TX_Result_CH_questao45']=resultCHq45


# In[ ]:


#ROTINA PARA GERAR COLUNA DE ZEROS E UNS DE ACORDO COM RESPOSTA E GABARITO DE CADA ALUNO NA PROVA DE Linguagens e Códigos

resultLCq1=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq2=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq3=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq4=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq5=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq6=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq7=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq8=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq9=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq10=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq11=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq12=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq13=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq14=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq15=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq16=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq17=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq18=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq19=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq20=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq21=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq22=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq23=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq24=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq25=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq26=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq27=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq28=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq29=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq30=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq31=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq32=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq33=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq34=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq35=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq36=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq37=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq38=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq39=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq40=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq41=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq42=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq43=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq44=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq45=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq46=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq47=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq48=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq49=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultLCq50=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas

#q1
for i in respostaLC.index: 
    if(respostaLC[i][0] == gabaritoLC[i][0]):
        resultLCq1[i]=1
    else:
        resultLCq1[i]=0            
#gera a coluna com zeros e uns para cada questao

#q2
for i in respostaLC.index: 
    if(respostaLC[i][1] == gabaritoLC[i][1]):
        resultLCq2[i]=1
    else:
        resultLCq2[i]=0            
#gera a coluna com zeros e uns para cada questao

#q3
for i in respostaLC.index: 
    if(respostaLC[i][2] == gabaritoLC[i][2]):
        resultLCq3[i]=1
    else:
        resultLCq3[i]=0            
#gera a coluna com zeros e uns para cada questao

#q4
for i in respostaLC.index: 
    if(respostaLC[i][3] == gabaritoLC[i][3]):
        resultLCq4[i]=1
    else:
        resultLCq4[i]=0            
#gera a coluna com zeros e uns para cada questao

#q5
for i in respostaLC.index: 
    if(respostaLC[i][4] == gabaritoLC[i][4]):
        resultLCq5[i]=1
    else:
        resultLCq5[i]=0            
#gera a coluna com zeros e uns para cada questao

#q6
for i in respostaCH.index: 
    if(respostaLC[i][5] == gabaritoLC[i][5]):
        resultLCq6[i]=1
    else:
        resultLCq6[i]=0            
#gera a coluna com zeros e uns para cada questao

#q7
for i in respostaLC.index: 
    if(respostaLC[i][6] == gabaritoLC[i][6]):
        resultLCq7[i]=1
    else:
        resultLCq7[i]=0            
#gera a coluna com zeros e uns para cada questao

#q8
for i in respostaLC.index: 
    if(respostaLC[i][7] == gabaritoLC[i][7]):
        resultLCq8[i]=1
    else:
        resultLCq8[i]=0            
#gera a coluna com zeros e uns para cada questao

#q9
for i in respostaLC.index: 
    if(respostaLC[i][8] == gabaritoLC[i][8]):
        resultLCq9[i]=1
    else:
        resultLCq9[i]=0            
#gera a coluna com zeros e uns para cada questao

#q10
for i in respostaLC.index: 
    if(respostaLC[i][9] == gabaritoLC[i][9]):
        resultLCq10[i]=1
    else:
        resultLCq10[i]=0            
#gera a coluna com zeros e uns para cada questao

#q11
for i in respostaLC.index: 
    if(respostaLC[i][10] == gabaritoLC[i][10]):
        resultLCq11[i]=1
    else:
        resultLCq11[i]=0            
#gera a coluna com zeros e uns para cada questao

#q12
for i in respostaLC.index: 
    if(respostaLC[i][11] == gabaritoLC[i][11]):
        resultLCq12[i]=1
    else:
        resultLCq12[i]=0            
#gera a coluna com zeros e uns para cada questao

#q13
for i in respostaLC.index: 
    if(respostaLC[i][12] == gabaritoLC[i][12]):
        resultLCq13[i]=1
    else:
        resultLCq13[i]=0            
#gera a coluna com zeros e uns para cada questao

#q14
for i in respostaLC.index: 
    if(respostaLC[i][13] == gabaritoLC[i][13]):
        resultLCq14[i]=1
    else:
        resultLCq14[i]=0            
#gera a coluna com zeros e uns para cada questao

#q15
for i in respostaLC.index: 
    if(respostaLC[i][14] == gabaritoLC[i][14]):
        resultLCq15[i]=1
    else:
        resultLCq15[i]=0            
#gera a coluna com zeros e uns para cada questao

#q16
for i in respostaLC.index: 
    if(respostaLC[i][15] == gabaritoLC[i][15]):
        resultLCq16[i]=1
    else:
        resultLCq16[i]=0            
#gera a coluna com zeros e uns para cada questao

#q17
for i in respostaLC.index: 
    if(respostaLC[i][16] == gabaritoLC[i][16]):
        resultLCq17[i]=1
    else:
        resultLCq17[i]=0            
#gera a coluna com zeros e uns para cada questao

#q18
for i in respostaLC.index: 
    if(respostaLC[i][17] == gabaritoLC[i][17]):
        resultLCq18[i]=1
    else:
        resultLCq18[i]=0            
#gera a coluna com zeros e uns para cada questao

#q19
for i in respostaLC.index: 
    if(respostaLC[i][18] == gabaritoLC[i][18]):
        resultLCq19[i]=1
    else:
        resultLCq19[i]=0            
#gera a coluna com zeros e uns para cada questao

#q20
for i in respostaLC.index: 
    if(respostaLC[i][19] == gabaritoCH[i][19]):
        resultLCq20[i]=1
    else:
        resultLCq20[i]=0            
#gera a coluna com zeros e uns para cada questao

#q21
for i in respostaLC.index: 
    if(respostaLC[i][20] == gabaritoLC[i][20]):
        resultLCq21[i]=1
    else:
        resultLCq21[i]=0            
#gera a coluna com zeros e uns para cada questao

#q22
for i in respostaLC.index: 
    if(respostaLC[i][21] == gabaritoLC[i][21]):
        resultLCq22[i]=1
    else:
        resultLCq22[i]=0            
#gera a coluna com zeros e uns para cada questao

#q23
for i in respostaLC.index: 
    if(respostaLC[i][22] == gabaritoLC[i][22]):
        resultLCq23[i]=1
    else:
        resultLCq23[i]=0            
#gera a coluna com zeros e uns para cada questao

#q24
for i in respostaLC.index: 
    if(respostaLC[i][23] == gabaritoLC[i][23]):
        resultLCq24[i]=1
    else:
        resultLCq24[i]=0            
#gera a coluna com zeros e uns para cada questao

#q25
for i in respostaLC.index: 
    if(respostaLC[i][24] == gabaritoLC[i][24]):
        resultLCq25[i]=1
    else:
        resultLCq25[i]=0            
#gera a coluna com zeros e uns para cada questao

#q26
for i in respostaLC.index: 
    if(respostaLC[i][25] == gabaritoLC[i][25]):
        resultLCq26[i]=1
    else:
        resultLCq26[i]=0            
#gera a coluna com zeros e uns para cada questao

#q27
for i in respostaLC.index: 
    if(respostaLC[i][26] == gabaritoLC[i][26]):
        resultLCq27[i]=1
    else:
        resultLCq27[i]=0            
#gera a coluna com zeros e uns para cada questao

#q28
for i in respostaLC.index: 
    if(respostaLC[i][27] == gabaritoLC[i][27]):
        resultLCq28[i]=1
    else:
        resultLCq28[i]=0            
#gera a coluna com zeros e uns para cada questao

#q29
for i in respostaLC.index: 
    if(respostaLC[i][28] == gabaritoLC[i][28]):
        resultLCq29[i]=1
    else:
        resultLCq29[i]=0            
#gera a coluna com zeros e uns para cada questao

#q30
for i in respostaLC.index: 
    if(respostaLC[i][29] == gabaritoLC[i][29]):
        resultLCq30[i]=1
    else:
        resultLCq30[i]=0            
#gera a coluna com zeros e uns para cada questao

#q31
for i in respostaLC.index: 
    if(respostaLC[i][30] == gabaritoLC[i][30]):
        resultLCq31[i]=1
    else:
        resultLCq31[i]=0            
#gera a coluna com zeros e uns para cada questao

#q32
for i in respostaLC.index: 
    if(respostaLC[i][31] == gabaritoLC[i][31]):
        resultLCq32[i]=1
    else:
        resultLCq32[i]=0            
#gera a coluna com zeros e uns para cada questao

#q33
for i in respostaLC.index: 
    if(respostaLC[i][32] == gabaritoLC[i][32]):
        resultLCq33[i]=1
    else:
        resultLCq33[i]=0            
#gera a coluna com zeros e uns para cada questao

#q34
for i in respostaLC.index: 
    if(respostaLC[i][33] == gabaritoLC[i][33]):
        resultLCq34[i]=1
    else:
        resultLCq34[i]=0            
#gera a coluna com zeros e uns para cada questao

#q35
for i in respostaLC.index: 
    if(respostaLC[i][34] == gabaritoLC[i][34]):
        resultLCq35[i]=1
    else:
        resultLCq35[i]=0            
#gera a coluna com zeros e uns para cada questao

#q36
for i in respostaLC.index: 
    if(respostaLC[i][35] == gabaritoLC[i][35]):
        resultLCq36[i]=1
    else:
        resultLCq36[i]=0            
#gera a coluna com zeros e uns para cada questao

#q37
for i in respostaLC.index: 
    if(respostaLC[i][36] == gabaritoLC[i][36]):
        resultLCq37[i]=1
    else:
        resultLCq37[i]=0            
#gera a coluna com zeros e uns para cada questao

#q38
for i in respostaLC.index: 
    if(respostaLC[i][37] == gabaritoLC[i][37]):
        resultLCq38[i]=1
    else:
        resultLCq38[i]=0            
#gera a coluna com zeros e uns para cada questao

#q39
for i in respostaLC.index: 
    if(respostaLC[i][38] == gabaritoLC[i][38]):
        resultLCq39[i]=1
    else:
        resultLCq39[i]=0            
#gera a coluna com zeros e uns para cada questao

#q40
for i in respostaLC.index: 
    if(respostaLC[i][39] == gabaritoLC[i][39]):
        resultLCq40[i]=1
    else:
        resultLCq40[i]=0            
#gera a coluna com zeros e uns para cada questao

#q41
for i in respostaLC.index: 
    if(respostaLC[i][40] == gabaritoLC[i][40]):
        resultLCq41[i]=1
    else:
        resultLCq41[i]=0            
#gera a coluna com zeros e uns para cada questao

#q42
for i in respostaLC.index: 
    if(respostaLC[i][41] == gabaritoLC[i][41]):
        resultLCq42[i]=1
    else:
        resultLCq42[i]=0            
#gera a coluna com zeros e uns para cada questao

#q43
for i in respostaLC.index: 
    if(respostaLC[i][42] == gabaritoLC[i][42]):
        resultLCq43[i]=1
    else:
        resultLCq43[i]=0            
#gera a coluna com zeros e uns para cada questao

#q44
for i in respostaLC.index: 
    if(respostaLC[i][43] == gabaritoLC[i][43]):
        resultLCq44[i]=1
    else:
        resultLCq44[i]=0            
#gera a coluna com zeros e uns para cada questao

#q45
for i in respostaLC.index: 
    if(respostaLC[i][44] == gabaritoLC[i][44]):
        resultLCq45[i]=1
    else:
        resultLCq45[i]=0            
#gera a coluna com zeros e uns para cada questao

#q46
for i in respostaLC.index: 
    if(respostaLC[i][45] == gabaritoLC[i][45]):
        resultLCq46[i]=1
    else:
        resultLCq46[i]=0            
#gera a coluna com zeros e uns para cada questao

#q47
for i in respostaLC.index: 
    if(respostaLC[i][46] == gabaritoLC[i][46]):
        resultLCq47[i]=1
    else:
        resultLCq47[i]=0            
#gera a coluna com zeros e uns para cada questao

#q48
for i in respostaLC.index: 
    if(respostaLC[i][47] == gabaritoLC[i][47]):
        resultLCq48[i]=1
    else:
        resultLCq48[i]=0            
#gera a coluna com zeros e uns para cada questao

#q49
for i in respostaLC.index: 
    if(respostaLC[i][48] == gabaritoLC[i][48]):
        resultLCq49[i]=1
    else:
        resultLCq49[i]=0            
#gera a coluna com zeros e uns para cada questao

#q50
for i in respostaLC.index: 
    if(respostaLC[i][49] == gabaritoLC[i][49]):
        resultLCq50[i]=1
    else:
        resultLCq50[i]=0            
#gera a coluna com zeros e uns para cada questao


#definindo coluna de resultado para prova de Linguagens e códigos

dados['TX_Result_LC_questao1']=resultLCq1
dados['TX_Result_LC_questao2']=resultLCq2
dados['TX_Result_LC_questao3']=resultLCq3
dados['TX_Result_LC_questao4']=resultLCq4
dados['TX_Result_LC_questao5']=resultLCq5
dados['TX_Result_LC_questao6']=resultLCq6
dados['TX_Result_LC_questao7']=resultLCq7
dados['TX_Result_LC_questao8']=resultLCq8
dados['TX_Result_LC_questao9']=resultLCq9
dados['TX_Result_LC_questao10']=resultLCq10
dados['TX_Result_LC_questao11']=resultLCq11
dados['TX_Result_LC_questao12']=resultLCq12
dados['TX_Result_LC_questao13']=resultLCq13
dados['TX_Result_LC_questao14']=resultLCq14
dados['TX_Result_LC_questao15']=resultLCq15
dados['TX_Result_LC_questao16']=resultLCq16
dados['TX_Result_LC_questao17']=resultLCq17
dados['TX_Result_LC_questao18']=resultLCq18
dados['TX_Result_LC_questao19']=resultLCq19
dados['TX_Result_LC_questao20']=resultLCq20
dados['TX_Result_LC_questao21']=resultLCq21
dados['TX_Result_LC_questao22']=resultLCq22
dados['TX_Result_LC_questao23']=resultLCq23
dados['TX_Result_LC_questao24']=resultLCq24
dados['TX_Result_LC_questao25']=resultLCq25
dados['TX_Result_LC_questao26']=resultLCq26
dados['TX_Result_LC_questao27']=resultLCq27
dados['TX_Result_LC_questao28']=resultLCq28
dados['TX_Result_LC_questao29']=resultLCq29
dados['TX_Result_LC_questao30']=resultLCq30
dados['TX_Result_LC_questao31']=resultLCq31
dados['TX_Result_LC_questao32']=resultLCq32
dados['TX_Result_LC_questao33']=resultLCq33
dados['TX_Result_LC_questao34']=resultLCq34
dados['TX_Result_LC_questao35']=resultLCq35
dados['TX_Result_LC_questao36']=resultLCq36
dados['TX_Result_LC_questao37']=resultLCq37
dados['TX_Result_LC_questao38']=resultLCq38
dados['TX_Result_LC_questao39']=resultLCq39
dados['TX_Result_LC_questao40']=resultLCq40
dados['TX_Result_LC_questao41']=resultLCq41
dados['TX_Result_LC_questao42']=resultLCq42
dados['TX_Result_LC_questao43']=resultLCq43
dados['TX_Result_LC_questao44']=resultLCq44
dados['TX_Result_LC_questao45']=resultLCq45
dados['TX_Result_LC_questao46']=resultLCq46
dados['TX_Result_LC_questao47']=resultLCq47
dados['TX_Result_LC_questao48']=resultLCq48
dados['TX_Result_LC_questao49']=resultLCq49
dados['TX_Result_LC_questao50']=resultLCq50


# In[ ]:


#ROTINA PARA GERAR COLUNA DE ZEROS E UNS DE ACORDO COM RESPOSTA E GABARITO DE CADA ALUNO NA PROVA DE Matemática

resultMTq1=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq2=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq3=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq4=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq5=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq6=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq7=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq8=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq9=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq10=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq11=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq12=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq13=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq14=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq15=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq16=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq17=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq18=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq19=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq20=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq21=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq22=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq23=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq24=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq25=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq26=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq27=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq28=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq29=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq30=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq31=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq32=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq33=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq34=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq35=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq36=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq37=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq38=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq39=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq40=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq41=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq42=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq43=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq44=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas
resultMTq45=[[]* 1 for i in range(len(dados))] #Cria coluna de 1000 entradas


#q1
for i in respostaMT.index: 
    if(respostaMT[i][0] == gabaritoMT[i][0]):
        resultMTq1[i]=1
    else:
        resultMTq1[i]=0            
#gera a coluna com zeros e uns para cada questao

#q2
for i in respostaMT.index: 
    if(respostaMT[i][1] == gabaritoMT[i][1]):
        resultMTq2[i]=1
    else:
        resultMTq2[i]=0            
#gera a coluna com zeros e uns para cada questao

#q3
for i in respostaMT.index: 
    if(respostaMT[i][2] == gabaritoMT[i][2]):
        resultMTq3[i]=1
    else:
        resultMTq3[i]=0            
#gera a coluna com zeros e uns para cada questao

#q4
for i in respostaMT.index: 
    if(respostaMT[i][3] == gabaritoMT[i][3]):
        resultMTq4[i]=1
    else:
        resultMTq4[i]=0            
#gera a coluna com zeros e uns para cada questao

#q5
for i in respostaMT.index: 
    if(respostaMT[i][4] == gabaritoMT[i][4]):
        resultMTq5[i]=1
    else:
        resultMTq5[i]=0            
#gera a coluna com zeros e uns para cada questao

#q6
for i in respostaMT.index: 
    if(respostaMT[i][5] == gabaritoMT[i][5]):
        resultMTq6[i]=1
    else:
        resultMTq6[i]=0            
#gera a coluna com zeros e uns para cada questao

#q7
for i in respostaMT.index: 
    if(respostaMT[i][6] == gabaritoMT[i][6]):
        resultMTq7[i]=1
    else:
        resultMTq7[i]=0            
#gera a coluna com zeros e uns para cada questao

#q8
for i in respostaMT.index: 
    if(respostaMT[i][7] == gabaritoMT[i][7]):
        resultMTq8[i]=1
    else:
        resultMTq8[i]=0            
#gera a coluna com zeros e uns para cada questao

#q9
for i in respostaMT.index: 
    if(respostaMT[i][8] == gabaritoMT[i][8]):
        resultMTq9[i]=1
    else:
        resultMTq9[i]=0            
#gera a coluna com zeros e uns para cada questao

#q10
for i in respostaMT.index: 
    if(respostaMT[i][9] == gabaritoMT[i][9]):
        resultMTq10[i]=1
    else:
        resultMTq10[i]=0            
#gera a coluna com zeros e uns para cada questao

#q11
for i in respostaMT.index: 
    if(respostaMT[i][10] == gabaritoMT[i][10]):
        resultMTq11[i]=1
    else:
        resultMTq11[i]=0            
#gera a coluna com zeros e uns para cada questao

#q12
for i in respostaMT.index: 
    if(respostaMT[i][11] == gabaritoMT[i][11]):
        resultMTq12[i]=1
    else:
        resultMTq12[i]=0            
#gera a coluna com zeros e uns para cada questao

#q13
for i in respostaMT.index: 
    if(respostaMT[i][12] == gabaritoMT[i][12]):
        resultMTq13[i]=1
    else:
        resultMTq13[i]=0            
#gera a coluna com zeros e uns para cada questao

#q14
for i in respostaMT.index: 
    if(respostaMT[i][13] == gabaritoMT[i][13]):
        resultMTq14[i]=1
    else:
        resultMTq14[i]=0            
#gera a coluna com zeros e uns para cada questao

#q15
for i in respostaMT.index: 
    if(respostaMT[i][14] == gabaritoMT[i][14]):
        resultMTq15[i]=1
    else:
        resultMTq15[i]=0            
#gera a coluna com zeros e uns para cada questao

#q16
for i in respostaMT.index: 
    if(respostaMT[i][15] == gabaritoMT[i][15]):
        resultMTq16[i]=1
    else:
        resultMTq16[i]=0            
#gera a coluna com zeros e uns para cada questao

#q17
for i in respostaMT.index: 
    if(respostaMT[i][16] == gabaritoMT[i][16]):
        resultMTq17[i]=1
    else:
        resultMTq17[i]=0            
#gera a coluna com zeros e uns para cada questao

#q18
for i in respostaMT.index: 
    if(respostaMT[i][17] == gabaritoMT[i][17]):
        resultMTq18[i]=1
    else:
        resultMTq18[i]=0            
#gera a coluna com zeros e uns para cada questao

#q19
for i in respostaMT.index: 
    if(respostaMT[i][18] == gabaritoMT[i][18]):
        resultMTq19[i]=1
    else:
        resultMTq19[i]=0            
#gera a coluna com zeros e uns para cada questao

#q20
for i in respostaMT.index: 
    if(respostaMT[i][19] == gabaritoMT[i][19]):
        resultMTq20[i]=1
    else:
        resultMTq20[i]=0            
#gera a coluna com zeros e uns para cada questao

#q21
for i in respostaMT.index: 
    if(respostaMT[i][20] == gabaritoMT[i][20]):
        resultMTq21[i]=1
    else:
        resultMTq21[i]=0            
#gera a coluna com zeros e uns para cada questao

#q22
for i in respostaMT.index: 
    if(respostaMT[i][21] == gabaritoMT[i][21]):
        resultMTq22[i]=1
    else:
        resultMTq22[i]=0            
#gera a coluna com zeros e uns para cada questao

#q23
for i in respostaMT.index: 
    if(respostaMT[i][22] == gabaritoMT[i][22]):
        resultMTq23[i]=1
    else:
        resultMTq23[i]=0            
#gera a coluna com zeros e uns para cada questao

#q24
for i in respostaMT.index: 
    if(respostaMT[i][23] == gabaritoMT[i][23]):
        resultMTq24[i]=1
    else:
        resultMTq24[i]=0            
#gera a coluna com zeros e uns para cada questao

#q25
for i in respostaMT.index: 
    if(respostaMT[i][24] == gabaritoMT[i][24]):
        resultMTq25[i]=1
    else:
        resultMTq25[i]=0            
#gera a coluna com zeros e uns para cada questao

#q26
for i in respostaMT.index: 
    if(respostaMT[i][25] == gabaritoMT[i][25]):
        resultMTq26[i]=1
    else:
        resultMTq26[i]=0            
#gera a coluna com zeros e uns para cada questao

#q27
for i in respostaMT.index: 
    if(respostaMT[i][26] == gabaritoMT[i][26]):
        resultMTq27[i]=1
    else:
        resultMTq27[i]=0            
#gera a coluna com zeros e uns para cada questao

#q28
for i in respostaMT.index: 
    if(respostaMT[i][27] == gabaritoMT[i][27]):
        resultMTq28[i]=1
    else:
        resultMTq28[i]=0            
#gera a coluna com zeros e uns para cada questao

#q29
for i in respostaMT.index: 
    if(respostaMT[i][28] == gabaritoMT[i][28]):
        resultMTq29[i]=1
    else:
        resultMTq29[i]=0            
#gera a coluna com zeros e uns para cada questao

#q30
for i in respostaMT.index: 
    if(respostaMT[i][29] == gabaritoMT[i][29]):
        resultMTq30[i]=1
    else:
        resultMTq30[i]=0            
#gera a coluna com zeros e uns para cada questao

#q31
for i in respostaMT.index: 
    if(respostaMT[i][30] == gabaritoMT[i][30]):
        resultMTq31[i]=1
    else:
        resultMTq31[i]=0            
#gera a coluna com zeros e uns para cada questao

#q32
for i in respostaMT.index: 
    if(respostaMT[i][31] == gabaritoMT[i][31]):
        resultMTq32[i]=1
    else:
        resultMTq32[i]=0            
#gera a coluna com zeros e uns para cada questao

#q33
for i in respostaMT.index: 
    if(respostaMT[i][32] == gabaritoMT[i][32]):
        resultMTq33[i]=1
    else:
        resultMTq33[i]=0            
#gera a coluna com zeros e uns para cada questao

#q34
for i in respostaMT.index: 
    if(respostaMT[i][33] == gabaritoMT[i][33]):
        resultMTq34[i]=1
    else:
        resultMTq34[i]=0            
#gera a coluna com zeros e uns para cada questao

#q35
for i in respostaMT.index: 
    if(respostaMT[i][34] == gabaritoMT[i][34]):
        resultMTq35[i]=1
    else:
        resultMTq35[i]=0            
#gera a coluna com zeros e uns para cada questao

#q36
for i in respostaMT.index: 
    if(respostaMT[i][35] == gabaritoMT[i][35]):
        resultMTq36[i]=1
    else:
        resultMTq36[i]=0            
#gera a coluna com zeros e uns para cada questao

#q37
for i in respostaMT.index: 
    if(respostaMT[i][36] == gabaritoMT[i][36]):
        resultMTq37[i]=1
    else:
        resultMTq37[i]=0            
#gera a coluna com zeros e uns para cada questao

#q38
for i in respostaMT.index: 
    if(respostaMT[i][37] == gabaritoMT[i][37]):
        resultMTq38[i]=1
    else:
        resultMTq38[i]=0            
#gera a coluna com zeros e uns para cada questao

#q39
for i in respostaMT.index: 
    if(respostaMT[i][38] == gabaritoMT[i][38]):
        resultMTq39[i]=1
    else:
        resultMTq39[i]=0            
#gera a coluna com zeros e uns para cada questao

#q40
for i in respostaMT.index: 
    if(respostaMT[i][39] == gabaritoMT[i][39]):
        resultMTq40[i]=1
    else:
        resultMTq40[i]=0            
#gera a coluna com zeros e uns para cada questao

#q41
for i in respostaMT.index: 
    if(respostaMT[i][40] == gabaritoMT[i][40]):
        resultMTq41[i]=1
    else:
        resultMTq41[i]=0            
#gera a coluna com zeros e uns para cada questao

#q42
for i in respostaMT.index: 
    if(respostaMT[i][41] == gabaritoMT[i][41]):
        resultMTq42[i]=1
    else:
        resultMTq42[i]=0            
#gera a coluna com zeros e uns para cada questao

#q43
for i in respostaMT.index: 
    if(respostaMT[i][42] == gabaritoMT[i][42]):
        resultMTq43[i]=1
    else:
        resultMTq43[i]=0            
#gera a coluna com zeros e uns para cada questao

#q44
for i in respostaMT.index: 
    if(respostaMT[i][43] == gabaritoMT[i][43]):
        resultMTq44[i]=1
    else:
        resultMTq44[i]=0            
#gera a coluna com zeros e uns para cada questao

#q45
for i in respostaMT.index: 
    if(respostaMT[i][44] == gabaritoMT[i][44]):
        resultMTq45[i]=1
    else:
        resultMTq45[i]=0            
#gera a coluna com zeros e uns para cada questao



#definindo coluna de resultado para prova de Matemática

dados['TX_Result_MT_questao1']=resultMTq1
dados['TX_Result_MT_questao2']=resultMTq2
dados['TX_Result_MT_questao3']=resultMTq3
dados['TX_Result_MT_questao4']=resultMTq4
dados['TX_Result_MT_questao5']=resultMTq5
dados['TX_Result_MT_questao6']=resultMTq6
dados['TX_Result_MT_questao7']=resultMTq7
dados['TX_Result_MT_questao8']=resultMTq8
dados['TX_Result_MT_questao9']=resultMTq9
dados['TX_Result_MT_questao10']=resultMTq10
dados['TX_Result_MT_questao11']=resultMTq11
dados['TX_Result_MT_questao12']=resultMTq12
dados['TX_Result_MT_questao13']=resultMTq13
dados['TX_Result_MT_questao14']=resultMTq14
dados['TX_Result_MT_questao15']=resultMTq15
dados['TX_Result_MT_questao16']=resultMTq16
dados['TX_Result_MT_questao17']=resultMTq17
dados['TX_Result_MT_questao18']=resultMTq18
dados['TX_Result_MT_questao19']=resultMTq19
dados['TX_Result_MT_questao20']=resultMTq20
dados['TX_Result_MT_questao21']=resultMTq21
dados['TX_Result_MT_questao22']=resultMTq22
dados['TX_Result_MT_questao23']=resultMTq23
dados['TX_Result_MT_questao24']=resultMTq24
dados['TX_Result_MT_questao25']=resultMTq25
dados['TX_Result_MT_questao26']=resultMTq26
dados['TX_Result_MT_questao27']=resultMTq27
dados['TX_Result_MT_questao28']=resultMTq28
dados['TX_Result_MT_questao29']=resultMTq29
dados['TX_Result_MT_questao30']=resultMTq30
dados['TX_Result_MT_questao31']=resultMTq31
dados['TX_Result_MT_questao32']=resultMTq32
dados['TX_Result_MT_questao33']=resultMTq33
dados['TX_Result_MT_questao34']=resultMTq34
dados['TX_Result_MT_questao35']=resultMTq35
dados['TX_Result_MT_questao36']=resultMTq36
dados['TX_Result_MT_questao37']=resultMTq37
dados['TX_Result_MT_questao38']=resultMTq38
dados['TX_Result_MT_questao39']=resultMTq39
dados['TX_Result_MT_questao40']=resultMTq40
dados['TX_Result_MT_questao41']=resultMTq41
dados['TX_Result_MT_questao42']=resultMTq42
dados['TX_Result_MT_questao43']=resultMTq43
dados['TX_Result_MT_questao44']=resultMTq44
dados['TX_Result_MT_questao45']=resultMTq45


# In[ ]:


#Filtrando os dados pelo caderno azul

#prova de CN
cadAzulCN=dados.loc[dados.CO_PROVA_CN==391.0] #faz filtragem de dados com CO_PROVA_CN=391 azul

#prova de CH
cadAzulCH=dados.loc[dados.CO_PROVA_CH==395.0]#faz filtragem de dados com CO_PROVA_CH=395 azul

#prova de LC
cadAzulLC=dados.loc[dados.CO_PROVA_LC==399.0] #faz filtragem de dados com CO_PROVA_LC=399 azul

#prova de MT
cadAzulMT=dados.loc[dados.CO_PROVA_MT==403.0]#faz filtragem de dados com CO_PROVA_MT=403 azul


# In[ ]:


###  Calculando media de acertos em cada questão, na prova de CN ####

#Caderno Azul
mediaQ1CNaz=cadAzulCN.TX_Result_CN_questao1.mean()
mediaQ2CNaz=cadAzulCN.TX_Result_CN_questao2.mean()
mediaQ3CNaz=cadAzulCN.TX_Result_CN_questao3.mean()
mediaQ4CNaz=cadAzulCN.TX_Result_CN_questao4.mean()
mediaQ5CNaz=cadAzulCN.TX_Result_CN_questao5.mean()
mediaQ6CNaz=cadAzulCN.TX_Result_CN_questao6.mean()
mediaQ7CNaz=cadAzulCN.TX_Result_CN_questao7.mean()
mediaQ8CNaz=cadAzulCN.TX_Result_CN_questao8.mean()
mediaQ9CNaz=cadAzulCN.TX_Result_CN_questao9.mean()
mediaQ10CNaz=cadAzulCN.TX_Result_CN_questao10.mean()
mediaQ11CNaz=cadAzulCN.TX_Result_CN_questao11.mean()
mediaQ12CNaz=cadAzulCN.TX_Result_CN_questao12.mean()
mediaQ13CNaz=cadAzulCN.TX_Result_CN_questao13.mean()
mediaQ14CNaz=cadAzulCN.TX_Result_CN_questao14.mean()
mediaQ15CNaz=cadAzulCN.TX_Result_CN_questao15.mean()
mediaQ16CNaz=cadAzulCN.TX_Result_CN_questao16.mean()
mediaQ17CNaz=cadAzulCN.TX_Result_CN_questao17.mean()
mediaQ18CNaz=cadAzulCN.TX_Result_CN_questao18.mean()
mediaQ19CNaz=cadAzulCN.TX_Result_CN_questao19.mean()
mediaQ20CNaz=cadAzulCN.TX_Result_CN_questao20.mean()
mediaQ21CNaz=cadAzulCN.TX_Result_CN_questao21.mean()
mediaQ22CNaz=cadAzulCN.TX_Result_CN_questao22.mean()
mediaQ23CNaz=cadAzulCN.TX_Result_CN_questao23.mean()
mediaQ24CNaz=cadAzulCN.TX_Result_CN_questao24.mean()
mediaQ25CNaz=cadAzulCN.TX_Result_CN_questao25.mean()
mediaQ26CNaz=cadAzulCN.TX_Result_CN_questao26.mean()
mediaQ27CNaz=cadAzulCN.TX_Result_CN_questao27.mean()
mediaQ28CNaz=cadAzulCN.TX_Result_CN_questao28.mean()
mediaQ29CNaz=cadAzulCN.TX_Result_CN_questao29.mean()
mediaQ30CNaz=cadAzulCN.TX_Result_CN_questao30.mean()
mediaQ31CNaz=cadAzulCN.TX_Result_CN_questao31.mean()
mediaQ32CNaz=cadAzulCN.TX_Result_CN_questao32.mean()
mediaQ33CNaz=cadAzulCN.TX_Result_CN_questao33.mean()
mediaQ34CNaz=cadAzulCN.TX_Result_CN_questao34.mean()
mediaQ35CNaz=cadAzulCN.TX_Result_CN_questao35.mean()
mediaQ36CNaz=cadAzulCN.TX_Result_CN_questao36.mean()
mediaQ37CNaz=cadAzulCN.TX_Result_CN_questao37.mean()
mediaQ38CNaz=cadAzulCN.TX_Result_CN_questao38.mean()
mediaQ39CNaz=cadAzulCN.TX_Result_CN_questao39.mean()
mediaQ40CNaz=cadAzulCN.TX_Result_CN_questao40.mean()
mediaQ41CNaz=cadAzulCN.TX_Result_CN_questao41.mean()
mediaQ42CNaz=cadAzulCN.TX_Result_CN_questao42.mean()
mediaQ43CNaz=cadAzulCN.TX_Result_CN_questao43.mean()
mediaQ44CNaz=cadAzulCN.TX_Result_CN_questao44.mean()
mediaQ45CNaz=cadAzulCN.TX_Result_CN_questao45.mean()


# In[ ]:


#Printando as medias de CN, caderno azul
print(mediaQ1CNaz*100,
mediaQ2CNaz*100,
mediaQ3CNaz*100,
mediaQ4CNaz*100,
mediaQ5CNaz*100,
mediaQ6CNaz*100,
mediaQ7CNaz*100,
mediaQ8CNaz*100,
mediaQ9CNaz*100,
mediaQ10CNaz*100,
mediaQ11CNaz*100,
mediaQ12CNaz*100,
mediaQ13CNaz*100,
mediaQ14CNaz*100,
mediaQ15CNaz*100,
mediaQ16CNaz*100,
mediaQ17CNaz*100,
mediaQ18CNaz*100,
mediaQ19CNaz*100,
mediaQ20CNaz*100,
mediaQ21CNaz*100,
mediaQ22CNaz*100,
mediaQ23CNaz*100,
mediaQ24CNaz*100,
mediaQ25CNaz*100,
mediaQ26CNaz*100,
mediaQ27CNaz*100,
mediaQ28CNaz*100,
mediaQ29CNaz*100,
mediaQ30CNaz*100,
mediaQ31CNaz*100,
mediaQ32CNaz*100,
mediaQ33CNaz*100,
mediaQ34CNaz*100,
mediaQ35CNaz*100,
mediaQ36CNaz*100,
mediaQ37CNaz*100,
mediaQ38CNaz*100,
mediaQ39CNaz*100,
mediaQ40CNaz*100,
mediaQ41CNaz*100,
mediaQ42CNaz*100,
mediaQ43CNaz*100,
mediaQ44CNaz*100,
mediaQ45CNaz*100)


# In[ ]:


###  Calculando media de acertos em cada questão, na prova de CH ####

#Caderno Azul
mediaQ1CHaz=cadAzulCH.TX_Result_CH_questao1.mean()
mediaQ2CHaz=cadAzulCH.TX_Result_CH_questao2.mean()
mediaQ3CHaz=cadAzulCH.TX_Result_CH_questao3.mean()
mediaQ4CHaz=cadAzulCH.TX_Result_CH_questao4.mean()
mediaQ5CHaz=cadAzulCH.TX_Result_CH_questao5.mean()
mediaQ6CHaz=cadAzulCH.TX_Result_CH_questao6.mean()
mediaQ7CHaz=cadAzulCH.TX_Result_CH_questao7.mean()
mediaQ8CHaz=cadAzulCH.TX_Result_CH_questao8.mean()
mediaQ9CHaz=cadAzulCH.TX_Result_CH_questao9.mean()
mediaQ10CHaz=cadAzulCH.TX_Result_CH_questao10.mean()
mediaQ11CHaz=cadAzulCH.TX_Result_CH_questao11.mean()
mediaQ12CHaz=cadAzulCH.TX_Result_CH_questao12.mean()
mediaQ13CHaz=cadAzulCH.TX_Result_CH_questao13.mean()
mediaQ14CHaz=cadAzulCH.TX_Result_CH_questao14.mean()
mediaQ15CHaz=cadAzulCH.TX_Result_CH_questao15.mean()
mediaQ16CHaz=cadAzulCH.TX_Result_CH_questao16.mean()
mediaQ17CHaz=cadAzulCH.TX_Result_CH_questao17.mean()
mediaQ18CHaz=cadAzulCH.TX_Result_CH_questao18.mean()
mediaQ19CHaz=cadAzulCH.TX_Result_CH_questao19.mean()
mediaQ20CHaz=cadAzulCH.TX_Result_CH_questao20.mean()
mediaQ21CHaz=cadAzulCH.TX_Result_CH_questao21.mean()
mediaQ22CHaz=cadAzulCH.TX_Result_CH_questao22.mean()
mediaQ23CHaz=cadAzulCH.TX_Result_CH_questao23.mean()
mediaQ24CHaz=cadAzulCH.TX_Result_CH_questao24.mean()
mediaQ25CHaz=cadAzulCH.TX_Result_CH_questao25.mean()
mediaQ26CHaz=cadAzulCH.TX_Result_CH_questao26.mean()
mediaQ27CHaz=cadAzulCH.TX_Result_CH_questao27.mean()
mediaQ28CHaz=cadAzulCH.TX_Result_CH_questao28.mean()
mediaQ29CHaz=cadAzulCH.TX_Result_CH_questao29.mean()
mediaQ30CHaz=cadAzulCH.TX_Result_CH_questao30.mean()
mediaQ31CHaz=cadAzulCH.TX_Result_CH_questao31.mean()
mediaQ32CHaz=cadAzulCH.TX_Result_CH_questao32.mean()
mediaQ33CHaz=cadAzulCH.TX_Result_CH_questao33.mean()
mediaQ34CHaz=cadAzulCH.TX_Result_CH_questao34.mean()
mediaQ35CHaz=cadAzulCH.TX_Result_CH_questao35.mean()
mediaQ36CHaz=cadAzulCH.TX_Result_CH_questao36.mean()
mediaQ37CHaz=cadAzulCH.TX_Result_CH_questao37.mean()
mediaQ38CHaz=cadAzulCH.TX_Result_CH_questao38.mean()
mediaQ39CHaz=cadAzulCH.TX_Result_CH_questao39.mean()
mediaQ40CHaz=cadAzulCH.TX_Result_CH_questao40.mean()
mediaQ41CHaz=cadAzulCH.TX_Result_CH_questao41.mean()
mediaQ42CHaz=cadAzulCH.TX_Result_CH_questao42.mean()
mediaQ43CHaz=cadAzulCH.TX_Result_CH_questao43.mean()
mediaQ44CHaz=cadAzulCH.TX_Result_CH_questao44.mean()
mediaQ45CHaz=cadAzulCH.TX_Result_CH_questao45.mean()


# In[ ]:


#Printando as medias de CH, caderno azul
print(mediaQ1CHaz*100,
mediaQ2CHaz*100,
mediaQ3CHaz*100,
mediaQ4CHaz*100,
mediaQ5CHaz*100,
mediaQ6CHaz*100,
mediaQ7CHaz*100,
mediaQ8CHaz*100,
mediaQ9CHaz*100,
mediaQ10CHaz*100,
mediaQ11CHaz*100,
mediaQ12CHaz*100,
mediaQ13CHaz*100,
mediaQ14CHaz*100,
mediaQ15CHaz*100,
mediaQ16CHaz*100,
mediaQ17CHaz*100,
mediaQ18CHaz*100,
mediaQ19CHaz*100,
mediaQ20CHaz*100,
mediaQ21CHaz*100,
mediaQ22CHaz*100,
mediaQ23CHaz*100,
mediaQ24CHaz*100,
mediaQ25CHaz*100,
mediaQ26CHaz*100,
mediaQ27CHaz*100,
mediaQ28CHaz*100,
mediaQ29CHaz*100,
mediaQ30CHaz*100,
mediaQ31CHaz*100,
mediaQ32CHaz*100,
mediaQ33CHaz*100,
mediaQ34CHaz*100,
mediaQ35CHaz*100,
mediaQ36CHaz*100,
mediaQ37CHaz*100,
mediaQ38CHaz*100,
mediaQ39CHaz*100,
mediaQ40CHaz*100,
mediaQ41CHaz*100,
mediaQ42CHaz*100,
mediaQ43CHaz*100,
mediaQ44CHaz*100,
mediaQ45CHaz*100)


# In[ ]:


###  Calculando media de acertos em cada questão, na prova de LC ####

#Caderno Azul
mediaQ1LCaz=cadAzulLC.TX_Result_LC_questao1.mean()
mediaQ2LCaz=cadAzulLC.TX_Result_LC_questao2.mean()
mediaQ3LCaz=cadAzulLC.TX_Result_LC_questao3.mean()
mediaQ4LCaz=cadAzulLC.TX_Result_LC_questao4.mean()
mediaQ5LCaz=cadAzulLC.TX_Result_LC_questao5.mean()
mediaQ6LCaz=cadAzulLC.TX_Result_LC_questao6.mean()
mediaQ7LCaz=cadAzulLC.TX_Result_LC_questao7.mean()
mediaQ8LCaz=cadAzulLC.TX_Result_LC_questao8.mean()
mediaQ9LCaz=cadAzulLC.TX_Result_LC_questao9.mean()
mediaQ10LCaz=cadAzulLC.TX_Result_LC_questao10.mean()
mediaQ11LCaz=cadAzulLC.TX_Result_LC_questao11.mean()
mediaQ12LCaz=cadAzulLC.TX_Result_LC_questao12.mean()
mediaQ13LCaz=cadAzulLC.TX_Result_LC_questao13.mean()
mediaQ14LCaz=cadAzulLC.TX_Result_LC_questao14.mean()
mediaQ15LCaz=cadAzulLC.TX_Result_LC_questao15.mean()
mediaQ16LCaz=cadAzulLC.TX_Result_LC_questao16.mean()
mediaQ17LCaz=cadAzulLC.TX_Result_LC_questao17.mean()
mediaQ18LCaz=cadAzulLC.TX_Result_LC_questao18.mean()
mediaQ19LCaz=cadAzulLC.TX_Result_LC_questao19.mean()
mediaQ20LCaz=cadAzulLC.TX_Result_LC_questao20.mean()
mediaQ21LCaz=cadAzulLC.TX_Result_LC_questao21.mean()
mediaQ22LCaz=cadAzulLC.TX_Result_LC_questao22.mean()
mediaQ23LCaz=cadAzulLC.TX_Result_LC_questao23.mean()
mediaQ24LCaz=cadAzulLC.TX_Result_LC_questao24.mean()
mediaQ25LCaz=cadAzulLC.TX_Result_LC_questao25.mean()
mediaQ26LCaz=cadAzulLC.TX_Result_LC_questao26.mean()
mediaQ27LCaz=cadAzulLC.TX_Result_LC_questao27.mean()
mediaQ28LCaz=cadAzulLC.TX_Result_LC_questao28.mean()
mediaQ29LCaz=cadAzulLC.TX_Result_LC_questao29.mean()
mediaQ30LCaz=cadAzulLC.TX_Result_LC_questao30.mean()
mediaQ31LCaz=cadAzulLC.TX_Result_LC_questao31.mean()
mediaQ32LCaz=cadAzulLC.TX_Result_LC_questao32.mean()
mediaQ33LCaz=cadAzulLC.TX_Result_LC_questao33.mean()
mediaQ34LCaz=cadAzulLC.TX_Result_LC_questao34.mean()
mediaQ35LCaz=cadAzulLC.TX_Result_LC_questao35.mean()
mediaQ36LCaz=cadAzulLC.TX_Result_LC_questao36.mean()
mediaQ37LCaz=cadAzulLC.TX_Result_LC_questao37.mean()
mediaQ38LCaz=cadAzulLC.TX_Result_LC_questao38.mean()
mediaQ39LCaz=cadAzulLC.TX_Result_LC_questao39.mean()
mediaQ40LCaz=cadAzulLC.TX_Result_LC_questao40.mean()
mediaQ41LCaz=cadAzulLC.TX_Result_LC_questao41.mean()
mediaQ42LCaz=cadAzulLC.TX_Result_LC_questao42.mean()
mediaQ43LCaz=cadAzulLC.TX_Result_LC_questao43.mean()
mediaQ44LCaz=cadAzulLC.TX_Result_LC_questao44.mean()
mediaQ45LCaz=cadAzulLC.TX_Result_LC_questao45.mean()
mediaQ46LCaz=cadAzulLC.TX_Result_LC_questao46.mean()
mediaQ47LCaz=cadAzulLC.TX_Result_LC_questao47.mean()
mediaQ48LCaz=cadAzulLC.TX_Result_LC_questao48.mean()
mediaQ49LCaz=cadAzulLC.TX_Result_LC_questao49.mean()
mediaQ50LCaz=cadAzulLC.TX_Result_LC_questao50.mean()


# In[ ]:


#Printando as medias de LC, caderno azul
print(mediaQ1LCaz*100,
mediaQ2LCaz*100,
mediaQ3LCaz*100,
mediaQ4LCaz*100,
mediaQ5LCaz*100,
mediaQ6LCaz*100,
mediaQ7LCaz*100,
mediaQ8LCaz*100,
mediaQ9LCaz*100,
mediaQ10LCaz*100,
mediaQ11LCaz*100,
mediaQ12LCaz*100,
mediaQ13LCaz*100,
mediaQ14LCaz*100,
mediaQ15LCaz*100,
mediaQ16LCaz*100,
mediaQ17LCaz*100,
mediaQ18LCaz*100,
mediaQ19LCaz*100,
mediaQ20LCaz*100,
mediaQ21LCaz*100,
mediaQ22LCaz*100,
mediaQ23LCaz*100,
mediaQ24LCaz*100,
mediaQ25LCaz*100,
mediaQ26LCaz*100,
mediaQ27LCaz*100,
mediaQ28LCaz*100,
mediaQ29LCaz*100,
mediaQ30LCaz*100,
mediaQ31LCaz*100,
mediaQ32LCaz*100,
mediaQ33LCaz*100,
mediaQ34LCaz*100,
mediaQ35LCaz*100,
mediaQ36LCaz*100,
mediaQ37LCaz*100,
mediaQ38LCaz*100,
mediaQ39LCaz*100,
mediaQ40LCaz*100,
mediaQ41LCaz*100,
mediaQ42LCaz*100,
mediaQ43LCaz*100,
mediaQ44LCaz*100,
mediaQ45LCaz*100,
mediaQ46LCaz*100,
mediaQ47LCaz*100,
mediaQ48LCaz*100,
mediaQ49LCaz*100,
mediaQ50LCaz*100)


# In[ ]:





# In[ ]:


###  Calculando media de acertos em cada questão, na prova de MT ####

#Caderno Azul
mediaQ1MTaz=cadAzulMT.TX_Result_MT_questao1.mean()
mediaQ2MTaz=cadAzulMT.TX_Result_MT_questao2.mean()
mediaQ3MTaz=cadAzulMT.TX_Result_MT_questao3.mean()
mediaQ4MTaz=cadAzulMT.TX_Result_MT_questao4.mean()
mediaQ5MTaz=cadAzulMT.TX_Result_MT_questao5.mean()
mediaQ6MTaz=cadAzulMT.TX_Result_MT_questao6.mean()
mediaQ7MTaz=cadAzulMT.TX_Result_MT_questao7.mean()
mediaQ8MTaz=cadAzulMT.TX_Result_MT_questao8.mean()
mediaQ9MTaz=cadAzulMT.TX_Result_MT_questao9.mean()
mediaQ10MTaz=cadAzulMT.TX_Result_MT_questao10.mean()
mediaQ11MTaz=cadAzulMT.TX_Result_MT_questao11.mean()
mediaQ12MTaz=cadAzulMT.TX_Result_MT_questao12.mean()
mediaQ13MTaz=cadAzulMT.TX_Result_MT_questao13.mean()
mediaQ14MTaz=cadAzulMT.TX_Result_MT_questao14.mean()
mediaQ15MTaz=cadAzulMT.TX_Result_MT_questao15.mean()
mediaQ16MTaz=cadAzulMT.TX_Result_MT_questao16.mean()
mediaQ17MTaz=cadAzulMT.TX_Result_MT_questao17.mean()
mediaQ18MTaz=cadAzulMT.TX_Result_MT_questao18.mean()
mediaQ19MTaz=cadAzulMT.TX_Result_MT_questao19.mean()
mediaQ20MTaz=cadAzulMT.TX_Result_MT_questao20.mean()
mediaQ21MTaz=cadAzulMT.TX_Result_MT_questao21.mean()
mediaQ22MTaz=cadAzulMT.TX_Result_MT_questao22.mean()
mediaQ23MTaz=cadAzulMT.TX_Result_MT_questao23.mean()
mediaQ24MTaz=cadAzulMT.TX_Result_MT_questao24.mean()
mediaQ25MTaz=cadAzulMT.TX_Result_MT_questao25.mean()
mediaQ26MTaz=cadAzulMT.TX_Result_MT_questao26.mean()
mediaQ27MTaz=cadAzulMT.TX_Result_MT_questao27.mean()
mediaQ28MTaz=cadAzulMT.TX_Result_MT_questao28.mean()
mediaQ29MTaz=cadAzulMT.TX_Result_MT_questao29.mean()
mediaQ30MTaz=cadAzulMT.TX_Result_MT_questao30.mean()
mediaQ31MTaz=cadAzulMT.TX_Result_MT_questao31.mean()
mediaQ32MTaz=cadAzulMT.TX_Result_MT_questao32.mean()
mediaQ33MTaz=cadAzulMT.TX_Result_MT_questao33.mean()
mediaQ34MTaz=cadAzulMT.TX_Result_MT_questao34.mean()
mediaQ35MTaz=cadAzulMT.TX_Result_MT_questao35.mean()
mediaQ36MTaz=cadAzulMT.TX_Result_MT_questao36.mean()
mediaQ37MTaz=cadAzulMT.TX_Result_MT_questao37.mean()
mediaQ38MTaz=cadAzulMT.TX_Result_MT_questao38.mean()
mediaQ39MTaz=cadAzulMT.TX_Result_MT_questao39.mean()
mediaQ40MTaz=cadAzulMT.TX_Result_MT_questao40.mean()
mediaQ41MTaz=cadAzulMT.TX_Result_MT_questao41.mean()
mediaQ42MTaz=cadAzulMT.TX_Result_MT_questao42.mean()
mediaQ43MTaz=cadAzulMT.TX_Result_MT_questao43.mean()
mediaQ44MTaz=cadAzulMT.TX_Result_MT_questao44.mean()
mediaQ45MTaz=cadAzulMT.TX_Result_MT_questao45.mean()


# In[ ]:


#Printando as medias de MT, caderno azul
print(mediaQ1MTaz*100,
mediaQ2MTaz*100,
mediaQ3MTaz*100,
mediaQ4MTaz*100,
mediaQ5MTaz*100,
mediaQ6MTaz*100,
mediaQ7MTaz*100,
mediaQ8MTaz*100,
mediaQ9MTaz*100,
mediaQ10MTaz*100,
mediaQ11MTaz*100,
mediaQ12MTaz*100,
mediaQ13MTaz*100,
mediaQ14MTaz*100,
mediaQ15MTaz*100,
mediaQ16MTaz*100,
mediaQ17MTaz*100,
mediaQ18MTaz*100,
mediaQ19MTaz*100,
mediaQ20MTaz*100,
mediaQ21MTaz*100,
mediaQ22MTaz*100,
mediaQ23MTaz*100,
mediaQ24MTaz*100,
mediaQ25MTaz*100,
mediaQ26MTaz*100,
mediaQ27MTaz*100,
mediaQ28MTaz*100,
mediaQ29MTaz*100,
mediaQ30MTaz*100,
mediaQ31MTaz*100,
mediaQ32MTaz*100,
mediaQ33MTaz*100,
mediaQ34MTaz*100,
mediaQ35MTaz*100,
mediaQ36MTaz*100,
mediaQ37MTaz*100,
mediaQ38MTaz*100,
mediaQ39MTaz*100,
mediaQ40MTaz*100,
mediaQ41MTaz*100,
mediaQ42MTaz*100,
mediaQ43MTaz*100,
mediaQ44MTaz*100,
mediaQ45MTaz*100)


# In[ ]:


#abstraindo as medias de notas dos inscritos nas provas

         #CIÊNCIAS DA NATUREZA
notasCN=dados.NU_NOTA_CN
#eliminando os dados nulos nela
notasCN.dropna(inplace=True)
mediaCN=notasCN.mean()

        #CIÊNCIAS HUMANAS
notasCH=dados.NU_NOTA_CH
#eliminando os dados nulos nela
notasCH.dropna(inplace=True)
mediaCH=notasCH.mean()

        #LINGUAGENS E CÓDIGOS
notasLC=dados.NU_NOTA_LC
#eliminando os dados nulos nela
notasLC.dropna(inplace=True)
mediaLC=notasLC.mean()

        #MATEMÁTICA
notasMT=dados.NU_NOTA_MT
#eliminando os dados nulos nela
notasMT.dropna(inplace=True)
mediaMT=notasMT.mean()

print(mediaCN,mediaCH,mediaLC,mediaMT)


# In[ ]:


#FILTRANDO AS COLUNAS PELOS ESTADOS BRASILEIROS E TIRANDO A MÉDIA DE NOTAS EM CADA UM


#São Paulo
SP=dados.loc[dados.SG_UF_RESIDENCIA=="SP"]
    #medias nas 4 partes da prova
mediaSPcn=SP.NU_NOTA_CN.mean()
mediaSPch=SP.NU_NOTA_CH.mean()
mediaSPlc=SP.NU_NOTA_LC.mean()
mediaSPmt=SP.NU_NOTA_MT.mean()

#Rio de Janeiro
RJ=dados.loc[dados.SG_UF_RESIDENCIA=="RJ"]
    #medias nas 4 partes da prova
mediaRJcn=RJ.NU_NOTA_CN.mean()
mediaRJch=RJ.NU_NOTA_CH.mean()
mediaRJlc=RJ.NU_NOTA_LC.mean()
mediaRJmt=RJ.NU_NOTA_MT.mean()


#Minas Gerais
MG=dados.loc[dados.SG_UF_RESIDENCIA=="MG"]
    #medias nas 4 partes da prova
mediaMGcn=MG.NU_NOTA_CN.mean()
mediaMGch=MG.NU_NOTA_CH.mean()
mediaMGlc=MG.NU_NOTA_LC.mean()
mediaMGmt=MG.NU_NOTA_MT.mean()


#Goiás
GO=dados.loc[dados.SG_UF_RESIDENCIA=="GO"]
    #medias nas 4 partes da prova
mediaGOcn=GO.NU_NOTA_CN.mean()
mediaGOch=GO.NU_NOTA_CH.mean()
mediaGOlc=GO.NU_NOTA_LC.mean()
mediaGOmt=GO.NU_NOTA_MT.mean()

#Mato Grosso
MT=dados.loc[dados.SG_UF_RESIDENCIA=="MT"]
    #medias nas 4 partes da prova
mediaMTcn=MT.NU_NOTA_CN.mean()
mediaMTch=MT.NU_NOTA_CH.mean()
mediaMTlc=MT.NU_NOTA_LC.mean()
mediaMTmt=MT.NU_NOTA_MT.mean()

#Amazonas
AM=dados.loc[dados.SG_UF_RESIDENCIA=="AM"]
    #medias nas 4 partes da prova
mediaAMcn=AM.NU_NOTA_CN.mean()
mediaAMch=AM.NU_NOTA_CH.mean()
mediaAMlc=AM.NU_NOTA_LC.mean()
mediaAMmt=AM.NU_NOTA_MT.mean()

#Rondônia
RO=dados.loc[dados.SG_UF_RESIDENCIA=="RO"]
    #medias nas 4 partes da prova
mediaROcn=RO.NU_NOTA_CN.mean()
mediaROch=RO.NU_NOTA_CH.mean()
mediaROlc=RO.NU_NOTA_LC.mean()
mediaROmt=RO.NU_NOTA_MT.mean()

#Rio Grande do Sul
RS=dados.loc[dados.SG_UF_RESIDENCIA=="RS"]
    #medias nas 4 partes da prova
mediaRScn=RS.NU_NOTA_CN.mean()
mediaRSch=RS.NU_NOTA_CH.mean()
mediaRSlc=RS.NU_NOTA_LC.mean()
mediaRSmt=RS.NU_NOTA_MT.mean()

#Paraná
PR=dados.loc[dados.SG_UF_RESIDENCIA=="PR"]
    #medias nas 4 partes da prova
mediaPRcn=PR.NU_NOTA_CN.mean()
mediaPRch=PR.NU_NOTA_CH.mean()
mediaPRlc=PR.NU_NOTA_LC.mean()
mediaPRmt=PR.NU_NOTA_MT.mean()

#Pará
PA=dados.loc[dados.SG_UF_RESIDENCIA=="PA"]
    #medias nas 4 partes da prova
mediaPAcn=PA.NU_NOTA_CN.mean()
mediaPAch=PA.NU_NOTA_CH.mean()
mediaPAlc=PA.NU_NOTA_LC.mean()
mediaPAmt=PA.NU_NOTA_MT.mean()

#Maranhão
MA=dados.loc[dados.SG_UF_RESIDENCIA=="MA"]
    #medias nas 4 partes da prova
mediaMAcn=MA.NU_NOTA_CN.mean()
mediaMAch=MA.NU_NOTA_CH.mean()
mediaMAlc=MA.NU_NOTA_LC.mean()
mediaMAmt=MA.NU_NOTA_MT.mean()

#Bahia
BA=dados.loc[dados.SG_UF_RESIDENCIA=="BA"]
    #medias nas 4 partes da prova
mediaBAcn=BA.NU_NOTA_CN.mean()
mediaBAch=BA.NU_NOTA_CH.mean()
mediaBAlc=BA.NU_NOTA_LC.mean()
mediaBAmt=BA.NU_NOTA_MT.mean()

#Ceará
CE=dados.loc[dados.SG_UF_RESIDENCIA=="CE"]
    #medias nas 4 partes da prova
mediaCEcn=CE.NU_NOTA_CN.mean()
mediaCEch=CE.NU_NOTA_CH.mean()
mediaCElc=CE.NU_NOTA_LC.mean()
mediaCEmt=CE.NU_NOTA_MT.mean()

#Sergipe
SE=dados.loc[dados.SG_UF_RESIDENCIA=="SE"]
    #medias nas 4 partes da prova
mediaSEcn=SE.NU_NOTA_CN.mean()
mediaSEch=SE.NU_NOTA_CH.mean()
mediaSElc=SE.NU_NOTA_LC.mean()
mediaSEmt=SE.NU_NOTA_MT.mean()


#dados.SG_UF_RESIDENCIA.describe()


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


#Obtendo Valores de Notas Máximas e Mínimas

##Aqui podemos fazer de duas formas:  1) com a função max() e min()
                                    # 2) com a função describe() que informa valores máximos, mínimos e etc

        #CIÊNCIAS DA NATUREZA  
minCN=dados.NU_NOTA_CN.dropna().min()
maxCN=dados.NU_NOTA_CN.dropna().max()

        #CIÊNCIAS HUMANAS
minCH=dados.NU_NOTA_CH.dropna().min()
maxCH=dados.NU_NOTA_CH.dropna().max()

        #LINGUAGENS E CÓDIGOS
minLC=dados.NU_NOTA_LC.dropna().min()
maxLC=dados.NU_NOTA_LC.dropna().max()
    
        #MATEMÁTICA 
minMT=dados.NU_NOTA_LC.dropna().min()
maxMT=dados.NU_NOTA_LC.dropna().max()


#COM DESCRIBE
cnd=dados.NU_NOTA_CN.describe()
chd=dados.NU_NOTA_CH.describe()
lcd=dados.NU_NOTA_LC.describe()
mtd=dados.NU_NOTA_MT.describe()


# In[ ]:


#Filtrando os dados por genero, raça, renda e tipo de escola


#Pelo Gênero
generoM=dados.loc[dados.TP_SEXO=='M'] #faz filtragem de dados para sexo masculino
generoF=dados.loc[dados.TP_SEXO=='F'] #faz filtragem de dados para sexo feminino

#Pela raça
raça0=dados.loc[dados.TP_COR_RACA== 0] #faz filtragem de dados para raça não declarada
raça1=dados.loc[dados.TP_COR_RACA== 1] #faz filtragem de dados para raça branca
raça2=dados.loc[dados.TP_COR_RACA== 2] #faz filtragem de dados para raça preta
raça3=dados.loc[dados.TP_COR_RACA== 3] #faz filtragem de dados para raça parda
raça4=dados.loc[dados.TP_COR_RACA== 4] #faz filtragem de dados para raça amarela
raça5=dados.loc[dados.TP_COR_RACA== 5] #faz filtragem de dados para raça indígena

#Pela renda
rendaA=dados.loc[dados.Q006== 'A'] #faz filtragem de dados para renda zero
rendaB=dados.loc[dados.Q006== 'B'] 
rendaC=dados.loc[dados.Q006== 'C']
rendaD=dados.loc[dados.Q006== 'D'] 
rendaE=dados.loc[dados.Q006== 'E'] 
rendaF=dados.loc[dados.Q006== 'F'] 
rendaG=dados.loc[dados.Q006== 'G'] 
rendaH=dados.loc[dados.Q006== 'H'] 
rendaI=dados.loc[dados.Q006== 'I'] 
rendaJ=dados.loc[dados.Q006== 'J'] 
rendaK=dados.loc[dados.Q006== 'K'] 
rendaL=dados.loc[dados.Q006== 'L'] 
rendaM=dados.loc[dados.Q006== 'M'] 
rendaN=dados.loc[dados.Q006== 'N'] 
rendaO=dados.loc[dados.Q006== 'O'] 
rendaP=dados.loc[dados.Q006== 'P'] 
rendaQ=dados.loc[dados.Q006== 'Q'] #faz filtragem de dados para renda mais de 18740

#por tipo de escola
escola1=dados.loc[dados.TP_ESCOLA==1] #faz filtragem de dados para escola não respondida
escola2=dados.loc[dados.TP_ESCOLA==2] #faz filtragem de dados para escola publica
escola3=dados.loc[dados.TP_ESCOLA==3] #faz filtragem de dados para escola privada
escola4=dados.loc[dados.TP_ESCOLA==4] #faz filtragem de dados para escola exterior



# In[ ]:


print(rendaK.NU_NOTA_CN.mean(),
rendaK.NU_NOTA_CH.mean(),
rendaK.NU_NOTA_LC.mean(),
rendaK.NU_NOTA_MT.mean())


# In[ ]:


print(rendaP.NU_NOTA_CN.mean(),
rendaP.NU_NOTA_CH.mean(),
rendaP.NU_NOTA_LC.mean(),
rendaP.NU_NOTA_MT.mean())


# In[ ]:


rendaQ.NU_NOTA_CN.describe()


# In[ ]:


rendaQ.NU_NOTA_CH.describe()


# In[ ]:


rendaQ.NU_NOTA_LC.describe()


# In[ ]:


rendaQ.NU_NOTA_MT.describe()


# In[ ]:





# In[ ]:


#Distribuição de notas em Ciências naturais
plt.hist(dados.NU_NOTA_CN, color="green",bins=50)#,marker='.' )
plt.title("Notas em Ciências da Natureza")
#x_axis('off')
#plt.axis([0, 1000, 0, 10000])
#plt.gca().invert_xaxis()
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:


#Distribuição de notas em Ciências humanas
plt.hist(notasCH, color="red", bins=50)#marker='.')
plt.title("Notas em Ciências Humanas")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas ")
plt.grid(True)
plt.show()


# In[ ]:


#Distribuição de notas em Linguagens e Códigos
plt.hist(notasLC, color="black",bins=50)#,marker='.' )
plt.title("Notas em Linguagens e Códigos")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:


#Distribuição de notas em Matemática
plt.hist(notasMT, color="blue", bins=50)# marker='.')
plt.title("Notas em Matemática")
plt.ylabel("Parcela de Inscritos")
plt.xlabel("Valores das Notas")
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:


#Fazendo a filtragem com o 1% maiores notas

#enem[campo_nota] >= enem[campo_nota].quantile(.99)
#enem_temp = enem[ enem[campo_nota] >= enem[campo_nota].quantile(.99) ]

dados.index = range(len(dados.index))


cn1cento= dados[dados['NU_NOTA_CN']>= dados['NU_NOTA_CN'].quantile(.99)]
ch1cento= dados[dados['NU_NOTA_CH']>= dados['NU_NOTA_CH'].quantile(.99)]
lc1cento= dados[dados['NU_NOTA_LC']>= dados['NU_NOTA_LC'].quantile(.99)]
mt1cento= dados[dados['NU_NOTA_MT']>= dados['NU_NOTA_MT'].quantile(.99)]


# In[ ]:


cn1cento.NU_NOTA_CN.describe()


# In[ ]:


ch1cento.NU_NOTA_CH.describe()


# In[ ]:


lc1cento.NU_NOTA_LC.describe()


# In[ ]:


mt1cento.NU_NOTA_MT.describe()


# In[ ]:


cn1cento.TP_SEXO.value_counts()


# In[ ]:


ch1cento.TP_SEXO.value_counts()


# In[ ]:


lc1cento.TP_SEXO.value_counts()


# In[ ]:


mt1cento.TP_SEXO.value_counts()


# In[ ]:





# In[ ]:


cn1cento.TP_COR_RACA.value_counts()


# In[ ]:


ch1cento.TP_COR_RACA.value_counts()


# In[ ]:


lc1cento.TP_COR_RACA.value_counts()


# In[ ]:


mt1cento.TP_COR_RACA.value_counts()


# In[ ]:





# In[ ]:


cn1cento.Q006.value_counts()


# In[ ]:


ch1cento.Q006.value_counts()


# In[ ]:


lc1cento.Q006.value_counts()


# In[ ]:


mt1cento.Q006.value_counts()


# In[ ]:


cn1cento.TP_ESCOLA.value_counts()


# In[ ]:


ch1cento.TP_ESCOLA.value_counts()


# In[ ]:


lc1cento.TP_ESCOLA.value_counts()


# In[ ]:


mt1cento.TP_ESCOLA.value_counts()


# In[ ]:





# In[ ]:


cn1cento.TX_Result_CN_questao11.value_counts()


# In[ ]:


cn1cento.TX_Result_CN_questao16.value_counts()


# In[ ]:





# In[ ]:


ch1cento.TX_Result_CH_questao13.value_counts()


# In[ ]:


ch1cento.TX_Result_CH_questao45.value_counts()


# In[ ]:





# In[ ]:


lc1cento.TX_Result_LC_questao39.value_counts()


# In[ ]:


lc1cento.TX_Result_LC_questao38.value_counts()


# In[ ]:





# In[ ]:


mt1cento.TX_Result_MT_questao19.value_counts()


# In[ ]:


mt1cento.TX_Result_MT_questao25.value_counts()


# In[ ]:





# In[ ]:


#Comparando as medias nas questões entre as classes

                  #Genero

#Masculino
generoMqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_SEXO=='M')]
generoMqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_SEXO=='M')]
generoMqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_SEXO=='M')]
generoMqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_SEXO=='M')]

generoMq11cn = generoMqcn.TX_Result_CN_questao11.mean()
generoMq16cn = generoMqcn.TX_Result_CN_questao16.mean()

generoMq13ch = generoMqch.TX_Result_CH_questao13.mean()
generoMq45ch = generoMqch.TX_Result_CH_questao45.mean()

generoMq34lc = generoMqlc.TX_Result_LC_questao39.mean()#39 pq são 5 de língua estrangeira + 34 questões de linguagens
generoMq33lc = generoMqlc.TX_Result_LC_questao38.mean()#38 pq são 5 de língua estrangeira + 33 questões de linguagens

generoMq19mt = generoMqmt.TX_Result_MT_questao19.mean()
generoMq25mt = generoMqmt.TX_Result_MT_questao25.mean()

#Feminino
generoFqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_SEXO=='F')]
generoFqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_SEXO=='F')]
generoFqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_SEXO=='F')]
generoFqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_SEXO=='F')]

generoFq11cn = generoFqcn.TX_Result_CN_questao11.mean()
generoFq16cn = generoFqcn.TX_Result_CN_questao16.mean()

generoFq13ch = generoFqch.TX_Result_CH_questao13.mean()
generoFq45ch = generoFqch.TX_Result_CH_questao45.mean()

generoFq34lc = generoFqlc.TX_Result_LC_questao39.mean()
generoFq33lc = generoFqlc.TX_Result_LC_questao38.mean()

generoFq19mt = generoFqmt.TX_Result_MT_questao19.mean()
generoFq25mt = generoFqmt.TX_Result_MT_questao25.mean()


                   #Raça
    
#Branco
racaBqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_COR_RACA== 1)]
racaBqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_COR_RACA== 1)]
racaBqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_COR_RACA== 1)]
racaBqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_COR_RACA== 1)]

racaBq11cn = racaBqcn.TX_Result_CN_questao11.mean()
racaBq16cn = racaBqcn.TX_Result_CN_questao16.mean()

racaBq13ch = racaBqch.TX_Result_CH_questao13.mean()
racaBq45ch = racaBqch.TX_Result_CH_questao45.mean()

racaBq34lc = racaBqlc.TX_Result_LC_questao39.mean()
racaBq33lc = racaBqlc.TX_Result_LC_questao38.mean()

racaBq19mt = racaBqmt.TX_Result_MT_questao19.mean()
racaBq25mt = racaBqmt.TX_Result_MT_questao25.mean()


#Preto
racaPtqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_COR_RACA== 2)]
racaPtqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_COR_RACA== 2)]
racaPtqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_COR_RACA== 2)]
racaPtqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_COR_RACA== 2)]

racaPtq11cn = racaPtqcn.TX_Result_CN_questao11.mean()
racaPtq16cn = racaPtqcn.TX_Result_CN_questao16.mean()

racaPtq13ch = racaPtqch.TX_Result_CH_questao13.mean()
racaPtq45ch = racaPtqch.TX_Result_CH_questao45.mean()

racaPtq34lc = racaPtqlc.TX_Result_LC_questao39.mean()
racaPtq33lc = racaPtqlc.TX_Result_LC_questao38.mean()

racaPtq19mt = racaPtqmt.TX_Result_MT_questao19.mean()
racaPtq25mt = racaPtqmt.TX_Result_MT_questao25.mean()


#Pardo
racaPaqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_COR_RACA== 3)]
racaPaqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_COR_RACA== 3)]
racaPaqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_COR_RACA== 3)]
racaPaqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_COR_RACA== 3)]

racaPaq11cn = racaPaqcn.TX_Result_CN_questao11.mean()
racaPaq16cn = racaPaqcn.TX_Result_CN_questao16.mean()

racaPaq13ch = racaPaqch.TX_Result_CH_questao13.mean()
racaPaq45ch = racaPaqch.TX_Result_CH_questao45.mean()

racaPaq34lc = racaPaqlc.TX_Result_LC_questao39.mean()
racaPaq33lc = racaPaqlc.TX_Result_LC_questao38.mean()

racaPaq19mt = racaPaqmt.TX_Result_MT_questao19.mean()
racaPaq25mt = racaPaqmt.TX_Result_MT_questao25.mean()


#Amarelo
racaAqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_COR_RACA== 4)]
racaAqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_COR_RACA== 4)]
racaAqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_COR_RACA== 4)]
racaAqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_COR_RACA== 4)]

racaAq11cn = racaAqcn.TX_Result_CN_questao11.mean()
racaAq16cn = racaAqcn.TX_Result_CN_questao16.mean()

racaAq13ch = racaAqch.TX_Result_CH_questao13.mean()
racaAq45ch = racaAqch.TX_Result_CH_questao45.mean()

racaAq34lc = racaAqlc.TX_Result_LC_questao39.mean()
racaAq33lc = racaAqlc.TX_Result_LC_questao38.mean()

racaAq19mt = racaAqmt.TX_Result_MT_questao19.mean()
racaAq25mt = racaAqmt.TX_Result_MT_questao25.mean()


#Indígena
racaIqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_COR_RACA== 5)]
racaIqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_COR_RACA== 5)]
racaIqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_COR_RACA== 5)]
racaIqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_COR_RACA== 5)]

racaIq11cn = racaIqcn.TX_Result_CN_questao11.mean()
racaIq16cn = racaIqcn.TX_Result_CN_questao16.mean()

racaIq13ch = racaIqch.TX_Result_CH_questao13.mean()
racaIq45ch = racaIqch.TX_Result_CH_questao45.mean()

racaIq34lc = racaIqlc.TX_Result_LC_questao39.mean()
racaIq33lc = racaIqlc.TX_Result_LC_questao38.mean()

racaIq19mt = racaIqmt.TX_Result_MT_questao19.mean()
racaIq25mt = racaIqmt.TX_Result_MT_questao25.mean()

                #Renda
    
#renda 0
renda0qcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.Q006== 'A')]
renda0qch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.Q006== 'A')]
renda0qlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.Q006== 'A')]
renda0qmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.Q006== 'A')]

renda0q11cn = renda0qcn.TX_Result_CN_questao11.mean()
renda0q16cn = renda0qcn.TX_Result_CN_questao16.mean()

renda0q13ch = renda0qch.TX_Result_CH_questao13.mean()
renda0q45ch = renda0qch.TX_Result_CH_questao45.mean()

renda0q34lc = renda0qlc.TX_Result_LC_questao39.mean()
renda0q33lc = renda0qlc.TX_Result_LC_questao38.mean()

renda0q19mt = renda0qmt.TX_Result_MT_questao19.mean()
renda0q25mt = renda0qmt.TX_Result_MT_questao25.mean()


#renda até 937
renda1qcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.Q006== 'B')]
renda1qch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.Q006== 'B')]
renda1qlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.Q006== 'B')]
renda1qmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.Q006== 'B')]

renda1q11cn = renda1qcn.TX_Result_CN_questao11.mean()
renda1q16cn = renda1qcn.TX_Result_CN_questao16.mean()

renda1q13ch = renda1qch.TX_Result_CH_questao13.mean()
renda1q45ch = renda1qch.TX_Result_CH_questao45.mean()

renda1q34lc = renda1qlc.TX_Result_LC_questao39.mean()
renda1q33lc = renda1qlc.TX_Result_LC_questao38.mean()

renda1q19mt = renda1qmt.TX_Result_MT_questao19.mean()
renda1q25mt = renda1qmt.TX_Result_MT_questao25.mean()


#renda de 1874,01 até 2342,50
renda2qcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.Q006== 'E')]
renda2qch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.Q006== 'E')]
renda2qlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.Q006== 'E')]
renda2qmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.Q006== 'E')]

renda2q11cn = renda2qcn.TX_Result_CN_questao11.mean()
renda2q16cn = renda2qcn.TX_Result_CN_questao16.mean()

renda2q13ch = renda2qch.TX_Result_CH_questao13.mean()
renda2q45ch = renda2qch.TX_Result_CH_questao45.mean()

renda2q34lc = renda2qlc.TX_Result_LC_questao39.mean()
renda2q33lc = renda2qlc.TX_Result_LC_questao38.mean()

renda2q19mt = renda2qmt.TX_Result_MT_questao19.mean()
renda2q25mt = renda2qmt.TX_Result_MT_questao25.mean()


#renda de 3748,01 até 4685
renda3qcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.Q006== 'H')]
renda3qch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.Q006== 'H')]
renda3qlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.Q006== 'H')]
renda3qmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.Q006== 'H')]

renda3q11cn = renda3qcn.TX_Result_CN_questao11.mean()
renda3q16cn = renda3qcn.TX_Result_CN_questao16.mean()

renda3q13ch = renda3qch.TX_Result_CH_questao13.mean()
renda3q45ch = renda3qch.TX_Result_CH_questao45.mean()

renda3q34lc = renda3qlc.TX_Result_LC_questao39.mean()
renda3q33lc = renda3qlc.TX_Result_LC_questao38.mean()

renda3q19mt = renda3qmt.TX_Result_MT_questao19.mean()
renda3q25mt = renda3qmt.TX_Result_MT_questao25.mean()


#renda de 9370,01 até 11244
renda4qcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.Q006== 'N')]
renda4qch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.Q006== 'N')]
renda4qlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.Q006== 'N')]
renda4qmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.Q006== 'N')]

renda4q11cn = renda4qcn.TX_Result_CN_questao11.mean()
renda4q16cn = renda4qcn.TX_Result_CN_questao16.mean()

renda4q13ch = renda4qch.TX_Result_CH_questao13.mean()
renda4q45ch = renda4qch.TX_Result_CH_questao45.mean()

renda4q34lc = renda4qlc.TX_Result_LC_questao39.mean()
renda4q33lc = renda4qlc.TX_Result_LC_questao38.mean()

renda4q19mt = renda4qmt.TX_Result_MT_questao19.mean()
renda4q25mt = renda4qmt.TX_Result_MT_questao25.mean()


#renda superior a 1874
renda5qcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.Q006== 'Q')]
renda5qch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.Q006== 'Q')]
renda5qlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.Q006== 'Q')]
renda5qmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.Q006== 'Q')]

renda5q11cn = renda5qcn.TX_Result_CN_questao11.mean()
renda5q16cn = renda5qcn.TX_Result_CN_questao16.mean()

renda5q13ch = renda5qch.TX_Result_CH_questao13.mean()
renda5q45ch = renda5qch.TX_Result_CH_questao45.mean()

renda5q34lc = renda5qlc.TX_Result_LC_questao39.mean()
renda5q33lc = renda5qlc.TX_Result_LC_questao38.mean()

renda5q19mt = renda5qmt.TX_Result_MT_questao19.mean()
renda5q25mt = renda5qmt.TX_Result_MT_questao25.mean()

                  #Tipo de Escola
    
#publica
escolaPbqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_ESCOLA==2)]
escolaPbqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_ESCOLA==2)]
escolaPbqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_ESCOLA==2)]
escolaPbqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_ESCOLA==2)]

escolaPbq11cn = escolaPbqcn.TX_Result_CN_questao11.mean()
escolaPbq16cn = escolaPbqcn.TX_Result_CN_questao16.mean()

escolaPbq13ch = escolaPbqch.TX_Result_CH_questao13.mean()
escolaPbq45ch = escolaPbqch.TX_Result_CH_questao45.mean()

escolaPbq34lc = escolaPbqlc.TX_Result_LC_questao39.mean()
escolaPbq33lc = escolaPbqlc.TX_Result_LC_questao38.mean()

escolaPbq19mt = escolaPbqmt.TX_Result_MT_questao19.mean()
escolaPbq25mt = escolaPbqmt.TX_Result_MT_questao25.mean()


#privada
escolaPvqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_ESCOLA==3)]
escolaPvqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_ESCOLA==3)]
escolaPvqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_ESCOLA==3)]
escolaPvqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_ESCOLA==3)]

escolaPvq11cn = escolaPvqcn.TX_Result_CN_questao11.mean()
escolaPvq16cn = escolaPvqcn.TX_Result_CN_questao16.mean()

escolaPvq13ch = escolaPvqch.TX_Result_CH_questao13.mean()
escolaPvq45ch = escolaPvqch.TX_Result_CH_questao45.mean()

escolaPvq34lc = escolaPvqlc.TX_Result_LC_questao39.mean()
escolaPvq33lc = escolaPvqlc.TX_Result_LC_questao38.mean()

escolaPvq19mt = escolaPvqmt.TX_Result_MT_questao19.mean()
escolaPvq25mt = escolaPvqmt.TX_Result_MT_questao25.mean()


#exterior
escolaEqcn = dados.loc[(dados.CO_PROVA_CN==391.0) & (dados.TP_ESCOLA==4)]
escolaEqch = dados.loc[(dados.CO_PROVA_CH==395.0) & (dados.TP_ESCOLA==4)]
escolaEqlc = dados.loc[(dados.CO_PROVA_LC==399.0) & (dados.TP_ESCOLA==4)]
escolaEqmt = dados.loc[(dados.CO_PROVA_MT==403.0) & (dados.TP_ESCOLA==4)]

escolaEq11cn = escolaEqcn.TX_Result_CN_questao11.mean()
escolaEq16cn = escolaEqcn.TX_Result_CN_questao16.mean()

escolaEq13ch = escolaEqch.TX_Result_CH_questao13.mean()
escolaEq45ch = escolaEqch.TX_Result_CH_questao45.mean()

escolaEq34lc = escolaEqlc.TX_Result_LC_questao39.mean()
escolaEq33lc = escolaEqlc.TX_Result_LC_questao38.mean()

escolaEq19mt = escolaEqmt.TX_Result_MT_questao19.mean()
escolaEq25mt = escolaEqmt.TX_Result_MT_questao25.mean()


# In[ ]:





# In[ ]:


generoMq19mt


# In[ ]:


generoMq25mt


# In[ ]:


generoFq19mt


# In[ ]:


generoFq25mt


# In[ ]:





# In[ ]:


print(escolaPbq11cn, escolaPvq11cn, escolaEq11cn)


# In[ ]:


print(escolaPbq16cn, escolaPvq16cn, escolaEq16cn)


# In[ ]:


print(escolaPbq13ch, escolaPvq13ch, escolaEq13ch)


# In[ ]:


print(escolaPbq45ch, escolaPvq45ch, escolaEq45ch)


# In[ ]:


print(escolaPbq34lc, escolaPvq34lc, escolaEq34lc)


# In[ ]:


print(escolaPbq33lc, escolaPvq33lc, escolaEq33lc)


# In[ ]:


print(escolaPbq19mt, escolaPvq19mt, escolaEq19mt)


# In[ ]:


print(escolaPbq25mt, escolaPvq25mt, escolaEq25mt)


# In[ ]:





# In[ ]:


print(generoMq34lc,
generoFq34lc,
racaBq34lc,
racaPtq34lc,
racaPaq34lc,
racaAq34lc,
racaIq34lc,
renda0q34lc,
renda1q34lc,
renda2q34lc,
renda3q34lc,
renda4q34lc,
renda5q34lc,
escolaPbq34lc,
escolaPvq34lc,
escolaEq34lc)


# In[ ]:


print(generoMq33lc,
generoFq33lc,
racaBq33lc,
racaPtq33lc,
racaPaq33lc,
racaAq33lc,
racaIq33lc,
renda0q33lc,
renda1q33lc,
renda2q33lc,
renda3q33lc,
renda4q33lc,
renda5q33lc,
escolaPbq33lc,
escolaPvq33lc,
escolaEq33lc)


# In[ ]:





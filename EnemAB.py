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
    resultCNq1[i]= respostaCN[i][0]           

#q2
for i in respostaCN.index: 
    resultCNq2[i]=respostaCN[i][1]
       
#q3
for i in respostaCN.index:
    resultCNq3[i]=respostaCN[i][2]

#q4
for i in respostaCN.index:
    resultCNq4[i]=respostaCN[i][3]

#q5
for i in respostaCN.index:
    resultCNq5[i]=respostaCN[i][4]

#q6
for i in respostaCN.index:
    resultCNq6[i]=respostaCN[i][5]

#q7
for i in respostaCN.index:
    resultCNq7[i]=respostaCN[i][6]

#q8
for i in respostaCN.index:
    resultCNq8[i]=respostaCN[i][7]

#q9
for i in respostaCN.index:
    resultCNq9[i]=respostaCN[i][8]

#q10
for i in respostaCN.index:
    resultCNq10[i]=respostaCN[i][9]

#q11
for i in respostaCN.index:
    resultCNq11[i]=respostaCN[i][10]

#q12
for i in respostaCN.index:
    resultCNq12[i]=respostaCN[i][11]

#q13
for i in respostaCN.index:
    resultCNq13[i]=respostaCN[i][12]

#q14
for i in respostaCN.index:
    resultCNq14[i]=respostaCN[i][13]

#q15
for i in respostaCN.index:
    resultCNq15[i]=respostaCN[i][14]

#q16
for i in respostaCN.index:
    resultCNq16[i]=respostaCN[i][15]

#q17
for i in respostaCN.index:
    resultCNq17[i]=respostaCN[i][16]

#q18
for i in respostaCN.index:
    resultCNq18[i]=respostaCN[i][17]

#q19
for i in respostaCN.index:
    resultCNq19[i]=respostaCN[i][18]

#q20
for i in respostaCN.index:
    resultCNq20[i]=respostaCN[i][19]

#q21
for i in respostaCN.index:
    resultCNq21[i]=respostaCN[i][20]

#q22
for i in respostaCN.index:
    resultCNq22[i]=respostaCN[i][21]

#q23
for i in respostaCN.index:
    resultCNq23[i]=respostaCN[i][22]

#q24
for i in respostaCN.index:
    resultCNq24[i]=respostaCN[i][23]

#q25
for i in respostaCN.index:
    resultCNq25[i]=respostaCN[i][24]

#q26
for i in respostaCN.index:
    resultCNq26[i]=respostaCN[i][25]

#q27
for i in respostaCN.index:
    resultCNq27[i]=respostaCN[i][26]

#q28
for i in respostaCN.index:
    resultCNq28[i]=respostaCN[i][27]

#q29
for i in respostaCN.index:
    resultCNq29[i]=respostaCN[i][28]

#q30
for i in respostaCN.index:
    resultCNq30[i]=respostaCN[i][29]

#q31
for i in respostaCN.index:
    resultCNq31[i]=respostaCN[i][30]
    
#q32
for i in respostaCN.index:
    resultCNq32[i]=respostaCN[i][31]

#q33
for i in respostaCN.index:
    resultCNq33[i]=respostaCN[i][32]

#q34
for i in respostaCN.index:
    resultCNq34[i]=respostaCN[i][33]

#q35
for i in respostaCN.index:
    resultCNq35[i]=respostaCN[i][34]

#q36
for i in respostaCN.index:
    resultCNq36[i]=respostaCN[i][35]

#q37
for i in respostaCN.index:
    resultCNq37[i]=respostaCN[i][36]

#q38
for i in respostaCN.index:
    resultCNq38[i]=respostaCN[i][37]

#q39
for i in respostaCN.index:
    resultCNq39[i]=respostaCN[i][38]

#q40
for i in respostaCN.index:
    resultCNq40[i]=respostaCN[i][39]

#q41
for i in respostaCN.index:
    resultCNq41[i]=respostaCN[i][40]

#q42
for i in respostaCN.index:
    resultCNq42[i]=respostaCN[i][41]

#q43
for i in respostaCN.index:
    resultCNq43[i]=respostaCN[i][42]

#q44
for i in respostaCN.index:
    resultCNq44[i]=respostaCN[i][43]

#q45
for i in respostaCN.index:
    resultCNq45[i]=respostaCN[i][44]



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
    resultCHq1[i]= respostaCH[i][0]           

#q2
for i in respostaCH.index: 
    resultCHq2[i]=respostaCH[i][1]
       
#q3
for i in respostaCH.index:
    resultCHq3[i]=respostaCH[i][2]

#q4
for i in respostaCH.index:
    resultCHq4[i]=respostaCH[i][3]

#q5
for i in respostaCH.index:
    resultCHq5[i]=respostaCH[i][4]

#q6
for i in respostaCH.index:
    resultCHq6[i]=respostaCH[i][5]

#q7
for i in respostaCH.index:
    resultCHq7[i]=respostaCH[i][6]

#q8
for i in respostaCH.index:
    resultCHq8[i]=respostaCH[i][7]

#q9
for i in respostaCH.index:
    resultCHq9[i]=respostaCH[i][8]

#q10
for i in respostaCH.index:
    resultCHq10[i]=respostaCH[i][9]

#q11
for i in respostaCH.index:
    resultCHq11[i]=respostaCH[i][10]

#q12
for i in respostaCH.index:
    resultCHq12[i]=respostaCH[i][11]

#q13
for i in respostaCH.index:
    resultCHq13[i]=respostaCH[i][12]

#q14
for i in respostaCH.index:
    resultCHq14[i]=respostaCH[i][13]

#q15
for i in respostaCH.index:
    resultCHq15[i]=respostaCH[i][14]

#q16
for i in respostaCH.index:
    resultCHq16[i]=respostaCH[i][15]

#q17
for i in respostaCH.index:
    resultCHq17[i]=respostaCH[i][16]

#q18
for i in respostaCH.index:
    resultCHq18[i]=respostaCH[i][17]

#q19
for i in respostaCH.index:
    resultCHq19[i]=respostaCH[i][18]

#q20
for i in respostaCH.index:
    resultCHq20[i]=respostaCH[i][19]

#q21
for i in respostaCH.index:
    resultCHq21[i]=respostaCH[i][20]

#q22
for i in respostaCH.index:
    resultCHq22[i]=respostaCH[i][21]

#q23
for i in respostaCH.index:
    resultCHq23[i]=respostaCH[i][22]

#q24
for i in respostaCH.index:
    resultCHq24[i]=respostaCH[i][23]

#q25
for i in respostaCH.index:
    resultCHq25[i]=respostaCH[i][24]

#q26
for i in respostaCH.index:
    resultCHq26[i]=respostaCH[i][25]

#q27
for i in respostaCH.index:
    resultCHq27[i]=respostaCH[i][26]

#q28
for i in respostaCH.index:
    resultCHq28[i]=respostaCH[i][27]

#q29
for i in respostaCH.index:
    resultCHq29[i]=respostaCH[i][28]

#q30
for i in respostaCH.index:
    resultCHq30[i]=respostaCH[i][29]

#q31
for i in respostaCH.index:
    resultCHq31[i]=respostaCH[i][30]
    
#q32
for i in respostaCH.index:
    resultCHq32[i]=respostaCH[i][31]

#q33
for i in respostaCH.index:
    resultCHq33[i]=respostaCH[i][32]

#q34
for i in respostaCH.index:
    resultCHq34[i]=respostaCH[i][33]

#q35
for i in respostaCH.index:
    resultCHq35[i]=respostaCH[i][34]

#q36
for i in respostaCH.index:
    resultCHq36[i]=respostaCH[i][35]

#q37
for i in respostaCH.index:
    resultCHq37[i]=respostaCH[i][36]

#q38
for i in respostaCH.index:
    resultCHq38[i]=respostaCH[i][37]

#q39
for i in respostaCH.index:
    resultCHq39[i]=respostaCH[i][38]

#q40
for i in respostaCH.index:
    resultCHq40[i]=respostaCH[i][39]

#q41
for i in respostaCH.index:
    resultCHq41[i]=respostaCH[i][40]

#q42
for i in respostaCH.index:
    resultCHq42[i]=respostaCH[i][41]

#q43
for i in respostaCH.index:
    resultCHq43[i]=respostaCH[i][42]

#q44
for i in respostaCH.index:
    resultCHq44[i]=respostaCH[i][43]

#q45
for i in respostaCH.index:
    resultCHq45[i]=respostaCH[i][44]




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
    resultLCq1[i]= respostaLC[i][0]           

#q2
for i in respostaLC.index: 
    resultLCq2[i]=respostaLC[i][1]
       
#q3
for i in respostaLC.index:
    resultLCq3[i]=respostaLC[i][2]

#q4
for i in respostaLC.index:
    resultLCq4[i]=respostaLC[i][3]

#q5
for i in respostaLC.index:
    resultLCq5[i]=respostaLC[i][4]

#q6
for i in respostaLC.index:
    resultLCq6[i]=respostaLC[i][5]

#q7
for i in respostaLC.index:
    resultLCq7[i]=respostaLC[i][6]

#q8
for i in respostaLC.index:
    resultLCq8[i]=respostaLC[i][7]

#q9
for i in respostaLC.index:
    resultLCq9[i]=respostaLC[i][8]

#q10
for i in respostaLC.index:
    resultLCq10[i]=respostaLC[i][9]

#q11
for i in respostaLC.index:
    resultLCq11[i]=respostaLC[i][10]

#q12
for i in respostaLC.index:
    resultLCq12[i]=respostaLC[i][11]

#q13
for i in respostaLC.index:
    resultLCq13[i]=respostaLC[i][12]

#q14
for i in respostaLC.index:
    resultLCq14[i]=respostaLC[i][13]

#q15
for i in respostaLC.index:
    resultLCq15[i]=respostaLC[i][14]

#q16
for i in respostaLC.index:
    resultLCq16[i]=respostaLC[i][15]

#q17
for i in respostaLC.index:
    resultLCq17[i]=respostaLC[i][16]

#q18
for i in respostaLC.index:
    resultLCq18[i]=respostaLC[i][17]

#q19
for i in respostaLC.index:
    resultLCq19[i]=respostaLC[i][18]

#q20
for i in respostaLC.index:
    resultLCq20[i]=respostaLC[i][19]

#q21
for i in respostaLC.index:
    resultLCq21[i]=respostaLC[i][20]

#q22
for i in respostaLC.index:
    resultLCq22[i]=respostaLC[i][21]

#q23
for i in respostaLC.index:
    resultLCq23[i]=respostaLC[i][22]

#q24
for i in respostaLC.index:
    resultLCq24[i]=respostaLC[i][23]

#q25
for i in respostaLC.index:
    resultLCq25[i]=respostaLC[i][24]

#q26
for i in respostaLC.index:
    resultLCq26[i]=respostaLC[i][25]

#q27
for i in respostaLC.index:
    resultLCq27[i]=respostaLC[i][26]

#q28
for i in respostaLC.index:
    resultLCq28[i]=respostaLC[i][27]

#q29
for i in respostaLC.index:
    resultLCq29[i]=respostaLC[i][28]

#q30
for i in respostaLC.index:
    resultLCq30[i]=respostaLC[i][29]

#q31
for i in respostaLC.index:
    resultLCq31[i]=respostaLC[i][30]
    
#q32
for i in respostaLC.index:
    resultLCq32[i]=respostaLC[i][31]

#q33
for i in respostaLC.index:
    resultLCq33[i]=respostaLC[i][32]

#q34
for i in respostaLC.index:
    resultLCq34[i]=respostaLC[i][33]

#q35
for i in respostaLC.index:
    resultLCq35[i]=respostaLC[i][34]

#q36
for i in respostaLC.index:
    resultLCq36[i]=respostaLC[i][35]

#q37
for i in respostaLC.index:
    resultLCq37[i]=respostaLC[i][36]

#q38
for i in respostaLC.index:
    resultLCq38[i]=respostaLC[i][37]

#q39
for i in respostaLC.index:
    resultLCq39[i]=respostaLC[i][38]

#q40
for i in respostaLC.index:
    resultLCq40[i]=respostaLC[i][39]

#q41
for i in respostaLC.index:
    resultLCq41[i]=respostaLC[i][40]

#q42
for i in respostaLC.index:
    resultLCq42[i]=respostaLC[i][41]

#q43
for i in respostaLC.index:
    resultLCq43[i]=respostaLC[i][42]

#q44
for i in respostaLC.index:
    resultLCq44[i]=respostaLC[i][43]

#q45
for i in respostaLC.index:
    resultLCq45[i]=respostaLC[i][44]
    
#q46
for i in respostaLC.index:
    resultLCq46[i]=respostaLC[i][45]
    
#q47
for i in respostaLC.index:
    resultLCq47[i]=respostaLC[i][46]
    
#q48
for i in respostaLC.index:
    resultLCq48[i]=respostaLC[i][47]
    
#q49
for i in respostaLC.index:
    resultLCq49[i]=respostaLC[i][48]
    
#q50
for i in respostaLC.index:
    resultLCq50[i]=respostaLC[i][49]



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
    resultMTq1[i]= respostaMT[i][0]           

#q2
for i in respostaMT.index: 
    resultMTq2[i]=respostaMT[i][1]
       
#q3
for i in respostaMT.index:
    resultMTq3[i]=respostaMT[i][2]

#q4
for i in respostaMT.index:
    resultMTq4[i]=respostaMT[i][3]

#q5
for i in respostaMT.index:
    resultMTq5[i]=respostaMT[i][4]

#q6
for i in respostaMT.index:
    resultMTq6[i]=respostaMT[i][5]

#q7
for i in respostaMT.index:
    resultMTq7[i]=respostaMT[i][6]

#q8
for i in respostaMT.index:
    resultMTq8[i]=respostaMT[i][7]

#q9
for i in respostaMT.index:
    resultMTq9[i]=respostaMT[i][8]

#q10
for i in respostaMT.index:
    resultMTq10[i]=respostaMT[i][9]

#q11
for i in respostaMT.index:
    resultMTq11[i]=respostaMT[i][10]

#q12
for i in respostaMT.index:
    resultMTq12[i]=respostaMT[i][11]

#q13
for i in respostaMT.index:
    resultMTq13[i]=respostaMT[i][12]

#q14
for i in respostaMT.index:
    resultMTq14[i]=respostaMT[i][13]

#q15
for i in respostaMT.index:
    resultMTq15[i]=respostaMT[i][14]

#q16
for i in respostaMT.index:
    resultMTq16[i]=respostaMT[i][15]

#q17
for i in respostaMT.index:
    resultMTq17[i]=respostaMT[i][16]

#q18
for i in respostaMT.index:
    resultMTq18[i]=respostaMT[i][17]

#q19
for i in respostaMT.index:
    resultMTq19[i]=respostaMT[i][18]

#q20
for i in respostaMT.index:
    resultMTq20[i]=respostaMT[i][19]

#q21
for i in respostaMT.index:
    resultMTq21[i]=respostaMT[i][20]

#q22
for i in respostaMT.index:
    resultMTq22[i]=respostaMT[i][21]

#q23
for i in respostaMT.index:
    resultMTq23[i]=respostaMT[i][22]

#q24
for i in respostaMT.index:
    resultMTq24[i]=respostaMT[i][23]

#q25
for i in respostaMT.index:
    resultMTq25[i]=respostaMT[i][24]

#q26
for i in respostaMT.index:
    resultMTq26[i]=respostaMT[i][25]

#q27
for i in respostaMT.index:
    resultMTq27[i]=respostaMT[i][26]

#q28
for i in respostaMT.index:
    resultMTq28[i]=respostaMT[i][27]

#q29
for i in respostaMT.index:
    resultMTq29[i]=respostaMT[i][28]

#q30
for i in respostaMT.index:
    resultMTq30[i]=respostaMT[i][29]

#q31
for i in respostaMT.index:
    resultMTq31[i]=respostaMT[i][30]
    
#q32
for i in respostaMT.index:
    resultMTq32[i]=respostaMT[i][31]

#q33
for i in respostaMT.index:
    resultMTq33[i]=respostaMT[i][32]

#q34
for i in respostaMT.index:
    resultMTq34[i]=respostaMT[i][33]

#q35
for i in respostaMT.index:
    resultMTq35[i]=respostaMT[i][34]

#q36
for i in respostaMT.index:
    resultMTq36[i]=respostaMT[i][35]

#q37
for i in respostaMT.index:
    resultMTq37[i]=respostaMT[i][36]

#q38
for i in respostaMT.index:
    resultMTq38[i]=respostaMT[i][37]

#q39
for i in respostaMT.index:
    resultMTq39[i]=respostaMT[i][38]

#q40
for i in respostaMT.index:
    resultMTq40[i]=respostaMT[i][39]

#q41
for i in respostaMT.index:
    resultMTq41[i]=respostaMT[i][40]

#q42
for i in respostaMT.index:
    resultMTq42[i]=respostaMT[i][41]

#q43
for i in respostaMT.index:
    resultMTq43[i]=respostaMT[i][42]

#q44
for i in respostaMT.index:
    resultMTq44[i]=respostaMT[i][43]

#q45
for i in respostaMT.index:
    resultMTq45[i]=respostaMT[i][44]



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





# In[ ]:


#Filtrando os dados pelos tipos de cadernos de provas

#separação em tipos de provas de CN 
cadAzulCN=dados.loc[dados.CO_PROVA_CN==391.0] #faz filtragem de dados com CO_PROVA_CN=391 azul
cadAmareloCN=dados.loc[dados.CO_PROVA_CN==392.0]#faz filtragem de dados com CO_PROVA_CN=392 amarelo 
cadCinzaCN=dados.loc[dados.CO_PROVA_CN==393.0] #faz filtragem de dados com CO_PROVA_CN=393 cinza
cadRosaCN=dados.loc[dados.CO_PROVA_CN==394.0]#faz filtragem de dados com CO_PROVA_CN=394 rosa

#separação em tipos de provas de CH
cadAzulCH=dados.loc[dados.CO_PROVA_CH==395.0]#faz filtragem de dados com CO_PROVA_CH=395 azul
cadAmareloCH=dados.loc[dados.CO_PROVA_CH==396.0] #faz filtragem de dados com CO_PROVA_CH=396 amarelo 
cadBrancoCH=dados.loc[dados.CO_PROVA_CH==397.0]#faz filtragem de dados com CO_PROVA_CH=397 branco
cadRosaCH=dados.loc[dados.CO_PROVA_CH==398.0] #faz filtragem de dados com CO_PROVA_CH=398 rosa

#separação em tipos de provas de LC
cadAzulLC=dados.loc[dados.CO_PROVA_LC==399.0] #faz filtragem de dados com CO_PROVA_LC=399 azul
cadAmareloLC=dados.loc[dados.CO_PROVA_LC==400.0] #faz filtragem de dados com CO_PROVA_LC=400 amarelo 
cadRosaLC=dados.loc[dados.CO_PROVA_LC==401.0] #faz filtragem de dados com CO_PROVA_LC=401 rosa
cadBrancoLC=dados.loc[dados.CO_PROVA_LC==402.0] #faz filtragem de dados com CO_PROVA_LC=402 branco

#separação em tipos de provas de MT
cadAzulMT=dados.loc[dados.CO_PROVA_MT==403.0]#faz filtragem de dados com CO_PROVA_MT=403 azul
cadAmareloMT=dados.loc[dados.CO_PROVA_MT==404.0] #faz filtragem de dados com CO_PROVA_MT=404 amarelo 
cadRosaMT=dados.loc[dados.CO_PROVA_MT==405.0]#faz filtragem de dados com CO_PROVA_MT=405 rosa
cadCinzaMT=dados.loc[dados.CO_PROVA_MT==406.0] #faz filtragem de dados com CO_PROVA_MT=406 cinza


# In[ ]:





# In[ ]:


### Respostas para cada questão, separando por tipo de caderno na prova de CN ###

#Caderno azul
respCNQ1az=cadAzulCN.TX_Result_CN_questao1.value_counts()
respCNQ2az=cadAzulCN.TX_Result_CN_questao2.value_counts()
respCNQ3az=cadAzulCN.TX_Result_CN_questao3.value_counts()
respCNQ4az=cadAzulCN.TX_Result_CN_questao4.value_counts()
respCNQ5az=cadAzulCN.TX_Result_CN_questao5.value_counts()
respCNQ6az=cadAzulCN.TX_Result_CN_questao6.value_counts()
respCNQ7az=cadAzulCN.TX_Result_CN_questao7.value_counts()
respCNQ8az=cadAzulCN.TX_Result_CN_questao8.value_counts()
respCNQ9az=cadAzulCN.TX_Result_CN_questao9.value_counts()
respCNQ10az=cadAzulCN.TX_Result_CN_questao10.value_counts()
respCNQ11az=cadAzulCN.TX_Result_CN_questao11.value_counts()
respCNQ12az=cadAzulCN.TX_Result_CN_questao12.value_counts()
respCNQ13az=cadAzulCN.TX_Result_CN_questao13.value_counts()
respCNQ14az=cadAzulCN.TX_Result_CN_questao14.value_counts()
respCNQ15az=cadAzulCN.TX_Result_CN_questao15.value_counts()
respCNQ16az=cadAzulCN.TX_Result_CN_questao16.value_counts()
respCNQ17az=cadAzulCN.TX_Result_CN_questao17.value_counts()
respCNQ18az=cadAzulCN.TX_Result_CN_questao18.value_counts()
respCNQ19az=cadAzulCN.TX_Result_CN_questao19.value_counts()
respCNQ20az=cadAzulCN.TX_Result_CN_questao20.value_counts()
respCNQ21az=cadAzulCN.TX_Result_CN_questao21.value_counts()
respCNQ22az=cadAzulCN.TX_Result_CN_questao22.value_counts()
respCNQ23az=cadAzulCN.TX_Result_CN_questao23.value_counts()
respCNQ24az=cadAzulCN.TX_Result_CN_questao24.value_counts()
respCNQ25az=cadAzulCN.TX_Result_CN_questao25.value_counts()
respCNQ26az=cadAzulCN.TX_Result_CN_questao26.value_counts()
respCNQ27az=cadAzulCN.TX_Result_CN_questao27.value_counts()
respCNQ28az=cadAzulCN.TX_Result_CN_questao28.value_counts()
respCNQ29az=cadAzulCN.TX_Result_CN_questao29.value_counts()
respCNQ30az=cadAzulCN.TX_Result_CN_questao30.value_counts()
respCNQ31az=cadAzulCN.TX_Result_CN_questao31.value_counts()
respCNQ32az=cadAzulCN.TX_Result_CN_questao32.value_counts()
respCNQ33az=cadAzulCN.TX_Result_CN_questao33.value_counts()
respCNQ34az=cadAzulCN.TX_Result_CN_questao34.value_counts()
respCNQ35az=cadAzulCN.TX_Result_CN_questao35.value_counts()
respCNQ36az=cadAzulCN.TX_Result_CN_questao36.value_counts()
respCNQ37az=cadAzulCN.TX_Result_CN_questao37.value_counts()
respCNQ38az=cadAzulCN.TX_Result_CN_questao38.value_counts()
respCNQ39az=cadAzulCN.TX_Result_CN_questao39.value_counts()
respCNQ40az=cadAzulCN.TX_Result_CN_questao40.value_counts()
respCNQ41az=cadAzulCN.TX_Result_CN_questao41.value_counts()
respCNQ42az=cadAzulCN.TX_Result_CN_questao42.value_counts()
respCNQ43az=cadAzulCN.TX_Result_CN_questao43.value_counts()
respCNQ44az=cadAzulCN.TX_Result_CN_questao44.value_counts()
respCNQ45az=cadAzulCN.TX_Result_CN_questao45.value_counts()


# In[ ]:





# In[ ]:


### Respostas para cada questão, separando por tipo de caderno na prova de CH ###

#Caderno azul
respCHQ1az=cadAzulCH.TX_Result_CH_questao1.value_counts()
respCHQ2az=cadAzulCH.TX_Result_CH_questao2.value_counts()
respCHQ3az=cadAzulCH.TX_Result_CH_questao3.value_counts()
respCHQ4az=cadAzulCH.TX_Result_CH_questao4.value_counts()
respCHQ5az=cadAzulCH.TX_Result_CH_questao5.value_counts()
respCHQ6az=cadAzulCH.TX_Result_CH_questao6.value_counts()
respCHQ7az=cadAzulCH.TX_Result_CH_questao7.value_counts()
respCHQ8az=cadAzulCH.TX_Result_CH_questao8.value_counts()
respCHQ9az=cadAzulCH.TX_Result_CH_questao9.value_counts()
respCHQ10az=cadAzulCH.TX_Result_CH_questao10.value_counts()
respCHQ11az=cadAzulCH.TX_Result_CH_questao11.value_counts()
respCHQ12az=cadAzulCH.TX_Result_CH_questao12.value_counts()
respCHQ13az=cadAzulCH.TX_Result_CH_questao13.value_counts()
respCHQ14az=cadAzulCH.TX_Result_CH_questao14.value_counts()
respCHQ15az=cadAzulCH.TX_Result_CH_questao15.value_counts()
respCHQ16az=cadAzulCH.TX_Result_CH_questao16.value_counts()
respCHQ17az=cadAzulCH.TX_Result_CH_questao17.value_counts()
respCHQ18az=cadAzulCH.TX_Result_CH_questao18.value_counts()
respCHQ19az=cadAzulCH.TX_Result_CH_questao19.value_counts()
respCHQ20az=cadAzulCH.TX_Result_CH_questao20.value_counts()
respCHQ21az=cadAzulCH.TX_Result_CH_questao21.value_counts()
respCHQ22az=cadAzulCH.TX_Result_CH_questao22.value_counts()
respCHQ23az=cadAzulCH.TX_Result_CH_questao23.value_counts()
respCHQ24az=cadAzulCH.TX_Result_CH_questao24.value_counts()
respCHQ25az=cadAzulCH.TX_Result_CH_questao25.value_counts()
respCHQ26az=cadAzulCH.TX_Result_CH_questao26.value_counts()
respCHQ27az=cadAzulCH.TX_Result_CH_questao27.value_counts()
respCHQ28az=cadAzulCH.TX_Result_CH_questao28.value_counts()
respCHQ29az=cadAzulCH.TX_Result_CH_questao29.value_counts()
respCHQ30az=cadAzulCH.TX_Result_CH_questao30.value_counts()
respCHQ31az=cadAzulCH.TX_Result_CH_questao31.value_counts()
respCHQ32az=cadAzulCH.TX_Result_CH_questao32.value_counts()
respCHQ33az=cadAzulCH.TX_Result_CH_questao33.value_counts()
respCHQ34az=cadAzulCH.TX_Result_CH_questao34.value_counts()
respCHQ35az=cadAzulCH.TX_Result_CH_questao35.value_counts()
respCHQ36az=cadAzulCH.TX_Result_CH_questao36.value_counts()
respCHQ37az=cadAzulCH.TX_Result_CH_questao37.value_counts()
respCHQ38az=cadAzulCH.TX_Result_CH_questao38.value_counts()
respCHQ39az=cadAzulCH.TX_Result_CH_questao39.value_counts()
respCHQ40az=cadAzulCH.TX_Result_CH_questao40.value_counts()
respCHQ41az=cadAzulCH.TX_Result_CH_questao41.value_counts()
respCHQ42az=cadAzulCH.TX_Result_CH_questao42.value_counts()
respCHQ43az=cadAzulCH.TX_Result_CH_questao43.value_counts()
respCHQ44az=cadAzulCH.TX_Result_CH_questao44.value_counts()
respCHQ45az=cadAzulCH.TX_Result_CH_questao45.value_counts()


# In[ ]:





# In[ ]:


### Respostas para cada questão, separando por tipo de caderno na prova de LC ###

#Caderno azul
respLCQ1az=cadAzulLC.TX_Result_LC_questao1.value_counts()
respLCQ2az=cadAzulLC.TX_Result_LC_questao2.value_counts()
respLCQ3az=cadAzulLC.TX_Result_LC_questao3.value_counts()
respLCQ4az=cadAzulLC.TX_Result_LC_questao4.value_counts()
respLCQ5az=cadAzulLC.TX_Result_LC_questao5.value_counts()
respLCQ6az=cadAzulLC.TX_Result_LC_questao6.value_counts()
respLCQ7az=cadAzulLC.TX_Result_LC_questao7.value_counts()
respLCQ8az=cadAzulLC.TX_Result_LC_questao8.value_counts()
respLCQ9az=cadAzulLC.TX_Result_LC_questao9.value_counts()
respLCQ10az=cadAzulLC.TX_Result_LC_questao10.value_counts()
respLCQ11az=cadAzulLC.TX_Result_LC_questao11.value_counts()
respLCQ12az=cadAzulLC.TX_Result_LC_questao12.value_counts()
respLCQ13az=cadAzulLC.TX_Result_LC_questao13.value_counts()
respLCQ14az=cadAzulLC.TX_Result_LC_questao14.value_counts()
respLCQ15az=cadAzulLC.TX_Result_LC_questao15.value_counts()
respLCQ16az=cadAzulLC.TX_Result_LC_questao16.value_counts()
respLCQ17az=cadAzulLC.TX_Result_LC_questao17.value_counts()
respLCQ18az=cadAzulLC.TX_Result_LC_questao18.value_counts()
respLCQ19az=cadAzulLC.TX_Result_LC_questao19.value_counts()
respLCQ20az=cadAzulLC.TX_Result_LC_questao20.value_counts()
respLCQ21az=cadAzulLC.TX_Result_LC_questao21.value_counts()
respLCQ22az=cadAzulLC.TX_Result_LC_questao22.value_counts()
respLCQ23az=cadAzulLC.TX_Result_LC_questao23.value_counts()
respLCQ24az=cadAzulLC.TX_Result_LC_questao24.value_counts()
respLCQ25az=cadAzulLC.TX_Result_LC_questao25.value_counts()
respLCQ26az=cadAzulLC.TX_Result_LC_questao26.value_counts()
respLCQ27az=cadAzulLC.TX_Result_LC_questao27.value_counts()
respLCQ28az=cadAzulLC.TX_Result_LC_questao28.value_counts()
respLCQ29az=cadAzulLC.TX_Result_LC_questao29.value_counts()
respLCQ30az=cadAzulLC.TX_Result_LC_questao30.value_counts()
respLCQ31az=cadAzulLC.TX_Result_LC_questao31.value_counts()
respLCQ32az=cadAzulLC.TX_Result_LC_questao32.value_counts()
respLCQ33az=cadAzulLC.TX_Result_LC_questao33.value_counts()
respLCQ34az=cadAzulLC.TX_Result_LC_questao34.value_counts()
respLCQ35az=cadAzulLC.TX_Result_LC_questao35.value_counts()
respLCQ36az=cadAzulLC.TX_Result_LC_questao36.value_counts()
respLCQ37az=cadAzulLC.TX_Result_LC_questao37.value_counts()
respLCQ38az=cadAzulLC.TX_Result_LC_questao38.value_counts()
respLCQ39az=cadAzulLC.TX_Result_LC_questao39.value_counts()
respLCQ40az=cadAzulLC.TX_Result_LC_questao40.value_counts()
respLCQ41az=cadAzulLC.TX_Result_LC_questao41.value_counts()
respLCQ42az=cadAzulLC.TX_Result_LC_questao42.value_counts()
respLCQ43az=cadAzulLC.TX_Result_LC_questao43.value_counts()
respLCQ44az=cadAzulLC.TX_Result_LC_questao44.value_counts()
respLCQ45az=cadAzulLC.TX_Result_LC_questao45.value_counts()
respLCQ46az=cadAzulLC.TX_Result_LC_questao46.value_counts()
respLCQ47az=cadAzulLC.TX_Result_LC_questao47.value_counts()
respLCQ48az=cadAzulLC.TX_Result_LC_questao48.value_counts()
respLCQ49az=cadAzulLC.TX_Result_LC_questao49.value_counts()
respLCQ50az=cadAzulLC.TX_Result_LC_questao50.value_counts()


# In[ ]:





# In[ ]:


### Respostas para cada questão, separando por tipo de caderno na prova de MT ###

#Caderno azul
respMTQ1az=cadAzulMT.TX_Result_MT_questao1.value_counts()
respMTQ2az=cadAzulMT.TX_Result_MT_questao2.value_counts()
respMTQ3az=cadAzulMT.TX_Result_MT_questao3.value_counts()
respMTQ4az=cadAzulMT.TX_Result_MT_questao4.value_counts()
respMTQ5az=cadAzulMT.TX_Result_MT_questao5.value_counts()
respMTQ6az=cadAzulMT.TX_Result_MT_questao6.value_counts()
respMTQ7az=cadAzulMT.TX_Result_MT_questao7.value_counts()
respMTQ8az=cadAzulMT.TX_Result_MT_questao8.value_counts()
respMTQ9az=cadAzulMT.TX_Result_MT_questao9.value_counts()
respMTQ10az=cadAzulMT.TX_Result_MT_questao10.value_counts()
respMTQ11az=cadAzulMT.TX_Result_MT_questao11.value_counts()
respMTQ12az=cadAzulMT.TX_Result_MT_questao12.value_counts()
respMTQ13az=cadAzulMT.TX_Result_MT_questao13.value_counts()
respMTQ14az=cadAzulMT.TX_Result_MT_questao14.value_counts()
respMTQ15az=cadAzulMT.TX_Result_MT_questao15.value_counts()
respMTQ16az=cadAzulMT.TX_Result_MT_questao16.value_counts()
respMTQ17az=cadAzulMT.TX_Result_MT_questao17.value_counts()
respMTQ18az=cadAzulMT.TX_Result_MT_questao18.value_counts()
respMTQ19az=cadAzulMT.TX_Result_MT_questao19.value_counts()
respMTQ20az=cadAzulMT.TX_Result_MT_questao20.value_counts()
respMTQ21az=cadAzulMT.TX_Result_MT_questao21.value_counts()
respMTQ22az=cadAzulMT.TX_Result_MT_questao22.value_counts()
respMTQ23az=cadAzulMT.TX_Result_MT_questao23.value_counts()
respMTQ24az=cadAzulMT.TX_Result_MT_questao24.value_counts()
respMTQ25az=cadAzulMT.TX_Result_MT_questao25.value_counts()
respMTQ26az=cadAzulMT.TX_Result_MT_questao26.value_counts()
respMTQ27az=cadAzulMT.TX_Result_MT_questao27.value_counts()
respMTQ28az=cadAzulMT.TX_Result_MT_questao28.value_counts()
respMTQ29az=cadAzulMT.TX_Result_MT_questao29.value_counts()
respMTQ30az=cadAzulMT.TX_Result_MT_questao30.value_counts()
respMTQ31az=cadAzulMT.TX_Result_MT_questao31.value_counts()
respMTQ32az=cadAzulMT.TX_Result_MT_questao32.value_counts()
respMTQ33az=cadAzulMT.TX_Result_MT_questao33.value_counts()
respMTQ34az=cadAzulMT.TX_Result_MT_questao34.value_counts()
respMTQ35az=cadAzulMT.TX_Result_MT_questao35.value_counts()
respMTQ36az=cadAzulMT.TX_Result_MT_questao36.value_counts()
respMTQ37az=cadAzulMT.TX_Result_MT_questao37.value_counts()
respMTQ38az=cadAzulMT.TX_Result_MT_questao38.value_counts()
respMTQ39az=cadAzulMT.TX_Result_MT_questao39.value_counts()
respMTQ40az=cadAzulMT.TX_Result_MT_questao40.value_counts()
respMTQ41az=cadAzulMT.TX_Result_MT_questao41.value_counts()
respMTQ42az=cadAzulMT.TX_Result_MT_questao42.value_counts()
respMTQ43az=cadAzulMT.TX_Result_MT_questao43.value_counts()
respMTQ44az=cadAzulMT.TX_Result_MT_questao44.value_counts()
respMTQ45az=cadAzulMT.TX_Result_MT_questao45.value_counts()


# In[ ]:





# In[ ]:


#Plotando gráfico em barra na questão 11 da prova CN 
respCNQ11az.plot.bar()
plt.title("Marcação de alternativas na Q11 de CN")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 25 da prova CN 
respCNQ25az.plot.bar()
plt.title("Marcação de alternativas na Q25 de CN")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 16 da prova CN 
respCNQ16az.plot.bar()
plt.title("Marcação de alternativas na Q16 de CN")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 13 da prova CH
respCHQ13az.plot.bar()
plt.title("Marcação de alternativas na Q13 de CH")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 26 da prova CH
respCHQ26az.plot.bar()
plt.title("Marcação de alternativas na Q26 de CH")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 45 da prova CH
respCHQ45az.plot.bar()
plt.title("Marcação de alternativas na Q45 de CH")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 39 da prova LC
respLCQ39az.plot.bar()
plt.title("Marcação de alternativas na Q39 de LC")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 19 da prova LC
respLCQ19az.plot.bar()
plt.title("Marcação de alternativas na Q19 de LC")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 38 da prova LC
respLCQ38az.plot.bar()
plt.title("Marcação de alternativas na Q38 de LC")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 19 da prova MT
respMTQ19az.plot.bar()
plt.title("Marcação de alternativas na Q19 de MT")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 43 da prova MT
respMTQ43az.plot.bar()
plt.title("Marcação de alternativas na Q43 de MT")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


# In[ ]:


#Plotando gráfico em barra na questão 25 da prova MT
respMTQ25az.plot.bar()
plt.title("Marcação de alternativas na Q25 de MT")
plt.xlabel("Alternativas")
plt.ylabel("Quantidade de inscritos")
plt.grid(True)
plt.show()


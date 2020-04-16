#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[33]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape

q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[34]:


def q2():
    # Retorne aqui o resultado da questão 2.

    # return black_friday[(black_friday['Age'] == '26-35') & (black_friday['Gender'] == 'F')].shape[0]
    return black_friday.query("Gender == 'F' & Age == '26-35'").shape[0]

q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[35]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()

q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[36]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()

q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[37]:


def q5():
    # Retorne aqui o resultado da questão 5.
    
    # Total lines
    tot = black_friday.shape[0]
    
    # Total lines without null value
    non_null = black_friday.dropna().shape[0]
    
    # Lines with some null value: Total lines - Lines with Null
    null_lines = tot - non_null
    
    return null_lines / tot

q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(black_friday.isnull().sum().max())
    
    
q6()    


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[13]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].mode().values[0]

q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[43]:


def q8():
    # Retorne aqui o resultado da questão 8.
    # Select Purchase columns
    purch = black_friday['Purchase']
    # Get normalized values
    norm = (purch - purch.min()) / (purch.max() - purch.min())
    return float(norm.mean())
    
q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[20]:


def q9():
    # Retorne aqui o resultado da questão 9.
    # Select Purchase columns
    purch = black_friday['Purchase']
    
    # Get padronized values
    padr = (purch - purch.mean()) / (purch.std())
    
    return padr[(padr < 1) & (padr > -1)].shape[0]
    
    

q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[42]:


def q10():
    # Retorne aqui o resultado da questão 10.
    # Select Null values from Product_Category_2
    null_cat_two = black_friday[black_friday['Product_Category_2'].isnull()]
    
    # Return min from is null on  Product_Category_3 if there is a null value the result is False
    return bool(null_cat_two['Product_Category_3'].isnull().min())

q10()


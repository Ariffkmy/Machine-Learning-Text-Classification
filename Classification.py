
# coding: utf-8

# In[2]:

import pandas as pd

from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble

import pandas,  numpy, string
# from keras.preprocessing import text, sequence
# from keras import layers, models, optimizers


# In[3]:

# from flask import Flask , request
# from flask_restplus import Api , Resource , fields
# from flask_cors import CORS, cross_origin
# from waitress import serve


# In[ ]:




# In[ ]:




# In[4]:

df=pd.read_excel('AI Dataset.xlsx')


# In[5]:

# df.head()


# In[6]:

# df['TAG'].unique()


# In[7]:

# df[df['TAG']=='Negative MPU4 Committee Feedback'].shape


# In[8]:

# len(df['TAG'].unique())


# In[9]:

train_x, valid_x, train_y, valid_y = model_selection.train_test_split(df['COMMENT'], df['TAG'])


# In[ ]:




# In[10]:

# word level tf-idf
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

tfidf_vect.fit(df['COMMENT'].values.astype('U'))
xtrain_tfidf =  tfidf_vect.transform(train_x.values.astype('U'))
xvalid_tfidf =  tfidf_vect.transform(valid_x.values.astype('U'))


# In[ ]:




# In[11]:


# Linear Classifier on Word Level TF IDF Vectors
# accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xvalid_tfidf)
# print("LR, WordLevel TF-IDF: ", accuracy)


# In[12]:


classifier=linear_model.LogisticRegression()
# fit the training dataset on the classifier
classifier.fit(xtrain_tfidf, train_y)
# predict the labels on validation dataset



# In[13]:

def testaRecord(str_record):
    xvalid_tfidf =  tfidf_vect.transform([str_record])
    predictions = classifier.predict(xvalid_tfidf)
    return predictions


# In[14]:

# testaRecord('you are good')


# In[15]:

# xvalid_tfidf =  tfidf_vect.transform(["MPU4 Committee"])


# In[16]:

# result=pd.DataFrame(columns=['Name','StudentID','Email','ProjectTitle','Feedback','Tag'])


# In[17]:

def Call_function(name_,studentid_,email_,ptitle_,feedback_):
    result=pd.read_excel('Results.xlsx')
    tag=testaRecord(feedback_)[0]
    tmp_=pd.DataFrame(columns=['Name','StudentID','Email','ProjectTitle','Feedback','Tag'],data=[[name_,studentid_,email_,ptitle_,feedback_,tag]])
    result=pd.concat([result,tmp_])
    result.to_excel('Results.xlsx')
    
    return tag
    


# In[18]:

# Call_function("Ariff","MSDS17046","asd@adsf.com","Idk","THis was a good project")


# In[20]:

# Call_function("Ariff","MSDS17046","asd@adsf.com","Idk","THis was a good project")


# In[ ]:




# In[ ]:




# In[ ]:




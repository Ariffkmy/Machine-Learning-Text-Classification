
# coding: utf-8

# In[1]:

import pandas as pd

from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble

import pandas,  numpy,  string
# from keras.preprocessing import text, sequence
# from keras import layers, models, optimizers


# In[2]:

df=pd.read_excel('AI Dataset.xlsx')


# In[85]:

# df.head()


# In[109]:

# df['TAG'].unique()


# In[110]:

# df[df['TAG']=='Negative MPU4 Committee Feedback'].shape


# In[111]:

# len(df['TAG'].unique())


# In[112]:

train_x, valid_x, train_y, valid_y = model_selection.train_test_split(df['COMMENT'], df['TAG'])


# In[ ]:




# In[113]:

# word level tf-idf
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

tfidf_vect.fit(df['COMMENT'].values.astype('U'))
xtrain_tfidf =  tfidf_vect.transform(train_x.values.astype('U'))
xvalid_tfidf =  tfidf_vect.transform(valid_x.values.astype('U'))


# In[ ]:




# In[114]:


# Linear Classifier on Word Level TF IDF Vectors
# accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xvalid_tfidf)
# print("LR, WordLevel TF-IDF: ", accuracy)


# In[115]:


classifier=linear_model.LogisticRegression()
# fit the training dataset on the classifier
classifier.fit(xtrain_tfidf, train_y)
# predict the labels on validation dataset



# In[118]:

def testaRecord(str_record):
    xvalid_tfidf =  tfidf_vect.transform([str_record])
    predictions = classifier.predict(xvalid_tfidf)
    return predictions


# In[125]:

# testaRecord('you are good')


# In[126]:

# xvalid_tfidf =  tfidf_vect.transform(["MPU4 Committee"])


# In[143]:

# result=pd.DataFrame(columns=['Name','StudentID','Email','ProjectTitle','Feedback','Tag'])


# In[150]:

def Call_function(name_,studentid_,email_,ptitle_,feedback_):
    result=pd.read_excel('Results.xlsx')
    tag=testaRecord(feedback_)[0]
    tmp_=pd.DataFrame(columns=['Name','StudentID','Email','ProjectTitle','Feedback','Tag'],data=[[name_,studentid_,email_,ptitle_,feedback_,tag]])
    result=pd.concat([result,tmp_])
    result.to_excel('Results.xlsx')
    
    return tag
    


# In[152]:

# Call_function("Mateen","MSDS17046","asd@adsf.com","Idk","THis was a good project")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




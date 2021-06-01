import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA 
import numpy as np 
import spacy 

nlp = spacy.load("en_core_web_md") 

vocab = nlp("cat dog tiger elephant bird monkey lion cheetah burger pizza food cheese wine salad noodles macaroni fruit vegetable") 

words = [word.text for word in vocab] 
vecs = np.vstack([word.vector for word in vocab if word.has_vector]) 
pca = PCA(n_components=2) 
vecs_transformed = pca.fit_transform(vecs) 
plt.figure(figsize=(20,15)) 
plt.scatter(vecs_transformed[:,0], vecs_transformed[:,1]) 
for word, coord in zip(words, vecs_transformed): 
    x,y = coord 
    plt.text(x,y,word, size=15) 

plt.show() 

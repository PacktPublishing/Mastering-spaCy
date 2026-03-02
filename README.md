


# Mastering spaCy

<a href="https://www.packtpub.com/product/mastering-spacy/9781800563353"><img src="https://static.packt-cdn.com/products/9781800563353/cover/smaller" alt="Mastering spaCy" height="256px" align="right"></a>

This is the code repository for [Mastering spaCy](https://www.packtpub.com/product/mastering-spacy/9781800563353), published by Packt.

**An end-to-end practical guide to implementing NLP applications using the Python ecosystem**

## What is this book about?
spaCy is an industrial-grade, efficient NLP Python library. It offers various pre-trained models and ready-to-use features. Mastering spaCy provides you with end-to-end coverage of spaCy's features and real-world applications.

This book covers the following exciting features: 
* Install spaCy, get started easily, and write your first Python script
* Understand core linguistic operations of spaCy
* Discover how to combine rule-based components with spaCy statistical models
* Become well-versed with named entity and keyword extraction
* Build your own ML pipelines using spaCy

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800563353) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Errata

page 10

How it looks like: word.index(e)
How it should be: word.index("e")

How it looks like: vecs = np.vstack([word.vector for word in vocab if word.has_vector])
How it should be: vecs = np.vstack([word.vector for word in vocab if word.has_vector])



## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import spacy
nlp = spacy.load("en_subwords_wiki_lg"
```

**Following is what you need for this book:**
This book is for data scientists and machine learners who want to excel in NLP as well as NLP developers who want to master spaCy and build applications with it. Language and speech professionals who want to get hands-on with Python and spaCy and software developers who want to quickly prototype applications with spaCy will also find this book helpful. Beginner-level knowledge of the Python programming language is required to get the most out of this book. A beginner-level understanding of linguistics such as parsing, POS tags, and semantic similarity will also be useful.

With the following software and hardware list you can run all code files present in the book (Chapter 1-15).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1        | Python>=3.6                    | Windows, Mac OS X, and Linux (Any) |
| 2        | spaCy v3.0            | Windows, Mac OS X, and Linux (Any) |
| 3        | Tensorflow 2.0           | Windows, Mac OS X, and Linux (Any) |
| 4        | Transformers            | Windows, Mac OS X, and Linux (Any) |
| 5        | scikit-learn          | Windows, Mac OS X, and Linux (Any) |
| 6        | pandas            | Windows, Mac OS X, and Linux (Any) |
| 7        | NumPy            | Windows, Mac OS X, and Linux (Any) |
| 8        | matplotlib           | Windows, Mac OS X, and Linux (Any) |
| 9        | Jupyter            | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it]( https://static.packt-cdn.com/downloads/9781800563353_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Python Natural Language Processing Cookbook [[Packt]](https://www.packtpub.com/product/python-natural-language-processing-cookbook/9781838987312) [[Amazon]](https://www.amazon.com/dp/1838987312)

* Getting Started with Google BERT [[Packt]](https://www.packtpub.com/product/getting-started-with-google-bert/9781838821593) [[Amazon]](https://www.amazon.com/dp/1838821597)

## Get to Know the Author
**Duygu Altınok**
is a senior Natural Language Processing (NLP) engineer with 12 years of experience in almost all areas of NLP, including search engine technology, speech recognition, text analytics, and conversational AI. She has published several publications in the NLP area at conferences such as LREC and CLNLP. She also enjoys working on open source projects and is a contributor to the spaCy library. Duygu earned her undergraduate degree in computer engineering from METU, Ankara, in 2010 and later earned her master's degree in mathematics from Bilkent University, Ankara, in 2012. She is currently a senior engineer at German Autolabs with a focus on conversational AI for voice assistants. Originally from Istanbul, Duygu currently resides in Berlin, Germany, with her cute dog Adele.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800563353">https://packt.link/free-ebook/9781800563353 </a> </p>
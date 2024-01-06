import nltk
from nltk.corpus import stopwords
import streamlit as st 

st.set_page_config(page_title='Text Summarizer',layout='wide')

st.header('Text Summarizer',divider='rainbow')

col1,col2 =st.columns((10,10))

with col1:
    text = st.text_area("Enter text to be summarized",height=400)
    length = st.slider('Summary Length',min_value=1.0,max_value = 2.0,value=1.5,step= 0.1)
    if st.button('Check'):
        with col2:
            freqTable = {}
            stopword = stopwords.words('english')
            for word in text.split():
                if word in stopword:
                    continue
                elif word in freqTable:
                    freqTable[word] += 1
                else:
                    freqTable[word] = 1

            sentTable = {}
            sentences = []
            for sentence in text.split(". "):
                sentences.append(sentence)
                sentTable[sentence.lower()] = 0

            for sentence in sentTable.keys():
                for word,score in freqTable.items():
                    if word.lower() in sentence:
                        sentTable[sentence] += score

            avg_score = 0.0
            for score in sentTable.values():
                avg_score += score
            avg_score = avg_score/len(sentTable)

            output = []
            for sentence in sentTable.keys():
                if sentTable[sentence]>(length*avg_score):
                    output.append(sentence)

            summary = ""
            for sentence in sentences:
                if sentence.lower() in output:
                    summary += sentence
            
            st.write(summary)
            st.write("Original Length = {}".format(len(text.split())))
            st.write("Summary Length  = {}".format(len(summary.split())))


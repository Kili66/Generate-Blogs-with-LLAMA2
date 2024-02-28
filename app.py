import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# function to get model from LLama2

def get_lama_response(input_text, no_words, blog_style):
    ## llma2 model
    llm= CTransformers(model='H:/LLM/llama-7b.ggmlv3.q8_0.bin', model_type='llama', config={'max_new_tokens':256, 'temperature':0.01})
    
    # prompt Template
    template= """
        Write a Blog for {blog_style} job profile for this topic {input_text} within {no_words} words.
        """
    prompt= PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)
    # generate response from llama2
    
    response= llm(prompt.format(blog_style="blog_style", input_text=input_text, no_words=no_words))
    print(response)
    
    return response


st.set_page_config(page_title="Blog Generation", page_icon='🚀', layout='centered', initial_sidebar_state='collapsed')

st.header('Generate Blogs with LLAMA2 🚀')
input_text= st.text_input("Enter the Blog Topic")

# creating 2 more cols for additional fiels

col1, col2= st.columns([5,5])

with col1:
    no_words= st.text_input("Number of Words")
with col2:
    blog_style= st.selectbox('Writing Blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)
submit= st.button("Generate")

# Response

if submit:
    st.write(get_lama_response(input_text, no_words, blog_style))
    
    
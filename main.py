import streamlit as st
import summarization as summa
import grammar as gr
import api
st.set_page_config(page_title="InfoClarity", page_icon=":suitcase")


def col1():
    payload = st.text_area("Enter your text to be summarized")
    summary = summa.query(payload, st.secrets["hf"])
    with st.expander("Text Provided"):
        st.write(payload)
    with st.expander("Summary"):
        st.write(summary)


def col2():
    payload = st.text_area("Enter your text to be corrected")
    if (payload != ""):
        grammar = gr.query(payload, st.secrets["hf"])
        with st.expander("Input"):
            st.write(payload)
        with st.expander("Output"):
            count = 0
            text = ""
            for i in grammar.split():
                if (i == "is:"):
                    k = grammar.split()
                    j = k.index("is:")
                    while grammar.split()[j] != "Input":
                        text = text+" "+k[j]
                        j = j+1
                    count = 1
                    break
                if (count == 1):
                    break

            st.text(text.lstrip("is: "))


def main():
    c1, c2 = st.tabs(["Summary", "Grammar"])
    with c1:
        st.header("Data Summarization")
        col1()
    with c2:
        st.header("Grammar Correction")
        col2()


if __name__ == "__main__":
    main()

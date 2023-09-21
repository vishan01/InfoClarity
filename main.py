import streamlit as st
import summarization as summa
import grammar as gr
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
            text = str(grammar)
            text = text.lstrip(
                f"Input statement: '{payload}' Corrected statement is: ")
            text = text.split(" ")
            text = text[0:len(payload)-1]
            st.text()


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

import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler


def create_def_chain():
    chat = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
        streaming=True,
    )

    tools = load_tools(["ddg-search", "wikipedia"])
    return initialize_agent(tools, chat, agent=AgentType.OPENAI_FUNCTIONS)


load_dotenv()

st.title("Langchain Streamlit App")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")


if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        callback = StreamlitCallbackHandler(st.container())
        agent_chain = create_def_chain()
        response = agent_chain.run(prompt, callbacks=[callback])
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

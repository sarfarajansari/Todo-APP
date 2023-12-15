import streamlit as st
from streamlit_option_menu import option_menu


st.title("To-do App")


with st.sidebar:
    selected = option_menu("Action", [
        "List",
        "Add",
        "Delete",

    ])
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []


tasks = st.session_state["tasks"]
if selected == "List":
    if len(tasks) == 0:
        st.subheader("No Pending Task")

    else:
        st.subheader(("Tasks List"))
        for t in tasks:
            # taskText = t["task"]
            st.markdown(f"- {t}")

if selected == "Add":
    task = st.text_input("New Task")
    if st.button("Add"):


        tasks.append(task)


if selected == "Delete":
    for index, t in enumerate(tasks):
        st.markdown(f"- {t}")

        st.button("Delete", key=index, on_click=lambda: tasks.remove(t))

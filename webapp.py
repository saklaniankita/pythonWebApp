import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)


st.title('My TO DO App')
st.subheader("My To Do App1")
st.write('My To Do App2')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # When st.experimental_rerun() is called, the script is halted - no more statements
        # will be run, and the script will be queued to re-run from the top.

st.text_input(label='', placeholder='Enter todo', on_change=add_todo, key='new_todo')

"""
following line of code is just for understanding purpose
"""
st.session_state
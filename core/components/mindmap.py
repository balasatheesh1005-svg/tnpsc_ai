import streamlit as st

def render_mindmap(node, level=0):

    indent = " " * level

    if "name" in node:
        label = node["name"]["en"]

        with st.expander(f"{indent}👉 {label}", expanded=(level==0)):
            
            st.caption(node["name"].get("ta", ""))

            if "children" in node:
                for child in node["children"]:
                    render_mindmap(child, level+1)
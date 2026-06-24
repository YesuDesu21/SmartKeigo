# app.py
import streamlit as st
from src.agent.graph import keigo_app
from src.agent.utils import initialize_pinecone_index

# Initialize Pinecone index on app startup
initialize_pinecone_index()

st.set_page_config(page_title="Smart Keigo", page_icon="🚀")
st.title("🎌 Keigo Master (ビジネス日本語コーチ)")
st.write("Enter your casual or rough Japanese below to transform it into professional Keigo.")

# 1. UI Input Box
user_text = st.text_area("Your Japanese input:", placeholder="明日、ミーティングに行けないです。")

if st.button("Refine Communication"):
    if user_text.strip() == "":
        st.warning("Please type something first!")
    else:
        # Show a loading spinner while the graph executes background API cycles
        with st.spinner("Analyzing context and generating professional draft..."):
            
            # 2. Feed the text directly into our LangGraph compilation object
            initial_state = {"raw_input": user_text, "audience": "", "draft_keigo": "", "feedback": "", "is_approved": False}
            final_output = keigo_app.invoke(initial_state)
            
            # 3. Display the updated attributes extracted from the final state structure
            st.success("Polishing Complete!")
            
            st.subheader("Target Context Analysis")
            st.info(f"Assessed Target Audience: **{final_output['audience']}**")
            
            st.subheader("Refined Keigo Draft")
            st.code(final_output["draft_keigo"], language="markdown")
            
            st.subheader("Etiquette Coach Notes")
            st.write(final_output["feedback"])

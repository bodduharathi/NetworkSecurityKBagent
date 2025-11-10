import os
import subprocess
import streamlit as st
from rag import make_answer, generate_quiz, grade_quiz


st.set_page_config(
    page_title="CS5342 Network-Security Tutor",
    page_icon="🛡️",
    layout="wide",
)


st.markdown("""
<style>
/* ---- Global look ---- */
html, body, .stApp {
    background: linear-gradient(160deg, #f8fbff 0%, #eef6ff 100%);
    color: #1a1a1a;
    font-family: "Inter", "Segoe UI", sans-serif;
}

h1, h2, h3, h4 {
    color: #003366;
    font-weight: 700;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f2f6ff 100%);
    border-right: 1px solid #cfd9e3;
    box-shadow: 3px 0 6px rgba(0,0,0,0.05);
}

/* ---- Buttons ---- */
.stButton > button {
    background: linear-gradient(90deg, #0099ff, #33ccff);
    color: white;
    font-weight: 600;
    border-radius: 8px;
    border: none;
    padding: 0.45rem 1.3rem;
    box-shadow: 0 3px 6px rgba(0,0,0,0.15);
    transition: 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.2);
}

/* ---- Input boxes ---- */
.stTextInput > div > div > input, textarea {
    background-color: #ffffff !important;
    border: 1px solid #c0d3eb !important;
    border-radius: 6px !important;
    color: #003366 !important;
}

.stRadio > div, .stSelectbox > div, .stSlider {
    color: #003366;
}

/* ---- Cards ---- */
.card {
    background: #ffffffcc;
    border-radius: 16px;
    padding: 1.5rem;
    margin-top: 1rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    border: 1px solid #e0ebf8;
}

/* ---- Dividers ---- */
hr {
    border: 0;
    border-top: 1px solid #e0e7f1;
    margin: 1.5rem 0;
}

/* ---- Tabs ---- */
.stTabs [data-baseweb="tab-list"] {
    gap: 1rem;
}

.stTabs [data-baseweb="tab"] {
    background: #f2f7ff;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    color: #005b9f;
    border: 1px solid #cce0ff;
    transition: 0.25s ease;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #0099ff, #33ccff);
    color: white !important;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;'>
Local Network-Security Tutor & Quiz Bot
</h1>

""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Tutor Agent", "Quiz Agent"])

with tab1:
    query = st.text_input(
        "Type your question:",
        placeholder="e.g., Explain how a firewall filters network traffic."
    )

    k = st.slider("Number of reference sources", 2, 8, 4)

    if st.button("Answer", type="primary"):
        if not query.strip():
            st.warning("Please enter a question first.")
        else:
            with st.spinner("Searching your local study materials..."):
                answer, sources = make_answer(query, k=k)
            st.success("Answer ready!")
            st.markdown("### Response")
            st.info(answer)


    st.markdown("</div>", unsafe_allow_html=True)


with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Generate & Take a Quiz")

    c1, c2 = st.columns(2)
    with c1:
        topic = st.text_input("Quiz topic (optional):", placeholder="e.g., VPN, IDS, Encryption")
    with c2:
        n = st.slider("Number of questions:", 3, 10, 5)

    if st.button("Generate Quiz"):
        with st.spinner("Preparing quiz..."):
            st.session_state.quiz = generate_quiz(topic, n)
        st.success("Quiz generated!")

    if "quiz" in st.session_state:
        quiz = st.session_state.quiz
        if not quiz["items"]:
            st.warning("No quiz data found. Try rebuilding the index.")
        else:
            st.markdown(f"**Topic:** {quiz['topic'].title()} | **Questions:** {len(quiz['items'])}")
            st.divider()

            answers = []
            for i, item in enumerate(quiz["items"], start=1):
                st.markdown(f"**Q{i}.** {item['q']}")
                if item["type"] == "tf":
                    answers.append(st.radio("", [True, False], horizontal=True, key=f"tf_{i}", index=None))
                elif item["type"] == "mcq":
                    answers.append(st.radio("", item["options"], key=f"mcq_{i}", index=None))
                else:
                    answers.append(st.text_area(f"Your response:", key=f"open_{i}", height=80))
                st.markdown("<hr>", unsafe_allow_html=True)

            if st.button("Grade Quiz"):
                with st.spinner("Grading your quiz..."):
                    result = grade_quiz(quiz["items"], answers)
                st.success(f"Your Score: {result['score']} / {result['total']}")

                for d in result["details"]:
                    icon = "✅" if d["correct"] else "❌"
                    st.markdown(f"{icon} **{d['question']}**")
                    st.write(f"- **Your Answer:** {d['your_answer']}")
                    st.write(f"- **Expected:** {d['expected']}")
                    st.caption(f"💡 {d['rationale']}")
                    if d.get("sources"):
                        st.caption("📘 " + ", ".join(d["sources"]))
                    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

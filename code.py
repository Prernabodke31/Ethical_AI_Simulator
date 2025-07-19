import streamlit as st

# Sample rule-based decision logic
def evaluate_ethics(scenario):
    scenario = scenario.lower()
    explanation = ""
    decision = ""

    # Rule 1: Human life > animal life
    if "dog" in scenario or "cat" in scenario:
        decision = "Avoid the human"
        explanation = "Prioritized human life over animal."
    
    # Rule 2: Save more people if possible
    elif "1 person" in scenario and "3 people" in scenario:
        decision = "Save 3 people"
        explanation = "Chose to minimize total harm."

    # Rule 3: Save child over elderly (if forced)
    elif "child" in scenario and "elderly" in scenario:
        decision = "Save the child"
        explanation = "Younger individuals may have longer future lifespan."

    # Rule 4: Default fallback
    else:
        decision = "No clear decision"
        explanation = "Ethical factors unclear. Needs human review."

    return decision, explanation

# Streamlit UI
st.set_page_config(page_title="Ethical AI Simulator", layout="centered")
st.title("⚖️ Ethical AI Simulator")
st.markdown("Enter a moral dilemma and let AI suggest a decision.")

# User input
scenario = st.text_area("Describe a dilemma scenario (e.g., A self-driving car must choose between hitting a child or swerving into a wall):")

if st.button("Evaluate Decision"):
    if scenario.strip():
        decision, explanation = evaluate_ethics(scenario)
        st.subheader("🧠 AI Decision:")
        st.success(decision)

        st.subheader("💬 Explanation:")
        st.info(explanation)
    else:
        st.warning("Please enter a scenario first.")



#cd "C:\Users\prern\Desktop\My Projects"
#streamlit run Ethical_AI_simulator.py



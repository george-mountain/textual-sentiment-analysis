import streamlit as st
from utilities import TextClassifier

classifier = TextClassifier()

fewshot_prompt_template = classifier.fewshot_template


st.title("Text Analysis")

user_input = st.text_area("Enter your text here:")
if st.button("Submit"):
    if not user_input:
        st.error("Provide a text to classify")
    else:
        with st.spinner("Please wait, analysis in progress..."):
            results = classifier.classify_user_input(user_input)
            st.success("Processing completed!")

            percentage_scores, percentage_df = classifier.calculate_percentage(results)
            st.subheader("Percentage Scores:")
            st.table(percentage_df)

            highest_category = classifier.highest_percentage_category(percentage_scores)
            st.subheader("Text Category and Tone:")
            st.success(highest_category)

            st.subheader("Pie Chart:")
            classifier.plot_pie_chart(percentage_scores)

            st.subheader("Bar Chart:")
            classifier.plot_bar_chart(results)

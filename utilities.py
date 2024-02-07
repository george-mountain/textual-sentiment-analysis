import os

import matplotlib.pyplot as plt
import openai
import pandas as pd
import streamlit as st
from dotenv import find_dotenv, load_dotenv


class TextClassifier:
    def __init__(self):
        load_dotenv(find_dotenv())
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.fewshot_template = """
Your task is to classify an input text (delimited by ```) into any of the following categories: anger, joy, love, surprise, hate, fear, and neutral.
You are to return a python dictionary containing each category and their corresponding score for the input text. The true category has a score of 1
while the other categories that the input text does not belong to have a score of 0.

Use the following examples to help with steering your responses:

TEXT: i feel it has only been agitated by the presence of the smoking
OUTPUT: dict('anger':0,'joy':0,'love':0,'surprise':0,'hate':0,'fear':1,'neutral':0)

...

TEXT: i am sure you will agree that these graphics are way cute and how good are you going to feel supporting a real teacher that is just like us
OUTPUT: dict('anger':0,'joy':1,'love':0,'surprise':0,'hate':0,'fear':0,'neutral':0)

Text: {user_input}
Output:
"""

    def split_text(self, input_text):
        sentences = input_text.split(".")
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences

    def get_completion(
        self, messages, model="gpt-3.5-turbo", temperature=0, max_tokens=300
    ):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message["content"]

    def generate_prompt(self, template, user_input):
        return template.format(user_input=f"```{user_input}```")

    def make_api_call(self, prompt, model="gpt-3.5-turbo"):
        message = [{"role": "user", "content": prompt}]
        return self.get_completion(message, model=model)

    def classify_user_input(self, user_input):
        results = {
            "anger": 0,
            "joy": 0,
            "love": 0,
            "surprise": 0,
            "hate": 0,
            "fear": 0,
            "neutral": 0,
        }
        user_inputs = self.split_text(user_input)
        for user_input in user_inputs:
            fewshot_prompt = self.generate_prompt(self.fewshot_template, user_input)
            fewshot_response_gpt_3_5 = self.make_api_call(fewshot_prompt)
            fewshot_response_gpt_3_5_dict = eval(fewshot_response_gpt_3_5)
            results["anger"] += fewshot_response_gpt_3_5_dict.get("anger", 0)
            results["joy"] += fewshot_response_gpt_3_5_dict.get("joy", 0)
            results["love"] += fewshot_response_gpt_3_5_dict.get("love", 0)
            results["surprise"] += fewshot_response_gpt_3_5_dict.get("surprise", 0)
            results["hate"] += fewshot_response_gpt_3_5_dict.get("hate", 0)
            results["fear"] += fewshot_response_gpt_3_5_dict.get("fear", 0)
            results["neutral"] += fewshot_response_gpt_3_5_dict.get("neutral", 0)
        return results

    def calculate_percentage(self, scores):
        total_score = sum(scores.values())
        percentage_scores = {
            category: round((score / total_score) * 100, 2)
            for category, score in scores.items()
        }
        df = pd.DataFrame(
            percentage_scores.items(), columns=["Category", "Percentage %"]
        )
        return percentage_scores, df

    def highest_percentage_category(self, percentage_scores):
        return max(percentage_scores, key=percentage_scores.get)

    def plot_pie_chart(self, percentage_scores, chart_size=(12, 12)):
        labels = list(percentage_scores.keys())
        sizes = list(percentage_scores.values())
        fig, ax = plt.subplots(figsize=chart_size)
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.set_title("Percentage Distribution of Categories")
        ax.legend(labels, loc="upper right")
        st.pyplot(fig)

    def plot_bar_chart(self, scores):
        categories = list(scores.keys())
        values = list(scores.values())
        fig, ax = plt.subplots()
        ax.bar(
            categories,
            values,
            color=["red", "green", "blue", "orange", "purple", "brown", "grey"],
        )
        ax.set_xlabel("Categories")
        ax.set_ylabel("Scores")
        ax.set_title("Scores for Each Category")
        st.pyplot(fig)

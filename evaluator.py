import os
from pprint import pprint

import comet_llm
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from tqdm import tqdm
from utilities import TextClassifier

classifier = TextClassifier()


class EvaluateTextClassifier:
    def __init__(self):
        load_dotenv(find_dotenv())

    def evaluate_response(self, evaluation_data):
        results = []
        for data in tqdm(evaluation_data):
            eval_result = classifier.classify_user_input(data["user_input"])
            percentage_scores, _ = classifier.calculate_percentage(eval_result)
            highest_category = classifier.highest_percentage_category(percentage_scores)
            eval_result["actual_response"] = data["output"]
            eval_result["prediction"] = highest_category
            if data["output"].lower() == highest_category.lower():
                eval_result["remark"] = "Correct"
            else:
                eval_result["remark"] = "Incorrect"
            eval_result["user_input"] = data["user_input"].strip()
            results.append(eval_result)

        df = pd.DataFrame(results)
        df.index.name = "Index"
        return results, df

    def llmops_log_results(self, evaluation_results):

        COMET_API_KEY = os.getenv("COMET_API_KEY")

        comet_llm.init(
            project="text-sentiment-analyser-evaluator", api_key=COMET_API_KEY
        )
        for result in tqdm(evaluation_results):
            user_input = result["user_input"]
            expected_output = result["actual_response"]
            predicted_categories = {
                key: value for key, value in list(result.items())[:6]
            }
            predictition = result["prediction"]
            remark = result["remark"]

            # Log zeroshot predictions
            comet_llm.log_prompt(
                prompt=classifier.generate_prompt(
                    classifier.fewshot_prompt_template, user_input
                ),
                prompt_template="few-shot",
                prompt_template_variables=classifier.fewshot_prompt_template,
                tags=["gpt-3.5", "few-shot"],
                metadata={
                    "model_name": "gpt-3.5",
                    "temperature": 0,
                    "predicted categories": predicted_categories,
                    "expected_output": expected_output,
                    "model_output": predictition,
                    "remark": remark,
                },
                output=remark,
            )


# Evaluation data

evaluation_data = [
    {
        "user_input": """
        I can't believe the incompetence I witnessed at work today. The constant delays, the lack of communication – it's infuriating. 
        I put in extra hours to meet deadlines, only to face setbacks caused by others' negligence. 
        The frustration is building up, and it feels like I'm reaching my limit.

        Despite expressing my concerns, it seems like nobody cares about the impact on the team. It's a continuous cycle of disappointment and anger. 
        I need things to change, or I might just explode. The level of inefficiency is unacceptable, and I can't contain my rage anymore.

        """,
        "output": "anger",
    },
    {
        "user_input": """
            Today was an extraordinary day filled with moments of pure joy. The sun was shining, and I couldn't help but smile as I strolled through the park. 
            I received unexpected good news that lifted my spirits. It's amazing how a simple gesture or a kind word can brighten your entire day.
            Spending time with loved ones added to the joyous atmosphere. Laughter echoed in the air, and for a moment, everything felt perfect. 
            I cherish these moments of happiness, and they remind me of the beauty that surrounds us. 
            Today, joy was the driving force that made every experience memorable.

        """,
        "output": "joy",
    },
    {
        "user_input": """
            In the quiet moments, I find myself reflecting on the profound love that binds us together. 
            The shared experiences, the support during challenging times – it's the foundation of a deep connection. 
            Love is the guiding force that gives life meaning and purpose.

            Even in the mundane routines, there's a warmth that comes from knowing you are cherished. 
            Small gestures, a gentle touch, and the unspoken understanding create a love that withstands the tests of time. 
            Today, as I express my feelings, it's clear that love is the cornerstone of my existence.

        """,
        "output": "love",
    },
    {
        "user_input": """
        
        Life has a way of throwing unexpected twists our way. Today, I stumbled upon a hidden gem – a quaint bookstore tucked away in the heart of the city. 
        The discovery took me by surprise, and the joy of finding such a unique place was exhilarating.

        As I explored the shelves, each book revealed a new world waiting to be explored. The unpredictability of life never ceases to amaze me. 
        It's in these surprise moments that I find inspiration and a renewed sense of wonder. 
        Embracing the unexpected adds a delightful flavor to the journey of life.

        
        """,
        "output": "surprise",
    },
    {
        "user_input": """
            There's a growing resentment within me, fueled by the constant betrayal and deceit. 
            It's disheartening to witness the actions of those I once trusted. The negative energy surrounding me is suffocating, and it's hard to escape the web of lies.
            Hate is a powerful emotion that takes root when confronted with repeated injustices. The realization that people can be so malicious is painful. 
            Despite attempts to maintain positivity, the hate keeps growing, poisoning every interaction. It's a struggle to find peace amidst the sea of animosity.

        """,
        "output": "hate",
    },
    {
        "user_input": """
            The looming uncertainties of the future cast a shadow over my thoughts. The fear of the unknown, of what lies ahead, grips me tightly. 
            Every decision feels like a leap into the abyss, and the anxiety is overwhelming.
            It's challenging to shake off the fear that holds me back from taking risks. 
            The world seems unpredictable, and the potential for disappointment is paralyzing. 
            Despite the fear, there's a glimmer of hope that encourages me to face the challenges. 
            Confronting these fears head-on becomes a necessary but daunting task.

        """,
        "output": "fear",
    },
]


if __name__ == "__main__":

    # evaluate the system performance
    evaluator = EvaluateTextClassifier()
    evaluation_results, evaluation_df = evaluator.evaluate_response(evaluation_data)

    # pprint(evaluation_results)

    pprint(evaluation_df)

# Textual Sentimen Analysis

### Full Stack AI Engineer Interview Question


**Project Task:**

**Description:**

Develop an AI system for textual sentiment analysis. The system must effectively process text inputs of variable lengths and determine the sentiments encapsulated within the text.

Note: The selection of an AI model for this task is flexible, ranging from utilizing base models to fine-tuning models based on project requirements. The emphasis lies on the implementation of the task and the accuracy of the system rather than the specific model employed.

**Requirements:**

1. The system should seamlessly handle texts of varying lengths, including but not limited to multiple paragraphs.
2. Textual inputs are to be classified on a sentence-by-sentence basis.
3. Sentimental scores must be computed based on the aggregate scores across each category of text labels provided.
4. Input texts are to be categorized into the following sentiment categories: anger, joy, love, surprise, hate, fear, and neutral.

**Determination and Evaluation of Scores**:

1. The system must classify input text on a sentence level into predefined sentiment categories. The overall sentiment of the input text is derived from these scores.
2. The sentiment category with the highest percentage score shall represent the overall sentiment of the provided input text.
3. The input text should be categorized according to the class/category with the highest percentage score.
4. Display the percentage distribution of each sentiment category in the input text in a tabular format, utilizing tools such as Pandas DataFrame or any other suitable tabular format.
5. Present a pie chart plot illustrating the percentage distribution of each sentiment category in the input texts.
6. Utilize a bar chart to visualize the sentimental scores across each sentiment category in the input texts.
7. Develop a user-friendly application (web app or desktop app) capable of receiving user input text and performing sentiment analysis. The application's graphical user interface (GUI) should display the overall sentiment of the input text, the percentage distribution of each sentiment category in a tabular format, along with pie and bar chart plots illustrating the sentiment analysis results.
8. Dockerize both the AI system and the application to facilitate deployment and scalability (Bonus Point).
9. Assess the performance of the AI system using the provided evaluation datasets. The system's performance should be evaluated by comparing predicted sentimental scores against ground truth outputs. Classify the system's performance as "Correct" if the predicted scores match the ground truth, and "Incorrect" otherwise. Ensure the implementation of readable code for this evaluation.

**Evaluation Data**:
```bash
evaluation_data = [
    {
        "user_input":"""
        I can't believe the incompetence I witnessed at work today. The constant delays, the lack of communication – it's infuriating. 
        I put in extra hours to meet deadlines, only to face setbacks caused by others' negligence. 
        The frustration is building up, and it feels like I'm reaching my limit.

        Despite expressing my concerns, it seems like nobody cares about the impact on the team. It's a continuous cycle of disappointment and anger. 
        I need things to change, or I might just explode. The level of inefficiency is unacceptable, and I can't contain my rage anymore.

        """,
        "output":"anger"
    },
     {
        "user_input":"""
            Today was an extraordinary day filled with moments of pure joy. The sun was shining, and I couldn't help but smile as I strolled through the park. 
            I received unexpected good news that lifted my spirits. It's amazing how a simple gesture or a kind word can brighten your entire day.
            Spending time with loved ones added to the joyous atmosphere. Laughter echoed in the air, and for a moment, everything felt perfect. 
            I cherish these moments of happiness, and they remind me of the beauty that surrounds us. 
            Today, joy was the driving force that made every experience memorable.

        """,
        "output":"joy"
    },
     {
        "user_input":"""
            In the quiet moments, I find myself reflecting on the profound love that binds us together. 
            The shared experiences, the support during challenging times – it's the foundation of a deep connection. 
            Love is the guiding force that gives life meaning and purpose.

            Even in the mundane routines, there's a warmth that comes from knowing you are cherished. 
            Small gestures, a gentle touch, and the unspoken understanding create a love that withstands the tests of time. 
            Today, as I express my feelings, it's clear that love is the cornerstone of my existence.

        """,
        "output":"love"
    },
     {
        "user_input":"""
        
        Life has a way of throwing unexpected twists our way. Today, I stumbled upon a hidden gem – a quaint bookstore tucked away in the heart of the city. 
        The discovery took me by surprise, and the joy of finding such a unique place was exhilarating.

        As I explored the shelves, each book revealed a new world waiting to be explored. The unpredictability of life never ceases to amaze me. 
        It's in these surprise moments that I find inspiration and a renewed sense of wonder. 
        Embracing the unexpected adds a delightful flavor to the journey of life.

        
        """,
        "output":"surprise"
    },
     {
        "user_input":"""
            There's a growing resentment within me, fueled by the constant betrayal and deceit. 
            It's disheartening to witness the actions of those I once trusted. The negative energy surrounding me is suffocating, and it's hard to escape the web of lies.
            Hate is a powerful emotion that takes root when confronted with repeated injustices. The realization that people can be so malicious is painful. 
            Despite attempts to maintain positivity, the hate keeps growing, poisoning every interaction. It's a struggle to find peace amidst the sea of animosity.

        """,
        "output":"hate"
    },
     {
        "user_input":"""
            The looming uncertainties of the future cast a shadow over my thoughts. The fear of the unknown, of what lies ahead, grips me tightly. 
            Every decision feels like a leap into the abyss, and the anxiety is overwhelming.
            It's challenging to shake off the fear that holds me back from taking risks. 
            The world seems unpredictable, and the potential for disappointment is paralyzing. 
            Despite the fear, there's a glimmer of hope that encourages me to face the challenges. 
            Confronting these fears head-on becomes a necessary but daunting task.

        """,
        "output":"fear"
    },
    
]
```


**Optional Task**:
Consider implementing logging and tracking mechanisms for experiments or the evaluation results of the AI system using tools such as Comet for enhanced monitoring and analysis.

--------------------------------------------

### Project Demo (Solution)

![text-sentiment-gui-demo](https://github.com/george-mountain/textual-sentiment-analysis/assets/19597087/eb1fa12e-9330-43d7-8cf8-3a0c244c1647)

--------------------------------------------


![piechart-sentiment-sample](https://github.com/george-mountain/textual-sentiment-analysis/assets/19597087/1db75201-5ef8-4069-87de-74d7f288f4af)

![barchart-sentiment-sample](https://github.com/george-mountain/textual-sentiment-analysis/assets/19597087/604af813-0e6d-41e0-b426-507ca09994fe)

------------------------------------------


### Getting Started

1. Fork/Clone the repository:


2. Create a `.env` file on the project root directory and add your OpenAI and COMET API key:

   ```env
   OPENAI_API_KEY=youropenaikey
   COMET_API_KEY=yourcometapikey
   ```



### Running the Application
There are two ways you can run the application:
1. Without Docker:
Navigate to the project root directory and run the streamlit app:
```bash
streamlit run app.py
```

2. With Docker:
Make sure you have Docker installed on your machine if you want to use the Dockerfile in this project, otherwise, you have to run the application locally.

Use the provided Makefile to build and run the Docker container:

```bash
make build
make up
```

This will build the necessary Docker images and start the services.

### Usage

1. Access the Streamlit interface by navigating to [http://localhost:8501](http://localhost:8501) in your web browser.

2. Enter your input text which you want to analyse in the input field and click submit.

3. After the sentimental analysis, the results/plots will be displayed dynamically in the web interface.

### Docker Compose

The project uses Docker Compose to manage the deployment service. The `docker-compose.yml`

### Makefile Commands

- `make build`: Build Docker images.
- `make up`: Start Docker containers in detached mode.
- `make up-v`: Start Docker containers in the foreground.
- `make down`: Stop and remove Docker containers.
- `make down-v`: Stop and remove Docker containers along with volumes.
- `make status`: Show status of Docker containers.
- `make show-logs`: Display logs of all Docker containers.
- `make restart`: Restart Docker containers.
- `make prune`: Remove unused Docker resources.
- `make remove-images`: Remove all Docker images.
- `make stop-container`: Stop a specific Docker container.
- `make remove-container`: Remove a specific Docker container.


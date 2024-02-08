FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel
LABEL maintainer="georgemountain"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501

CMD [ "streamlit","run","app.py" ]

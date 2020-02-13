FROM python:3.8.1-alpine3.11
WORKDIR /app
ADD MainScores.py /app
ADD Scores.txt /app
ADD requirements.txt /app
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["python","/app/MainScores.py"]
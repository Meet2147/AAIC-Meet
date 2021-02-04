FROM python:3.7
COPY aaic.py .
COPY quiz.json .
CMD python3 aaic.py
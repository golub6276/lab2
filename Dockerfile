FROM python:3.11-slim

ARG STUDENT_DIR=Holub

WORKDIR /${STUDENT_DIR}

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lab2.py .

CMD ["python", "lab2.py"]

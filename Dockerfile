FROM python:3.8-slim

WORKDIR /root/
COPY requirements.txt .

# Setup
RUN mkdir output &&\
	python -m pip install --upgrade pip &&\
	pip install -r requirements.txt

# Copy python files
#COPY SA_pred.py /root/
#COPY text_preprocessing.py /root/
COPY ./scripts/*.py /root/

COPY src src

# Expose port to talk
EXPOSE 8080

# Make entrypoint of container
ENTRYPOINT ["python"]
CMD ["SA_pred.py"]

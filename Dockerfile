FROM python:3.8-slim

WORKDIR /root/
COPY requirements.txt .

RUN mkdir output &&\
	python -m pip install --upgrade pip &&\
	pip install -r requirements.txt

COPY SA_pred.py /root/
COPY text_preprocessing.py /root/

COPY src src

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["SA_pred.py"]
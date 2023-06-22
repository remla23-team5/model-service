FROM python:3.9-slim

WORKDIR /app/

COPY requirements.txt .

# Setup
RUN echo "Installing python packages" &&\
  mkdir output &&\
	python -m pip install --upgrade pip &&\
	pip install -r requirements.txt

# Copy python files
COPY ./app /app

# Expose port to talk
EXPOSE 8080

# Make entrypoint of container
ENTRYPOINT ["python"]
CMD ["main.py"]

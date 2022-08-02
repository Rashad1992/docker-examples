FROM python:alpine
WORKDIR /main.py
RUN pip install pymongo 
COPY . /main.py
CMD ["python", "main.py"]
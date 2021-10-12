FROM python:3.8.3
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8001
CMD ["python3", "api.py"]
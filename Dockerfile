FROM python:3.13.5-slim-bullseye 
ENV APP_HOME /app 
WORKDIR $APP_HOME 
COPY requirements.txt . 
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . . 
ENV PORT 8080 
EXPOSE 8080 
CMD ["python", "main.py"] 
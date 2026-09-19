FROM python:3.14
RUN apt update && apt install libgnat-14 -y
WORKDIR /code 
COPY ./requirements.txt /code/requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 
COPY ./app /code/app
COPY ./html /code/.
COPY ./whitakers-words/. /code/
CMD ["fastapi", "run", "app/main.py", "--port", "80"]

FROM python:3.10.5

COPY . /app/app
WORKDIR /app/app

RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ 'unicorn', 'main:data_src_app', '--host', '0.0.0.0']


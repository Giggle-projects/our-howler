FROM python:3.9.18-alpine3.18

COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apk update && apk add git
RUN git config --global user.name "howler.bot"
RUN git config --global user.email "howler.bot@giggle.com"
RUN git add .
ENV TZ Asia/Seoul

CMD [ "python3", "-u", "server/main.py" ]
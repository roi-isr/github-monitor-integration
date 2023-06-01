FROM --platform=linux/amd64 python:3.11

WORKDIR /app

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt update && \
    apt install -y libnss3 && \
    apt install -y software-properties-common && \
    add-apt-repository "deb http://dl.google.com/linux/chrome/deb/ stable main"
RUN apt update && \
    apt install -y google-chrome-stable

# install chrome driver
RUN apt-get install unzip
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin
RUN rm -f /tmp/chromedriver.zip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE ${PORT}

CMD ["./entrypoint.sh"]

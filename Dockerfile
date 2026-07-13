# Используем актуальную стабильную версию Python 3.14 на Debian Slim
FROM python:3.14-slim-bookworm

# Устанавливаем необходимые системные пакеты (Java, Chromium, утилиты)
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    unzip \
    openjdk-17-jre-headless \
    chromium \
    chromium-driver \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем актуальную версию Allure (2.29.0 или новее)
RUN curl -o allure.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.29.0/allure-commandline-2.29.0.tgz \
    && tar -zxvf allure.tgz -C /opt/ \
    && ln -s /opt/allure-2.29.0/bin/allure /usr/local/bin/allure \
    && rm allure.tgz

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем зависимости и устанавливаем их
COPY ./requirements.txt /usr/workspace/
RUN pip install --no-cache-dir -r requirements.txt





# FROM python:3.12.0a4-alpine3.17
# # update apk repo
# RUN echo "https://dl-4.alpinelinux.org/alpine/v3.10/main" >> /etc/apk/repositories && \
#     echo "https://dl-4.alpinelinux.org/alpine/v3.10/community" >> /etc/apk/repositories

# # install chromedriver
# RUN apk update
# RUN apk add --no-cache chromium chromium-chromedriver tzdata

# # Get all the prereqs
# RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
# RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
# RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

# RUN apk update && \
#     apk add openjdk11-jre curl tar && \
#     curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
#     tar -zxvf allure-2.13.8.tgz -C /opt/ && \
#     ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
#     rm allure-2.13.8.tgz

# WORKDIR /usr/workspace

# # Copy the dependencies file to the working directory
# COPY ./requirements.txt /usr/workspace

# # Install Python dependencies
# RUN pip3 install -r requirements.txt
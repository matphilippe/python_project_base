ARG BASE=python:3.11-slim

FROM $BASE

WORKDIR /app

# The aim here is to be flexible with the order in which requirements are setup.
# Feel free to adapt: dependancies that are unlikely to change go before others.

COPY requirements.txt /app/requirements.txt
# COPY requirements_that_changes_a_bit_more_often.txt /app/...

RUN pip install -r requirements.txt 


CMD bash
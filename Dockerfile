FROM python:3.9.1

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install nano
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python setup.py install

CMD ["bash"]

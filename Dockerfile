FROM python:latest
 
WORKDIR /szbot
COPY . /szbot
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "szbot"]

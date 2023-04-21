FROM python:alpine

WORKDIR /root/Suggestion_Box

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "gunicorn", "-c", "configure/gunicorn.conf.py", "run:app" ]
# CMD [ "python", "./run.py" ]

FROM python:3.11-slim

ENV PORT=3000
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY reader.py .

EXPOSE 3000

CMD ["python", "reader.py"]
FROM python:3.10-slim
RUN apt-get update && apt-get install -y ffmpeg && \
    pip install flask yt-dlp
COPY app.py /app/app.py
WORKDIR /app
CMD ["python3", "app.py"]

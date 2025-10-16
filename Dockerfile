# Base: official n8n image
FROM n8nio/n8n

# Switch to root to install extra tools
USER root

# Install ffmpeg + python3 + yt-dlp
RUN apt-get update && \
    apt-get install -y ffmpeg python3-pip && \
    pip install yt-dlp && \
    rm -rf /var/lib/apt/lists/*

# Switch back to n8n user
USER node

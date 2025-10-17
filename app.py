from flask import Flask, request, jsonify
import os, subprocess

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    query = data.get("query", "")
    count = data.get("count", 5)
    out = "/tmp/output.mp4"

    try:
        subprocess.run(
            ["yt-dlp", query, "--max-downloads", str(count),
             "-f", "mp4", "-o", "/tmp/video%(autonumber)s.mp4"], check=True)
        with open("input.txt", "w") as f:
            for i in range(1, count + 1):
                f.write(f"file '/tmp/video{i}.mp4'\n")
        subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i",
                        "input.txt", "-c", "copy", out], check=True)
        return jsonify({"status": "done", "file": out})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload directory
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    # Display upload form
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image Upload</title>
    </head>
    <body>
        <h2>Upload an Image</h2>

        <form method="POST"
              action="/upload"
              enctype="multipart/form-data">

            <input type="file" name="image" accept="image/*">
            <button type="submit">Upload</button>

        </form>
    </body>
    </html>
    """


@app.route("/upload", methods=["POST"])
def upload():
    # Get uploaded file
    file = request.files.get("image")

    # Validate file existence
    if not file or file.filename == "":
        return "No file selected"

    # Generate a safe filename
    filename = secure_filename(file.filename)

    # Save file to upload directory
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )
    file.save(filepath)

    # Display uploaded image
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload Success</title>
    </head>
    <body>
        <h2>Upload Successful</h2>

        <img
            src="/uploads/{filename}"
            style="max-width:600px;"
        >

        <br><br>

        <a href="/">Upload Another Image</a>
    </body>
    </html>
    """


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    # Serve uploaded file
    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


if __name__ == "__main__":
    # Start Flask development server
    app.run(debug=True)
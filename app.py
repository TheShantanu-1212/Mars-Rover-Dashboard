from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)

# Initialize the cameras
cap1 = cv2.VideoCapture(0)  # Camera at index 0
cap2 = cv2.VideoCapture(2)  # Camera at index 2
cap3 = cv2.VideoCapture(6)  # Camera at index 6

# Path to static image for unavailable camera
static_image_path = "static/boss_cat.png"


def generate(camera, use_static_image=False):
    """Generate frames from a specific camera or display static image if unavailable."""
    while True:
        if use_static_image:
            with open(static_image_path, "rb") as f:
                frame = f.read()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
            break
        else:
            success, frame = camera.read()
            if not success:
                break
            _, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def dashboard():
    """Serve the dashboard HTML."""
    return render_template("dashboard.html")


@app.route("/video_feed1")
def video_feed1():
    """Route for Camera 1."""
    if not cap1.isOpened():
        return Response(
            generate(cap1, use_static_image=True),
            mimetype="multipart/x-mixed-replace; boundary=frame",
        )
    return Response(
        generate(cap1), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/video_feed2")
def video_feed2():
    """Route for Camera 2."""
    if not cap2.isOpened():
        return Response(
            generate(cap2, use_static_image=True),
            mimetype="multipart/x-mixed-replace; boundary=frame",
        )
    return Response(
        generate(cap2), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/video_feed3")
def video_feed3():
    """Route for Camera 3."""
    if not cap3.isOpened():
        return Response(
            generate(cap3, use_static_image=True),
            mimetype="multipart/x-mixed-replace; boundary=frame",
        )
    return Response(
        generate(cap3), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

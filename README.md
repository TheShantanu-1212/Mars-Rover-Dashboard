# Mars Rover Dashboard

A web-based dashboard for monitoring and controlling a Mars rover, featuring live video feeds, telemetry, and interactive controls.

## Features

- **Live Camera Feeds:** View up to three real-time video streams from rover cameras.
- **Telemetry Display:** Monitor battery status, IMU (tilt/orientation), wheel RPMs, and communication statistics.
- **Command Log:** See recent commands sent to the rover.
- **Interactive Map:** Visualize rover position and path using Leaflet maps.
- **Robotic Arm Control:** (UI placeholder for future arm control features)
- **Resizable Sidebar:** Adjust the sidebar width for your workflow.
- **Responsive Layout:** Works on desktop and tablets.

## Getting Started

### Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Flask](https://pypi.org/project/Flask/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Mars-Rover-Dashboard.git
   cd Mars-Rover-Dashboard
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Place a fallback image:**
   - If you want a custom image when a camera is unavailable, replace `static/boss_cat.png` with your own JPEG.

### Running the Dashboard

```bash
python app.py
```

- Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Notes

- The dashboard expects up to three cameras connected to your system at indices 0, 2, and 6. Adjust `app.py` if your camera indices differ.
- For demo/testing, the dashboard will show a static image if a camera is not available.

## Screenshot

![main_page_screenshot](https://github.com/user-attachments/assets/875de241-7ce9-4f65-aec6-4c034da7ef00)

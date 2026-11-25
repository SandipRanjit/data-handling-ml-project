
import os
import base64
from pathlib import Path

ASSET_PATH = ("/content/drive/MyDrive/data_handling_and_machine_learning/UI/assets/")

GREEN = "#6FCF97"
PURPLE = "#A05ACB"
BLUE = "#00D6FF"
YELLOW = "#f7ce46"
BLUE_PURPLE = "#7B7EDB"

def load_svg(filename):
    path = os.path.join(ASSET_PATH, filename)

    with open(path, "r") as f:
        return f.read()

def load_svg_as_image(filename):

    svg = load_svg(filename)

    svg = svg.replace(
        "currentColor",
        "#B86CFF"
    )

    encoded = base64.b64encode(
        svg.encode("utf-8")
    ).decode("utf-8")

    return f"data:image/svg+xml;base64,{encoded}"

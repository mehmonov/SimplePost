import gradio as gr
from generate import generate_post
from image import generate_img
from PIL import Image
import numpy as np
import requests
from io import BytesIO

def app(channel_name: str, channel_topic: str, post_title: str, post_description: str):
    # Postni yaratish
    post_text = generate_post(channel_name, channel_topic, post_title, post_description)

    # Rasmni yaratish

    img_url = generate_img(post_description)
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    r = np.array(img)

    return post_text, r

G = gr.Interface(
    fn=app,
    inputs=["text", "text", "text", "text"],
    outputs=[gr.Textbox(), gr.Image()],
)

G.launch()

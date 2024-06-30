from recog import compare
import gradio as gr

def image_classifier(inp):
    return {'cat': 0.3, 'dog': 0.7}

demo = gr.Interface(fn=compare, inputs=["image","image"], outputs="json")
demo.launch()
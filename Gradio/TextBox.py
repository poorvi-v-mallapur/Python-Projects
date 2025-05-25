import gradio as gr

def reverse_text(text):
    return text[::-1]

interface = gr.Interface(
    fn = reverse_text,
    inputs = gr.Textbox(label = "Enter text"),
    outputs = gr.Textbox(label = "Reversed text")
)

interface.launch()
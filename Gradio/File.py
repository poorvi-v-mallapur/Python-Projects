import gradio as gr

def analyze_text(file):
    text = file.name

    with open(text, 'r', encoding = 'utf-8') as f:
        content = f.read()
    word_count = len(content.split())
    return f"The file contains {word_count} words"

interface = gr.Interface(
    fn = analyze_text,
    inputs = gr.File(label = "Upload a text file"),
    outputs = gr.Textbox(label = "Word Count")
)

interface.launch()
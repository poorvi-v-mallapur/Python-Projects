import gradio as gr

def add_nums(a, b):
    return a + b

interface = gr.Interface(
    fn = add_nums,
    inputs = [gr.Number(label = "First Number"), gr.Number(label = "Second Number")],
    outputs = gr.Number(label = "Sum")
)

interface.launch()
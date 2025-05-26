import gradio as gr

def add_nums(a, b, c):
    return a + b + c

interface = gr.Interface(
    fn = add_nums,
    inputs = [gr.Number(label = "First Number"), gr.Number(label = "Second Number"), gr.Number(label = "Third Number")],
    outputs = gr.Number(label = "Sum")
)

interface.launch()
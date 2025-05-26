import gradio as gr

def cube_number(number):
    return number ** 3

interface = gr.Interface(
    fn = cube_number,
    inputs = gr.Slider(minimum=0, maximum=100, step=1,
                       label="Select a number"),
    outputs = gr.Number(label="Result")
)

interface.launch()
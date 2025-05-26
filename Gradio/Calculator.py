import gradio as gr

def calculator(num1, num2, op):
    if op == 'Addition':
        return num1 + num2
    elif op == 'Subtraction':
        return num1 - num2
    elif op == 'Multiplication':
        return num1 * num2
    elif op == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return f'Error: Division by zero'
        
interface = gr.Interface(
    fn = calculator,
    inputs = [
        gr.Number(label = "First Number"),
        gr.Number(label = "Second number"),
        gr.Dropdown(choices = ['Addition', 'Subtraction', 'Multiplication', 'Division'])
    ],
    outputs = gr.Number(label="Result")
)    

interface.launch()
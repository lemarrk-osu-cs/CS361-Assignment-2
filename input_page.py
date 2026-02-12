from nicegui import ui


def on_continue_press(event):
    ui.notify(f"Continue was pressed:")

def on_darkmode_pressed():
    ui.notify('dark mode engaged')

def on_input_validation(value):
    try:
        conv = int(value) 
    except ValueError as e:
        err1 = ui.label(f'Input must a number {e}').on("click",lambda:err1.classes('opacity-0'))
    if conv <= 0:
        err2 = ui.label(f'Input must a number greater than 0').on("click",lambda:err2.classes('opacity-0'))

with ui.row().classes('h-screen w-full items-center justify-center'):
        with ui.column(align_items='center').classes('w-120 items-center justify-center'):
             ui.label('Budget Input')
             with ui.card().classes('flex-grow').classes('w-full items-center'):
                ui.input(placeholder='Input Monthly Amount', on_change=lambda e: result.set_text('You entered!' + e.value),
                     validation=on_input_validation).props('clearable').classes('w-90')
                ui.input(placeholder='Input Weekly Amount', on_change=lambda e: result.set_text('You entered!' + e.value),
                        validation=on_input_validation).props('clearable').classes('w-90')
                              
                ui.button('Continue',on_click=on_continue_press).classes('w-full')  
                ui.button("Dark Mode",on_click=on_darkmode_pressed).classes('w-full')    


ui.run(title="Input Page")
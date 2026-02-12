from nicegui import ui

def on_continue_press(event):
    ui.notify(f"""Continue was pressed: {event}""")

def on_darkmode_pressed():
    ui.notify('dark mode engaged')

def on_input_validation(value):
    try:
        conv = int(value) 
    except ValueError as e:
        ui.label(f'Input must a number {e}')
    if conv <= 0:
        ui.label(f'Input must a number greater than 0')

with ui.column().classes('fixed-center max-w-3xl'):
    with ui.column().classes('w-full items-center'):
        ui.label('Budget Input')
        with ui.card().classes('flex-grow').classes('w-full items-center'):
            m_amount = ui.input(placeholder='Input Monthly Amount',
                                on_change=lambda e: e.set_text('You entered!' + e.value),
                validation=on_input_validation).props('clearable').without_auto_validation()
        
            w_amount = ui.input(placeholder='Input Weekly Amount', 
                                 on_change=lambda e: e.set_text('You entered!' + e.value),
                validation=on_input_validation).props('clearable').without_auto_validation()
            
            cont_click = ui.button('Continue',on_click=on_continue_press)   
            d_mode = ui.button("Dark Mode",on_click=on_darkmode_pressed)

ui.run(title="Input Page")
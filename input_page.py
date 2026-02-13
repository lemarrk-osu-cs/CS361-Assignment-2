from nicegui import ui, app


def on_continue_pressed(event):
    ui.navigate.to('/account_summary')

def on_input_monthly_validation(value):
    conv:int
    try:
       conv = int(value) 
    except ValueError as e:
        err1 = ui.label(f'Monthly input must a number {e}').on("click",lambda:on_click_delete_label(err1))
    if conv <= 0:
        err2 = ui.label(f'Monthly input must a number greater than 0').on("click",lambda:on_click_delete_label(err2))

def on_input_weekly_validation(value):
    conv:int
    try:
        conv = int(value) 
    except ValueError as e:
        err3 = ui.label(f'Weekly input must a number {e}').on("click",lambda:on_click_delete_label(err3))
    if conv <= 0:
        err4 = ui.label(f'Weekly input must a number greater than 0').on("click",lambda:on_click_delete_label(err4))

def on_click_delete_label(label):
     label.delete()

def on_change_input_one(e):
     label_one.set_text(f'You entered!{e.value}')

def on_change_input_two(e):
     label_two.set_text(f'You entered!{e.value}')

def on_click_help_button():
    ui.notify("""Hello and Thank You for using this app. Please input your monthly amount of funds to spend minus your 
              known monthly expenditures. By continuing to use the features of this page you can easily input all 
              information needed to set your monthly, weekly and daily budget""")

def on_click_dark_mode():
   ui.dark_mode().bind_value(app.storage.user,'dark_mode')

@ui.page('/')
def input_page():
    with ui.row().classes('h-screen w-full items-center justify-center'):
        with ui.column(align_items='center').classes('w-120 items-center justify-center'):
             ui.label('Budget Input').classes('w-120 text-center p5')
             ui.button('Help?',color='red', on_click=on_click_help_button).classes('text-white w-120')
             with ui.card().classes('flex-grow').classes('w-full items-center'):
                label_one = ui.input(placeholder='Input Monthly Amount', on_change=on_change_input_one,
                     validation=on_input_monthly_validation).props('clearable').classes('w-90')
                label_two = ui.input(placeholder='Input Weekly Amount', on_change=on_change_input_two,
                     validation=on_input_weekly_validation).props('clearable').classes('w-90')
                              
                ui.button('Continue',on_click=on_continue_pressed).classes('w-full')  
                ui.button("Dark Mode",on_click=on_click_dark_mode).classes('w-full')    

@ui.page('/account_summary')
def account_summary():
    with ui.row().classes('h-screen w-full items-center justify-center'):
        with ui.column(align_items='center').classes('w-120 items-center justify-center'):
             ui.label('Account Summary Page').classes('w-120 text-center').style('font-size:20px')
             ui.button("Dark Mode",on_click=on_click_dark_mode).classes('w-full') 

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Input Page", storage_secret='901')
from nicegui import ui, app
from datetime import datetime as time

def make_dark():
    ui.dark_mode().toggle()

def on_click_delete_label(err):
    err.delete()

def on_click_continue_pressed():
    ui.navigate.to('/account_summary')

def on_input_monthly_validation(value):
    conv:int
    try:
       conv = int(value) 
    except ValueError as e:
        err1 = ui.label(f'Monthly input must a number {e}').on("click",lambda:on_click_delete_label(err1)).style('font-size:18px')
    if conv <= 0:
        err2 = ui.label(f'Monthly input must a number greater than 0').on("click",lambda:on_click_delete_label(err2)).style('font-size:18px')

def on_input_monthly_expenses_validation(value):
    conv:int
    try:
        conv = int(value) 
    except ValueError as e:
        err3 = ui.label(f'Weekly input must a number {e}').on("click",lambda:on_click_delete_label(err3)).style('font-size:18px')
    if conv <= 0:
        err4 = ui.label(f'Weekly input must a number greater than 0').on("click",lambda:on_click_delete_label(err4)).style('font-size:18px')

def on_change_input_one(e):
     app.storage.user['val1'] = e.value

def on_change_input_two(e):
     app.storage.user['val2'] = e.value

def on_click_input_help_button():
   ui.notify("""Hello and Thank You for using this app. Please input your monthly expenditures of and your 
              known monthly income. By continuing to use the features of this page you can easily input all 
              information needed to set your monthly, weekly and daily budget! Just press "Continue" or the "Arrow Keys"
              when you are done to be able to calculate your budget for Weekly and Daily amounts.
              """,timeout=10000).style('font-size:18px')

def on_click_account_help_button():
    ui.notify("""Your monthly and weekly information needed to set your daily budget
              is here. The daily allowance is calculated by the number of days in the month divided into the monthly amount.
              The weekly amount is very similarly calculated as the number of weeks divided into the monthly
               amount of income given.
             """,timeout=10000).style('font-size:18px')

def on_click_navigate_to_summary():
    ui.navigate.to('/account_summary')

def on_click_navigate_to_root():
    ui.navigate.to('/')

def calc_daily():
    fmt = time.now()
    return str(fmt.today())

@ui.page('/')
def input_page():
    with ui.row().classes('h-screen w-full items-center justify-center'):
            ui.button('<-').style('font-size:18px') 
            with ui.column(align_items='center').classes('w-120 items-center justify-center'):
                ui.label('Budget Input').classes('w-120 text-center').style('font-size:30px').style('font-size:18px')
                ui.button('Help?',color='red', on_click=on_click_input_help_button).classes('text-white w-120').style('font-size:18px')
                with ui.card().classes('flex-grow').classes('w-full items-center'):
                    ui.input(placeholder='Input Monthly Income', on_change=on_change_input_one,
                        validation=on_input_monthly_validation).props('clearable').classes('w-90').style('font-size:18px')
                    ui.input(placeholder='Input Monthly Expenses', on_change=on_change_input_two,
                        validation=on_input_monthly_expenses_validation).props('clearable').classes('w-90').style('font-size:18px')             
                    ui.button('Continue',on_click=on_click_continue_pressed).classes('w-full').style('font-size:18px') 
                    ui.button("Dark Mode",on_click=make_dark).classes('w-full').style('font-size:18px') 
            ui.button('->',on_click=on_click_navigate_to_summary).style('font-size:18px')

@ui.page('/account_summary')
def account_summary():
    with ui.row().classes('h-screen w-full items-center justify-center'):
        ui.button('<-',on_click=on_click_navigate_to_root).style('font-size:18px')
        with ui.column(align_items='center').classes('w-120 items-center justify-center'):
           ui.label('Account Summary Page').classes('w-120 text-center').style('font-size:30px').style('font-size:18px')
           ui.button('Account Summary?',color='red', on_click=on_click_account_help_button).classes('text-white w-120').style('font-size:18px')
           with ui.card().classes('flex-grow').classes('w-full items-center'):
                ui.html(f'Monthly Income: {app.storage.user.get('val1')}',).classes('w-90').style('font-size:18px')
                ui.html(f'Monthly Expenses: {app.storage.user.get('val2')}').classes('w-90').style('font-size:18px')
                ui.label(text='').text = calc_daily()
                ui.button("Dark Mode",on_click=make_dark).classes('w-full').style('font-size:18px')
        ui.button('->').style('font-size:18px')

ui.run(title="Input Page", storage_secret='901',dark=False)
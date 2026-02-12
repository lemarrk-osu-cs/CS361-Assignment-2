from nicegui import ui


with ui.column().classes('fixed-center'):
    with ui.column().classes('w-full items-center'):
        ui.label('Budget Input')
        with ui.card().classes('flex-grow').classes('w-full items-center'):
            ui.input( placeholder='Input Monthly Amount',on_change=lambda e: result.set_text('you clicked!' + e.value),
                validation={'Input must be greater than zero ': lambda value: len(value) > 0})
            ui.input( placeholder='Input Weekly Amount',on_change=lambda e: result.set_text('you clicked!' + e.value),
                validation={'Input must be greater than zero ': lambda value: len(value) > 0})
            ui.button('Continue')   
            ui.button("Dark Mode",on_click=lambda:ui.notify('dark mode engaged'))

ui.run(title="Input Page")
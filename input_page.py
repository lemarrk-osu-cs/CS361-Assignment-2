from nicegui import ui


with ui.column().classes('fixed-center'):
    ui.label('Budget Input')
    with ui.card().classes('flex-grow'):
        ui.input( placeholder='Input Monthly Amount',on_change=lambda e: result.set_text('you clicked!' + e.value),
                validation={'Input must be greater than zero ': lambda value: len(value) > 0})
        ui.input( placeholder='Input Weekly Amount',on_change=lambda e: result.set_text('you clicked!' + e.value),
                validation={'Input must be greater than zero ': lambda value: len(value) > 0})
        ui.button('Continue')

ui.run(title="Input Page")
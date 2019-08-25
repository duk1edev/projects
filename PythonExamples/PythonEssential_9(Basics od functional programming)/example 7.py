handlers = []
for i in range(1, 4):
    def on_click():
        print(f'Button {i} clicked')


    handlers.append(on_click())

for handler in handlers:
    handler

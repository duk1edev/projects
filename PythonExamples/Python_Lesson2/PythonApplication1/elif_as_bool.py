is_ready = True

if is_ready:
    state_msg = "Ready"
else:
    state_msg = "Not ready yet!"

state_msg1 = is_ready and "Ready" or "Not READY YET!"

state_msg2 = "Ready" if is_ready else "Not Ready YETYYY!"

print(state_msg)
print(state_msg1)
print(state_msg2)

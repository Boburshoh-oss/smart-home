async def message_handler(message, websocket):
    # process message here
    print(message)
    
    # You can also send the message back to server
    await websocket.send("Message received from client")



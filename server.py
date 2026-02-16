import asyncio # behövs för att skapa en asynkron server

# Funktion för att hantera varje klient som ansluter
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Connected: {addr}')

    writer.write(b'Thank you for connecting\n')
    await writer.drain() # drain gör att vi väntar tills data har skickats innan vi fortsätter

    # Läs data från klienten i en loop tills klienten stänger anslutningen
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(b'Server received: ' + data)
        await writer.drain()

    writer.close()

# Huvudfunktion som startar servern
async def main():
    PORT = 40674
    print(f'Server listening on port {PORT}...')

    #  starta servern på port och ange handle_client för att hantera varje anslutning
    server = await asyncio.start_server(handle_client, '', PORT)

    async with server:
        await server.serve_forever()

asyncio.run(main())

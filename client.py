# Vi behöver socket modulen för att skapa en klient som kan ansluta till servern
import socket

# Skapa ett socket-objekt
s = socket.socket()

# Vilken port servern lyssnar på
PORT = 40674

# Anslut till servern på localhost (eller annan IP-adress)
s.connect(('127.0.0.1', PORT))

# Ta emot välkomstmeddelande från servern
print(s.recv(1024).decode())

# Skicka meddelanden till servern
s.send("Jag kopplar upp mig från klienten.".encode())

# Ta emot svar från servern
response = s.recv(1024)
print(f'Svar från server: {response.decode()}')

# Stäng anslutningen
s.close()
print('Anslutningen stängd')

# steganography_chat

Opis projektu:
Jest to chat typu IRC ze steganografią - szyfrowaniem wiadomości w przesyłanym pliku graficznym.
Serwer działa na dwóch wątkach - w jednym zapisuje wysłane do niego wiadomości, w drugim zaś wysyła je do klientów, jeśli otrzyma odpowiednie zapytanie. Klient jednym wątkiem tworzy GUI i wysyła wiadomości, a drugiego używa do odpytywania serwera i odbierania ich. W przypadku potencjalnego klienta nieposiadającego funkcji dekodującej, otrzymałby jedynie zdjęcie.

Połączenie między klientem a serwerem jest realizowane przy pomocy gniazd BSD na TCP.

Moduły:
  client:
      client.py - nawiązuje połączenie i odbiera wiadomości z serwera
      steganography.py - zawiera funkcje potrzebne do kodowania i rozkodowania wiadomości
      view.py - tworzy interfejs graficzny, koduje i wysyła wiadomości
      settings.py - zawiera ustawienia portów i użytkownika

  server:
      server.cpp - zajmuje się łącznością między klientami, przechowuje historię wiadomości


Uruchamianie:
server.cpp: g++ --std=c++11 -Wall -O0 -g -pthread -o server server.cpp
client: python3 client.py

Autorzy:
Piotr Ceranek
Michał Chatłas

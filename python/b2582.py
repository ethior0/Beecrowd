C = int(input());

musicas = ["PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!", "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"]

for _ in range(C):
  X, Y = map(int, input().split());
  print(musicas[X+Y]);
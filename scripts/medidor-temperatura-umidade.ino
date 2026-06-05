// LANGUAGE: Lua
// ENV: Arduino | ESP
// AUTHOR: Jackson Roberio
// Code that reads the temperature and humidity of the place and displays in console. 
// Note you must have the DHT component to read the temperature and humidity.

#include <DHTesp.h>

// --- DHT ---
/**
* Lybrary para consumir o dispositivo
* de leitor de temperatura.
*/
#include <DHT.h>

#define DHTPIN D3
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

/**
* Ao rodar no console, atente-se
* para a porta 115200
*/
void setup() {
  Serial.begin(115200);
}

void loop() {
  int umidade = dht.readHumidity();
  int temperatura = dht.readTemperature(false);
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.print("°C");
  Serial.print("   ");
  Serial.print("Umidade: ");
  Serial.println(umidade);
  delay(5000);
}

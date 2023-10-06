const int ledPin = 13; // The built-in LED on Arduino Uno
const long dotDelay = 250; // Duration of a dot (in milliseconds)
const long dashDelay = dotDelay * 3; // Duration of a dash (3 times the dot)

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  char message[] = "HELLO WORLD";
  
  for (int i = 0; message[i] != '\0'; i++) {
    char c = toupper(message[i]);
    
    if (c == ' ') {
      // Space between words (7 dots duration)
      delay(dotDelay * 7);
    } else {
      // Transmit the Morse code for the character
      transmitMorseCode(c);
      
      // Gap between characters (3 dots duration)
      delay(dotDelay * 3);
    }
  }
  
  // Gap between messages (7 dots duration)
  delay(dotDelay * 7);
}

void transmitMorseCode(char c) {
  switch (c) {
    case 'A':
      dot();
      dash();
      break;
    case 'B':
      dash();
      dot();
      dot();
      dot();
      break;
    case 'C':
      dash();
      dot();
      dash();
      dot();
      break;
    case 'D':
      dash();
      dot();
      dot();
      break;
    case 'E':
      dot();
      break;
    case 'F':
      dot();
      dot();
      dash();
      dot();
      break;
    case 'G':
      dash();
      dash();
      dot();
      break;
    case 'H':
      dot();
      dot();
      dot();
      dot();
      break;
    case 'I':
      dot();
      dot();
      break;
    case 'J':
      dot();
      dash();
      dash();
      dash();
      break;
    case 'K':
      dash();
      dot();
      dash();
      break;
    case 'L':
      dot();
      dash();
      dot();
      dot();
      break;
    case 'M':
      dash();
      dash();
      break;
    case 'N':
      dash();
      dot();
      break;
    case 'O':
      dash();
      dash();
      dash();
      break;
    case 'P':
      dot();
      dash();
      dash();
      dot();
      break;
    case 'Q':
      dash();
      dash();
      dot();
      dash();
      break;
    case 'R':
      dot();
      dash();
      dot();
      break;
    case 'S':
      dot();
      dot();
      dot();
      break;
    case 'T':
      dash();
      break;
    case 'U':
      dot();
      dot();
      dash();
      break;
    case 'V':
      dot();
      dot();
      dot();
      dash();
      break;
    case 'W':
      dot();
      dash();
      dash();
      break;
    case 'X':
      dash();
      dot();
      dot();
      dash();
      break;
    case 'Y':
      dash();
      dot();
      dash();
      dash();
      break;
    case 'Z':
      dash();
      dash();
      dot();
      dot();
      break;
    default:
      // If the character is not in our Morse code table, ignore it.
      break;
  }
  
  // Gap between dots and dashes within a character (1 dot duration)
  delay(dotDelay);
}

void dot() {
  digitalWrite(ledPin, HIGH);
  delay(dotDelay);
  digitalWrite(ledPin, LOW);
  delay(dotDelay);
}

void dash() {
  digitalWrite(ledPin, HIGH);
  delay(dashDelay);
  digitalWrite(ledPin, LOW);
  delay(dotDelay);
}

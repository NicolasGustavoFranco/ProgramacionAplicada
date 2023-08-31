int ResVerde = 23;
int botonAzul = 4;
#define  ledVerde 33
#define  ledAzul 25

void setup() {
  Serial.begin(9600);
  pinMode(ResVerde,  INPUT_PULLDOWN);
  pinMode(botonAzul,  INPUT_PULLDOWN);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAzul, OUTPUT);
}

void loop(){ 
  int estadoBoton1;
  int estadoBoton2;

  estadoBoton1 = digitalRead(ResVerde);
  Serial.println(estadoBoton1);
  delay(10);
  estadoBoton2 = digitalRead(botonAzul);
  delay(10);
    
  if(estadoBoton1 == HIGH){
  Serial.println("Boton Verde Pulsado");

  digitalWrite(ledVerde, HIGH);
  

  }
  else{
    digitalWrite(ledVerde, LOW);
  }

  if(estadoBoton2 == HIGH){
  Serial.println("Boton Azul Pulsado");

  digitalWrite(ledAzul, HIGH);
  
  }
  else{
    digitalWrite(ledAzul, LOW);
  }

}  

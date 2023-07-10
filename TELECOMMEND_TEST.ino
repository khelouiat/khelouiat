#define dureeMinimaleImpulsionCommandeESC     1000        // La durée minimale pour une impulsion est de 1000 µs, soit 1 ms (comme pour un servomoteur, en fait)
#define dureeMaximaleImpulsionCommandeESC    2000        // La durée maximale pour une impulsion est de 2000 µs, soit 2 ms (comme pour un servomoteur, idem donc)

#include <ethernet_comp.h>
#include <UIPClient.h>
#include <UIPEthernet.h>
#include <UIPServer.h>
#include <UIPUdp.h>
int packetBuffer;
String datReq; //String for our data
int packetSize; //Size of Packet
EthernetUDP Udp; //Define UDP Object
// #include <enc28j60.h>
// #include <EtherCard.h>
// #include <net.h>
int dureeImpulsionCommandeESC1;
int dureeImpulsionCommandeESC2;
int dureeImpulsionCommandeESC3;
int dureeImpulsionCommandeESC4;
// #include <SPI.h>        
// #include <Ethernet.h>
// #include <EthernetUdp.h>
    

byte mac[] = {  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEE };
IPAddress ip(192, 168, 1, 200);    // local IP - address of my Arduino 
unsigned int localPort = 5000;      // local port to listen - default X-Plane port 
byte buf = 00;   // buffer for  UDP packet (BYTE, not char)

//EthernetUDP Udp; // An EthernetUDP instance to send and receive packets over UDP

//-------------------------------------------------------------------------------

void setup() 
{
  Ethernet.begin(mac,ip);   // start the Ethernet 
  Udp.begin(localPort);     //..and UDP
}
void loop() {

  int packetSize = Udp.parsePacket();
 Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());  //Initialize Packet send
 int sensorValue1 = analogRead(A0);
  int sensorValue2 = analogRead(A1);
  int sensorValue3 = analogRead(A2);
  
 dureeImpulsionCommandeESC1 = map(sensorValue1, 0, 1023, dureeMinimaleImpulsionCommandeESC, dureeMaximaleImpulsionCommandeESC);
 dureeImpulsionCommandeESC2 = map(sensorValue3, 0, 1023, dureeMinimaleImpulsionCommandeESC, dureeMaximaleImpulsionCommandeESC);
  //dureeImpulsionCommandeESC3 = map(sensorValue3, 0, 1023,  dureeMinimaleImpulsionCommandeESC, dureeMaximaleImpulsionCommandeESC);
  //dureeImpulsionCommandeESC4 = map(sensorValue3, 0, 1023,   dureeMaximaleImpulsionCommandeESC,dureeMinimaleImpulsionCommandeESC);
  dureeImpulsionCommandeESC4 = (dureeImpulsionCommandeESC1+dureeImpulsionCommandeESC2)/2;
  
  
   Udp.print(dureeImpulsionCommandeESC1); //Send string back to client 
    Udp.print(",");
    Udp.print(dureeImpulsionCommandeESC2); //Send string back to client
    Udp.print(","); 
    Udp.print(1); //Send string back to client 
    Udp.print(","); 
    Udp.print(dureeImpulsionCommandeESC4);
    Udp.print(","); 
    Udp.print(2);
    Udp.endPacket(); //Packet has been sent
  
delay(50);

}

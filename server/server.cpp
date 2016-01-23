#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <time.h>
#include <ctime>

#define SERVER_PORT 1234
#define QUEUE_SIZE 5

class Message {

    private:
     int timestamp;
     int** lena;

    public:
     Message(int** input_lena) {
        this->lena = input_lena;
        this->timestamp = std::time(0);
     }
     Message() {}
     int get_timestamp() {
        return this->timestamp;
     }
     int** get_lena() {
        return this->lena;
     }
};

class History {
    private:
     int newest_index;
     Message* message_list;

    public:
     History() {
        this->newest_index = 0;
        this->message_list = new Message[100];
     }
     int get_newest_index() {
        return this->newest_index;
     }
     Message get_message(int index) {
        return this->message_list[index];
     }
     void insert_message(Message new_message) {
        this->newest_index += 1;
        this->newest_index = (this->newest_index%100);
        this->message_list[this->newest_index] = new_message;
     }
};

int main() {

   int nSocket, nClientSocket;
   int nBind, nListen;
   int nFoo = 1;
   socklen_t nTmp;
   struct sockaddr_in stAddr, stClientAddr;


   /* address structure */
   memset(&stAddr, 0, sizeof(struct sockaddr));
   stAddr.sin_family = AF_INET;
   stAddr.sin_addr.s_addr = htonl(INADDR_ANY);
   stAddr.sin_port = htons(SERVER_PORT);

   /* create a socket */
   nSocket = socket(AF_INET, SOCK_STREAM, 0);
   setsockopt(nSocket, SOL_SOCKET, SO_REUSEADDR, (char*)&nFoo, sizeof(nFoo));

   /* bind a name to a socket */
   nBind = bind(nSocket, (struct sockaddr*)&stAddr, sizeof(struct sockaddr));

   /* specify queue size */
   nListen = listen(nSocket, QUEUE_SIZE);

   while(1)
   {
       /* block for connection request */
       nTmp = sizeof(struct sockaddr);
       nClientSocket = accept(nSocket, (struct sockaddr*)&stClientAddr, &nTmp);

           printf("[connection from: %s]\n", inet_ntoa((struct in_addr)stClientAddr.sin_addr));
           time_t now;
           struct tm *local;
           time (&now);
           local = localtime(&now);
           char buffer[50];
           int n;
           n = sprintf(buffer, "%s\n", asctime(local));
           write(nClientSocket, buffer, n);
           close(nClientSocket);
       }

   close(nSocket);
   return(0);
}

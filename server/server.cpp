#include <cstdlib>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <iostream>
#include <ctime>

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

    int** dupa;
    dupa = new int*[512];
    for (int i = 0; i <512; i++) {
        dupa[i] = new int[512];
    }
    dupa[3][4] = 33;

    Message* test = new Message(dupa);
    test->get_lena()[123][7] = 666;

    History* common_message_history = new History();

    for (int i = 0; i < 1123; i++) {
        common_message_history->insert_message(*test);
    }

    std::cout<<common_message_history->get_newest_index()<<std::endl<<common_message_history->get_message(3).get_lena()[123][7];
}

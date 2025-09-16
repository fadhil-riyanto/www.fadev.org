# Resume alpro double linkedlists

langsung saja ini kodenya, 3 kode bebas, disini saya wrap di func saja karna agar tidak perlu buat banyak file. 

penjelasan kode ADA DIBAGIAN BAWAH SNIPPET KODE ini.

```cpp
#include <cstddef>
#include <iostream>

using namespace std;

struct Node {
  int data;
  Node *prev;
  Node *next;
};

Node *create_node(int data) {
  Node *newly_created_node = new Node;

  newly_created_node->data = data;
  newly_created_node->next = nullptr;
  newly_created_node->prev = nullptr;

  return newly_created_node;
}

void print(Node *head) {
  Node *current = head;
  cout << "Informasi tentang setiap node:" << endl;
  while (current != nullptr) {
    cout << "Alamat: " << current << endl;
    cout << "Nilai: " << current->data << endl;
    cout << "Alamat prev: " << current->prev << endl;
    cout << "Alamat next: " << current->next << endl << endl;
    current = current->next;
  }
  cout << "---------------------------------------" << endl;
}

void insert_last(Node *&head, int data) {
  Node *newly_created_node = create_node(data);
  if (head == nullptr) {
    head = newly_created_node;
  } else {
    Node *current = head;

    while (current->next != nullptr) {
      current = current->next;
    }

    current->next = newly_created_node;
    newly_created_node->prev = current;
  }
}

void insertFirst(Node *&head, int data) {
  Node *newNode = create_node(data);
  if (head == nullptr) {
    head = newNode;
  } else {
    newNode->next = head;
    head->prev = newNode; 
    head = newNode;
  }
}

void delete_first(Node *&head) {

  if (head == nullptr) {
    printf("node kosong\n");
  }

  Node *temp = head;
  head = head->next;

  if (head != nullptr) {
    head->prev = nullptr;
  }

  delete temp;
}

int main() {
  Node *head = nullptr;

  head = create_node(7);
  insert_last(head, 1);
  insert_last(head, 10);
  delete_first(head);
  insertFirst(head, 99);

  print(head);
}
```

### func `create_node`
Walau bukan bagian dari tugas, saya sekalian jelaskan saja. intinya func ini membuat node baru, yang isinya prev dan next, diisi nullptr (alias nullpointer), dan datanya.

jadi maksud func ini, kita bikin node yang bener2 kosong tanpa terhubung ke siapapun. lalu return value nya.

### func `insert_last`
Cara kerjanya spt ini. 

- kita buat dulu node nya (node yg tidak terhubung dgn siapapun pakai create_node)
- lalu cek, misalkan head yg dari func `main` itu masih nullptr (karna emang defaultnya nullptr), maka pertanda linked listsnya masih kosong, maka kita bisa timpa saja.
- jika tidak? kita simpan dulu node saat ini, anggap saja namanya current
- sudah kesimpan kan? current kita arahkan ke `current->next`, alhasil dia ngakses pointer selanjutnya, lalu cek apakah dia nullptr atau bukan (sbg penanda)
- misal iya, maka saatnya berhenti, lalu sambung, intinya karna dibelakang nullptr, maka untuk nyambungnya, nullptr kita ganti saja pakai address node yang barusan dibuat.
- agar bisa nyambung kebelaknng, maka prev (previus miliknya new node) kita timpa pakai current, kenapa? node yg terbaru itu prev nya masih nullptr, agar nyambung, maka kita harus isi dengan node sebelumnya yg sudah disimpan.

nb: `Node *&head` artinya nge-deferensi pointer, sekaligus kalau ada perubahan data, sekalian di update, jadi misal ubah data di func delete_last, maka kalau dibaca oleh insert_first, data yg kita share tetep singkron

### func `insertFirst` 
nah, ini func paling easy wkwk, karna head guarantee akan selalu point ke depan, maka untuk nyispin data didepan sangatlah easy.

buat node baru, lalu node baru (next nya) diisi head.
untuk prev (milik nya node lama) kita addr node baru.

### func `delete_first`
konsepnya mirip dengan insert first, hanya saja

- karna head selalu point ke depan, maka kita perlu simpan head (yang sekarang), lalu saatnya pindah state ke node sebelahnya (kekanan)
- lalu lanjut mark bahwa head->prev itu nullptr, artinya headnya pindah.
- ok sudah, nah, head yang tadi disimpan, bisa di hapus pakai `delete`

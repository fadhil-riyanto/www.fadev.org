# Tree

Apa itu tree? tree adalah struktur data, dimana bentuknya menyerupai tree (perumpamaan saja), aslinya structur data ini berbentuk mirip linkedlists-double hanya saja, perumpamaan cabang kiri (diganti dgn nama prev), cabang kanan (diganti dgn nama next)

## Perbedaan
- Linkedlists itu monoton, alias saling sambung menyambung dan flat. 
- sedangkan tree tidak ada aturan harus saling menyambung, bisa saja linkedlists nya seperti ini 

`root -> next -> next -> next` (dimana ini nanti akan membuat tree yang gambar visualnya bakal menjorok kekanan)

## jenis jenis transversal
- preorder (root, kiri, lalu ke-kanan)
- inorder (kiri, root, lalu ke-kanan)
- postorder (kiri, kanan, lalu ke-root)

nb: tranversal adalah cara mengunjungi simpul (tepat satu kali saja)

## coding
sudah cukup hal non teknisnya, bagian ini akan membahas bagian koding

## struct
struct untuk tree sangat mirip dgn struct untuk linked-list-double. di kasus ini struct dibawah hanya bisa hold data char saja. bisa diganti juga dgn int. dan lain lain

```c
struct ListNode {
        char val;
        ListNode *prev;
        ListNode *next;

        ListNode(char x) : val(x), prev(nullptr), next(nullptr) {}
};
```

terlihat? selain hold data `val` yang isinya char, kita ada opsi untuk hold pointer prev dan pointer next. dimana ini adalah kunci dari tree.

## contoh meng-isinya

ada tree seperti ini
![image](/../_images/44cc7ec324a3454a5419ed656412246ae1548b060c631f05fac4829d3a41d4966443696f0942c5ec088680984a7e60565ebbd45e01d0298a1b7bc6b3.png)

ini contoh cara mengisinya
```c
ListNode *head = new ListNode('A');
head->prev = new ListNode('B');
head->prev->prev = new ListNode('D');
head->prev->prev->next = new ListNode('G');

head->next = new ListNode('C');
head->next->next = new ListNode('F');
head->next->prev = new ListNode('E');
head->next->prev->prev = new ListNode('H');
head->next->prev->next = new ListNode('I');
```

kenapa tidak pakai val? karna ketika kita `new ListNode('H');`, secara otomatis kita mengisi val. val baru dipakai ketika mau diakses. 

## contoh cara mengaksesnya
contoh singkat ada dibawah, contoh (komplit) nya silahkan [klik disini](https://drive.google.com/drive/folders/1lfvxDxCctEnp2Yg8H0ws7NgH1yMxDEZT?usp=sharing)

### inorder
```c
cout << "step 1: " << head->prev->prev->next->val <<
" " << head->prev->prev->val <<
" " << head->prev->val <<
" " << head->val <<
" " << head->next->prev->prev->val <<
" " << head->next->prev->val <<
 " " << head->next->prev->next->val <<
 " " << head->next->val <<
" " << head->next->next->val <<
endl;
```
### postorder
```c
cout << "step 9: " << head->prev->prev->next->val << 
" " << head->prev->prev->val << 
" " << head->prev->val << 
" " << head->next->prev->prev->val << 
" " << head->next->prev->next->val << 
" " << head->next->prev->val << 
" " << head->next->next->val <<
" " << head->next->val <<
" " << head->val <<

endl;
```

### preorder
```c
cout << "step 8: " << head->val << 
" " << head->prev->val << 
" " << head->prev->prev->val <<
" " << head->prev->prev->next->val << 
" " << head->next->val << 
" " << head->next->prev->val <<
" " << head->next->prev->prev->val <<
" " << head->next->prev->next->val <<
" " << head->next->next->val << endl;

```
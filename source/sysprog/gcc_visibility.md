# gcc compiler visibility

intresting buat diulik

```cpp
class rectangle {
        int width, height;

        public:
                void set_value(int, int);
                int area();
};

void rectangle::set_value(int x, int y) 
{
        width = x;
        height = y;
}


int rectangle::area()
{
        return width * height;
}

```

compile pakai 
- `g++ -Wall -c -fPIC abc.cc`
- `g++ -o librec.so --shared abc.o`
- `nm -C librec.so`

akan ada
```text
000000000000110e T rectangle::area()
00000000000010ea T rectangle::set_value(int, int)
```

nah, disitu kalau di compile pakai `-fvisibility=hidden`
ntar pas di cek pakai 
`nm -CD librec.so `

bakalan gak ada. nah ini ada kaitannya sama
`__attribute__ ((visibility ("hidden")))`

tambahan: [https://groups.google.com/g/ode-users/c/T3qiy-4dviQ](https://groups.google.com/g/ode-users/c/T3qiy-4dviQ)
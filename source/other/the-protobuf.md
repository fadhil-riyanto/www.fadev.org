# Protobuf

protobuf ini intinya format pertukaran data, mirip json, tapi dia pakai schema (mirip graphql), agak kaku, dan ada method2

baca spec: [https://protobuf.dev/programming-guides/proto3/](https://protobuf.dev/programming-guides/proto3/)

ini termasuk prelude nya

```protobuf
syntax = "proto3";

// this is namefile 
package grpc.fadhil;
```

lalu ini anggap saja seperti struct, jika di C biasanya sent data over file pakai struct.

```protobuf
message Message1 {}

message Message2 {
  Message1 foo = 1;
}

```

baru kita define semacam namespace yang didalamnya hold func func yang akan dicall oleh grpc
```protobuf
service SearchService {
  rpc Search(SearchRequest) returns (SearchResponse);
}
```



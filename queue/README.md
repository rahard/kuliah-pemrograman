# Queue

Ada dua queue dalam sistem ini. Satu (**inQueue**) menerima data (dari penyetor data)
dan satunya lagi (**OutQueue**) berisi ID Instagram yang menunggu di*crawl*).

Format data yang masuk ke **inQueue** adalah:

> IDpenyetor IDygdicrawl Follower

Data tersebut dapat berulang apabila *IDyangdicrawl* memiliki banyak followers.

Sementara itu output yang tersedia di **outQueue** memiliki format:

> IDtocrawl

*IDtocrawl* adalah ID Instagram yang akan dicrawl.

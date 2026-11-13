# concurrency

A small project for exploring concurrency concepts and patterns.

This is with GIL enabled by default because of older python version


It will act as Async single threaded process. An illussion of parallelism. It uses single thread. With concurrency it create illussion of parallelism.
```shell
 uv run --python 3.12 ./main.py
```

This is with GIL disabled by default making multithread work as parrallelism
It will act as Async multi threaded process process. A True parallelism with using more than 1 CPU cores
```shell
 uv run --python 3.14 ./main.py
```

```shell
 uv run --python 3.14t ./main.py
```
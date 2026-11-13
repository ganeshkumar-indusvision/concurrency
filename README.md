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


## Results


```shell

gk@jarvis:~/indus/concurrency$ uv run --python 3.12 ./main.py
3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]
Total runtime of the program in simple is 7.589684257982299 seconds
Total runtime of the program in thread is 8.74162275204435 seconds
gk@jarvis:~/indus/concurrency$ uv run --python 3.14 ./main.py
3.14.3 free-threading build (main, Feb  3 2026, 22:55:28) [Clang 21.1.4 ]
Total runtime of the program in simple is 9.498899512982462 seconds
Total runtime of the program in thread is 0.8658988000242971 seconds
gk@jarvis:~/indus/concurrency$ uv run --python 3.14t ./main.py
3.14.3 free-threading build (main, Feb  3 2026, 22:55:28) [Clang 21.1.4 ]
Total runtime of the program in simple is 9.52794164599618 seconds
Total logical CPU cores: 24
Total runtime of the program in thread is 0.9783794250106439 seconds
gk@jarvis:~/indus/concurrency$ 
```
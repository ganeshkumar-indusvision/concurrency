# concurrency

A small project for exploring concurrency concepts and patterns.

This is with GIL enabled by default because of older python version


It will act as Async single threaded process. An illussion of parallelism. It uses single thread. With concurrency it create illussion of parallelism.
```shell
 uv run --python 3.12 ./main.py
```

This is with GIL enabled by default present in last python version with GIL present.
It will act as Async single threaded process. An illussion of parallelism. It uses single thread. With concurrency it create illussion of parallelism.
```shell
 uv run --python 3.14.2 ./main.py
```
This is with GIL disabled by default making multithread work as parrallelism
It will act as Async multi threaded process process. A True parallelism with using more than 1 CPU cores
```shell
 uv run --python 3.14t ./main.py
```


## Results


```shell

gk@jarvis:~/indus/concurrency$ uv run --python 3.12 ./main.py
3.12.3 (main, Aug 31 2026, 10:18:26) [GCC 13.3.0]
Total runtime of the program in simple is 7.589684257982299 seconds
Total runtime of the program in thread is 8.74162275204435 seconds
gk@jarvis:~/indus/concurrency$ uv run --python 3.14.2 ./main.py
3.14.2 (main, Jan 27 2026, 23:59:57) [Clang 21.1.4 ]
Total runtime of the program in simple is 9.431666391028557 seconds
Total logical CPU cores: 24
Total runtime of the program in thread is 10.71485746698454 seconds
gk@jarvis:~/indus/concurrency$ 
gk@jarvis:~/indus/concurrency$ uv run --python 3.14t ./main.py
3.14.3 free-threading build (main, Feb  3 2026, 22:55:28) [Clang 21.1.4 ]
Total runtime of the program in simple is 9.52794164599618 seconds
Total logical CPU cores: 24
Total runtime of the program in thread is 0.9783794250106439 seconds
gk@jarvis:~/indus/concurrency$ 
```


Testing on 4 Core CPU with 100 iter

```shell
(ml) gk@jarvis:~/indus/concurrency$ uv run --python 3.12 main.py 
3.12.14 | packaged by Anaconda, Inc. | (main, Aug 27 2026, 14:46:43) [GCC 14.3.0]
Total runtime of the program in simple is 41.25938564500029 seconds
Total logical CPU cores: 4
Total runtime of the program in thread is 24.711810887001775 seconds
Total logical CPU cores: 4
Total runtime of the program in process is 9.60962972299967 seconds
(ml) gk@jarvis:~/indus/concurrency$ uv run --python 3.14t main.py 
3.14.7 free-threading build (main, Sep 24 2026, 17:58:28) [Clang 22.1.3 ]
Total runtime of the program in simple is 40.345531865998055 seconds
Total logical CPU cores: 4
Total runtime of the program in thread is 10.20734043399716 seconds
Total logical CPU cores: 4
Total runtime of the program in process is 8.417236731002049 seconds
(ml) gk@jarvis:~/indus/concurrency$ 

```
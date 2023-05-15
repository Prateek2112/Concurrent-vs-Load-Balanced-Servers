# PROJECT TITLE
### Performance of Multi-threaded server vs Load-Balanced Server

## INTRODUCTION
The aim of this project is to compare and evaluate the performance, scalability, and management complexity of Concurrent and Load-Balanced servers for optimizing server performance. This project aims to assist decision- makers in choosing the optimal option based on their unique use cases by offering a thorough study of these two server administration techniques. It will also point out the advantages and disadvantages of each strategy, giving both individuals as well as organizations useful insights into server management.

## AUTHORS
|Name|Net Id|
|----|------|
|[Bhavesh Veersen Sidhwani](https://github.com/BhaveshSidhwani)|bs1061|
|[Prateek Mishra](https://github.com/Prateek2112)|pm883|


## REQUIREMENTS
* Python3
* Pandas


## STEPS TO EXECUTE

### For Multi-Threaded server
1. Make sure that no csv exists.
2. Start the multi-threaded server on terminal
    ```
    python3 server_mt.py
    ```
3. Start the client and pass number of requests (Replace 1500 with the desired number) on another terminal instance
    ```
    python3 client_mt.py 1500
    ```
4. To get the average latency, execute the following on the terminal
    ```
    python3 avglatency.py
    ```

### For Load-Balanced Server
1. Make sure that no csv file exists.
2. Start the load-balancing server and secondary servers
    ```
    bash start_servers_lb.sh
    ```
3. Start the client and pass number of requests (Replace 1500 with the desired number) on another terminal instance
    ```
    python3 client_lb.py 1500
    ```
4. To get the average latency, send the KeyBoard Interrupt by pressing Ctrl+C or Cmd+C (On MacOS)

## REFERENCES
* [Multi-Threading](https://www.tutorialspoint.com/python/python_multithreading.htm)
* [Socket programming Ref. 1](https://docs.python.org/3/howto/sockets.html)
* [Socket programming Ref. 2](https://www.geeksforgeeks.org/socket-programming-python/)
* [Load-balancing server](https://blog.devgenius.io/5-minutes-to-learn-python-and-create-your-own-load-balancer-step-by-step-tutorial-included-f3109b5f7961)
* [Markdown file](https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f)

## ACKNOWLEDGEMENTS
We thank our Professor Srinivas Narayana for his constant support and guidance towards the success of our project.
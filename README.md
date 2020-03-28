![Comeet](./docs/comeet_logo.png)

## Comeet
Simple Client Server Chat

[![Python](https://img.shields.io/badge/Python-2.7-000.svg?style=flat-square)](https://www.python.org)
[![GitHub (pre-)release](https://img.shields.io/github/v/release/fctaddia/comeet.svg?color=000&include_prereleases&label=Release&style=flat-square)](./../../releases)

Comet gives the possibility to create a simple chat client server. Where you will have the opportunity to better understand the functioning of a tcp connection, so that you can develop a more complex chat.

### How to run server.py?

> **Tip:** You can run server.py on a raspberry pi so as to really simulate the communication between client and server
> **Tip:** Change the ip and port in server.py
#### Linux
Open the terminal, go to the directory where you saved server.py. Then to run server.py type this:

```Bash
python server.py
```
#### Windows
Suppose your script is in "Z:\code\hw01\server.py"

1) Open Command line:  Start menu -> Run  and type cmd
2) Type:  ```C:\python27\python.exe Z:\code\hw01\server.py```
> **Tip:** Or if your system is configured correctly, you can drag and drop your script from Explorer onto the Command Line window and press enter.
#### macOS

1) Open Command line:   Finder -> Go menu -> Applications -> Terminal
2) From the terminal go to the directory where you saved server.py (you can move to the directories via "cd")
3) Now to run server.py type this:
```Bash
python server.py
```

### How to run client.py?

> **Tip:** For each client that connects use a different username

To execute client.py repeat the same procedure, only changing "server.py" to "client.py".
Type this:
#### Linux, macOS
```Bash
python client.py
```
#### Windows
```Bash
C:\python27\python.exe Z:\code\hw01\client.py
```







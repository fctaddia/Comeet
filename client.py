import socket, select, string, sys

#Funzione ausiliare per la formattazione della chat
def display() :
	you="\33[33m\33[1m"+" Tu: "+"\33[0m"
	sys.stdout.write(you)
	sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        host = raw_input("Inserisci l'ip del server: ")
    else:
        host = sys.argv[1]

    port = 6005
    
    #richiesta nuovo nome utente
    name=raw_input("\33[34m\33[1m CREAZIONE NUOVO ID:\n Inserisci un username: \33[0m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    # connessione al server
    try :
        s.connect((host, port))
    except :
        print ("\33[31m\33[1m Impossibile connettersi al server \33[0m")
        sys.exit()

    #se si connette
    s.send(name)
    display()
    while 1:
        socket_list = [sys.stdin, s]
        
        # Ottieni l'elenco dei socket che sono leggibili
        rList, wList, error_list = select.select(socket_list , [], [])
        
        for sock in rList:
            #messaggio in arrivo dal server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print ('\33[31m\33[1m \rDISCONNESSO!!\n \33[0m')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    display()
        
            #l'utente ha inserito un messaggio
            else :
                msg=sys.stdin.readline()
                s.send(msg)
                display()

if __name__ == "__main__":
    main()

import socket, select

#Funzione per inviare messaggi a tutti i client connessi
def send_to_all (sock, message):
	#Messaggio non inoltrato al server e al mittente stesso
	for socket in connected_list:
		if socket != server_socket and socket != sock :
			try :
				socket.send(message)
			except :
				# se la connessione non e disponibile
				socket.close()
				connected_list.remove(socket)

if __name__ == "__main__":
	name=""
	# dizionario per memorizzare l'indirizzo corrispondente al nome utente
	record={}
	# Elenco per tenere traccia dei socket descriptors
	connected_list = []
	buffer = 4096
	port = 6005  # you can change the port to the one you want
	ip = 'localhost' # you can change the ip to the one you want

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_socket.bind((ip, port))
	server_socket.listen(10) # ascolta almeno 10 connessioni contemporaneamente

	# Aggiungi server socket all'elenco delle connessioni leggibili
	connected_list.append(server_socket)

	print ("\33[32m \t\t\t\tSERVER FUNZIONANTE \33[0m") 

	while 1:
	# Ottieni i socket della lista che sono pronti per essere letti attraverso select	
		rList,wList,error_sockets = select.select(connected_list,[],[])

		for sock in rList:
			#Nuova connessione
			if sock == server_socket:
				# Gestire il caso in cui e stata ricevuta una nuova connessione tramite server_socket
				sockfd, addr = server_socket.accept()
				name=sockfd.recv(buffer)
				connected_list.append(sockfd)
				record[addr]=""
				#print ("record and conn list ",record,connected_list)
                
                #se ripetuto lo username
				if name in list(record.values()):
					sockfd.send("\r\33[31m\33[1m Username gia in uso!\n\33[0m")
					del record[addr]
					connected_list.remove(sockfd)
					sockfd.close()
					continue
				else:
                    #aggiungi nome e indirizzo
					record[addr]=name
					print(("Client (%s, %s) online" % addr," [",record[addr],"]"))
					sockfd.send("\33[32m\r\33[1m Benvenuto nella Tchat. Inserisci 'tadda' in qualsiasi momento per uscire\n\33[0m")
					send_to_all(sockfd, "\33[32m\33[1m\r "+name+" si e unito alla conversazione \n\33[0m")

			#Alcuni messaggi in arrivo da un client
			else:
				# Data da client
				try:
					data1 = sock.recv(buffer)
					#print ("sock is: ",sock)
					data=data1[:data1.index("\n")]
					#print(("\ndata received: ",data))
                    
				#get indirizzo del client che invia il messaggio
					i,p=sock.getpeername()
					if data == "tadda":
						msg="\r\33[1m"+"\33[31m "+record[(i,p)]+" ha lasciato la conversazione \33[0m\n"
						send_to_all(sock,msg)
						print(("Client (%s, %s) e offline" % (i,p)," [",record[(i,p)],"]"))
						del record[(i,p)]
						connected_list.remove(sock)
						sock.close()
						continue

					else:
						msg="\r\33[1m"+"\33[35m "+record[(i,p)]+": "+"\33[0m"+data+"\n"
						send_to_all(sock,msg)
            
				#uscita improvvisa dell utente
				except:
					(i,p)=sock.getpeername()
					send_to_all(sock, "\r\33[31m \33[1m"+record[(i,p)]+" ha lasciato la conversazione inaspettatamente\33[0m\n")
					print(("Client (%s, %s) e offline (errore)" % (i,p)," [",record[(i,p)],"]\n"))
					del record[(i,p)]
					connected_list.remove(sock)
					sock.close()
					continue

	server_socket.close()


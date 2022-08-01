from socket import gethostbyname, gethostname, AF_INET, SOCK_DGRAM, SOCK_STREAM

REQUEST_COMMAND = "!REQ"
GRANT_COMMAND = "!GRANT"
DISCONNECT_COMMAND = "!DISC"
RELEASE_COMMAND = "!REL"

CLIENT_ID_IDENTIFIER = "!CLIENT_ID"

SERVER_IP = gethostbyname(gethostname())
UDP_SERVER_PORT = 5566
UDP_SERVER_ADDRESS = (SERVER_IP, UDP_SERVER_PORT)

MESSAGE_HEADER = 64
MESSAGE_SIZE = 1024
MESSAGE_FORMAT = "ascii"

SOCKET_FAMILY = AF_INET
SOCKET_UDP = SOCK_DGRAM
SOCKET_TCP = SOCK_STREAM

chosen_client_id = None
process_answered_counters = {}

import json
import time
import grpc
import messenger_pb2
import messenger_pb2_grpc
from concurrent import futures
import messenger

class Messenger(messenger_pb2_grpc.MessengerCallerServicer):
    def GetMessengerData(self , req , context):
        
        number = req.query
        print(number)
        myvar=messenger.Messenger()
        var2=myvar.test_add_contacts(number)
        print(var2)
        return messenger_pb2.MessengerResponse(response=json.dumps(var2) )
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    messenger_pb2_grpc.add_MessengerCallerServicer_to_server(Messenger(),server)
    server.add_insecure_port('[::]:50066')
    server.start()
    print ("started Messenger")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()


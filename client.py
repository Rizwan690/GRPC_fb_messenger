import json
import time
import grpc
import messenger_pb2
import messenger_pb2_grpc

def run():
    channel = grpc.insecure_channel(target = "localhost:50066")
    stub=messenger_pb2_grpc.MessengerCallerStub(channel)
    res = stub.GetMessengerData(messenger_pb2.MessengerQuery(query="SEARCH_NUMBER"))
    print(res.response)

    
if __name__ == "__main__":
    run()
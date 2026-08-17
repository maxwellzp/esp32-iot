import socket
import json


class APIServer:
    def __init__(self, sensor, host="0.0.0.0", port=80):
        self.sensor = sensor
        self.host = host
        self.port = port

    def start(self):
        address = socket.getaddrinfo(self.host, self.port)[0][-1]

        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(address)
        server.listen(1)

        print("HTTP server started")
        print("Listening on port:", self.port)

        while True:
            client, address = server.accept()

            try:
                self.handle_request(client)
            except Exception as e:
                print("Request error:", e)
            finally:
                client.close()

    def handle_request(self, client):
        request = client.recv(1024)

        if not request:
            return

        request_line = request.split(b"\r\n", 1)[0]
        parts = request_line.split()

        if len(parts) < 2:
            self.send_response(client, 400, {"error": "Bad request"})
            return

        method = parts[0]
        path = parts[1]

        if method != b"GET":
            self.send_response(client, 405, {"error": "Method not allowed"})
            return

        if path == b"/api/sensors":
            data = self.sensor.read()

            self.send_response(client, 200, data)
            return

        if path == b"/":
            self.send_response(client, 200, {"name": "esp32-iot", "status": "ok"})
            return

        self.send_response(client, 404, {"error": "Not found"})

    def send_response(self, client, status_code, data):
        body = json.dumps(data)

        status_messages = {
            200: "OK",
            400: "Bad Request",
            404: "Not Found",
            405: "Method Not Allowed",
        }

        status_message = status_messages.get(status_code, "Internal Server Error")

        response = (
            "HTTP/1.1 {} {}\r\n"
            "Content-Type: application/json\r\n"
            "Content-Length: {}\r\n"
            "Connection: close\r\n"
            "\r\n"
            "{}"
        ).format(status_code, status_message, len(body), body)

        client.send(response.encode())

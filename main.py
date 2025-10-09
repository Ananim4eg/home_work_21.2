from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        with open("src/web_main_page.html", 'r', encoding='utf-8') as file:
            web_page = file.read()
            return web_page

    def __get_new_page(self):
        with open("src/web_contact_page.html", 'r', encoding='utf-8') as file:
            web_page = file.read()
            return web_page

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_address = query_components.get('contact')
        page_content = self.__get_index()
        if page_address:
            page_content = self.__get_new_page()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
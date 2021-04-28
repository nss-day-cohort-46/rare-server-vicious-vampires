from http.server import BaseHTTPRequestHandler, HTTPServer
from categories import get_all_categories, delete_category, update_category, create_category, get_single_category  
from comments import get_all_comments, update_comment, delete_comment, create_comment, get_comment_by_post
from posts import get_all_posts, update_post, delete_post, get_posts_by_user, create_post, get_single_post
from users import get_all_users, get_single_user, create_user
from tags import get_all_tags, delete_tag, update_tag, create_tag, get_single_tag
import json

class HandleRequests(BaseHTTPRequestHandler):

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:

            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return ( resource, key, value )

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  
            except ValueError:
                pass 

            return (resource, id)

    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"

            if resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"
                    
            if resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
                    
            if resource == "tags":
                if id is not None:
                    response = f"{get_single_tag(id)}"
                else:
                    response = f"{get_all_tags()}"

        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

        # resource?key=value

            if key == "user_id" and resource == "posts":
                response = f"{get_posts_by_user(value)}"

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_comment = None
        new_category = None
        new_post = None
        new_tag = None
        new_user = None

        if resource == "comments":
            new_comment = create_comment(post_body)
            self.wfile.write(f"{new_comment}".encode())


        if resource == "categories":
            new_category = create_category(post_body)
            self.wfile.write(f"{new_category}".encode())


        if resource == "posts":
            new_post = create_post(post_body)
            self.wfile.write(f"{create_post}".encode())


        if resource == "tags":
            new_tag = create_tag(post_body)
            self.wfile.write(f"{new_tag}".encode())
        
        if resource == "users":
            new_tag = create_user(post_body)
            self.wfile.write(f"{new_user}".encode())



    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "categories":
            delete_category(id)
            self.wfile.write("".encode())

        if resource == "comments":
            delete_comment(id)
            self.wfile.write("".encode())

        if resource == "posts":
            delete_post(id)
            self.wfile.write("".encode())

        if resource == "tags":
            delete_tag(id)
            self.wfile.write("".encode())


    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "categories":
            success = update_category(id, post_body)

        if resource == "comments":
            success = update_comment(id, post_body)

        if resource == "posts":
            success = update_post(id, post_body)

        if resource == "tags":
            success = update_tag(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
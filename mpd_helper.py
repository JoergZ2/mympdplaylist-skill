def show_current_title(self, host, port):
    self.open_connection(host, port)
    liste = mpcc.currentsong()
    if not 'artist' in liste:
        answer = "Platz " + str(int(liste['pos']) + 1) + " " + liste['name']
    else:
        answer = "Platz " + str(int(liste['pos']) + 1) + " " + liste['title'] + " von Interpretin " + " " + liste['artist']
    self.close_connection()
    return answer



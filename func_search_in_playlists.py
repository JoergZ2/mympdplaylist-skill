#!/usr/bin/python3
#encoding: utf-8
import sys
import os
import time
from mpd import MPDClient #erforderlich zur Kommunikation mit dem MPD-Internet-Radio-Player
from mpd import CommandError as mce
mpcc = MPDClient()
host = "192.168.178.106"
port = 6600
#Basic functions
class mce(Exception):
    def __init__(self, wert):
        self.Wert = wert

def open_connection(host, port):
    mpcc.connect(str(host),int(port))

def close_connection():
    mpcc.disconnect()

def eval_playlists(pl, liste):
    for key1 in range(0, len(pl)):
        for key2 in range(0, len(liste[pl[key1]])):
                          print(liste[pl[key1]][key2]['file'])
def make_answer_from_search(suchwort, result_dict):
    answer = suchwort + " habe ich gefunden "
    for k in result_dict:
        pos = ''
        inner_answer = str(result_dict[k]) + " an Position "
        for k2 in result_dict[k]:
            pos = pos + str(result_dict[k][k2]) + " "
        answer = answer + " in " + result_dict[k] + inner_answer + pos
    return answer
            
def collect_stored_lists():
    open_connection(host, port)
    pl = list(mpcc.listplaylists())
    a = []
    pl_dict = {}
    for key in range(0, len(pl)):
        pl_dict[pl[key]['playlist']] = mpcc.listplaylistinfo(pl[key]['playlist'])
        a.append(pl_dict)
    close_connection()
    return pl_dict

def versuch2(suchwort):
    result = ''
    pl_dict = search_stored_lists()
    a = list(pl_dict)
    for key1 in range(0, len(a)):
        for key2 in range(0, len(pl_dict[a[key1]])):
            if 'name' in pl_dict[a[key1]][key2]:
                if suchwort.casefold() in pl_dict[a[key1]][key2]['name'].casefold():
                    line = (pl_dict[a[key1]][key2])
                    pos = pl_dict[a[key1]].index(line)
                    pos = pos + 1
                    result_raw = a[key1] + " an Position " + str(pos) #+ pl_dict[a[key1]][key2]['name']
                    result = result + result_raw + "\n"
                else:
                    pass
            else:
                pass
    result = "Gefunden in Liste:\n" + result
    return result

def create_answer_from_search_result(suchwort, result_dict):
    answer = "Das Suchwort " + suchwort + " habe ich gefunden "
    for k1 in result_dict:
        pos = ''
        for k2 in range(0, len(result_dict[k1])):
            pos = pos + str(result_dict[k1][k2])
            if len(result_dict[k1])> 1 and k2 < len(result_dict[k1]) - 1: pos = pos + " und "
            if k2 == len(result_dict[k1]) - 1: pos = pos + ". "
        answer = answer + "in Liste " + k1 + " an Position " + pos
    return answer


def versuch3(suchwort):
    result = ''
    result_raw = {}
    value_result = []
    pl_dict = collect_stored_lists()
    a = list(pl_dict)
    for key1 in range(0, len(a)):
        for key2 in range(0, len(pl_dict[a[key1]])):
            if 'name' in pl_dict[a[key1]][key2]:
                if suchwort.casefold() in pl_dict[a[key1]][key2]['name'].casefold():
                    line = (pl_dict[a[key1]][key2])
                    pos = pl_dict[a[key1]].index(line)
                    pos = pos + 1
                    value_result.append(pos)
                    key_result = a[key1]
                    result_raw.update({key_result: value_result}) #+ pl_dict[a[key1]][key2]['name']
                    result = result_raw
                else:
                    pass
            else:
                pass
        value_result = []
    #result = "Gefunden in Liste:\n" + result
    print(result)
    answer = create_answer_from_search_result(suchwort, result)
    return answer


def versuch4(suchwort):
    result = ''
    result_raw = {}
    value_result = []
    pl_dict = collect_stored_lists()
    a = list(pl_dict)
    for key1 in range(0, len(a)):
        for key2 in range(0, len(pl_dict[a[key1]])):
            if 'http://' in pl_dict[a[key1]][key2]['file']:
                if 'name' in pl_dict[a[key1]][key2]:
                    if suchwort.casefold() in pl_dict[a[key1]][key2]['name'].casefold():
                        line = (pl_dict[a[key1]][key2])
                        pos = pl_dict[a[key1]].index(line)
                        pos = pos + 1
                        value_result.append(pos)
                        key_result = a[key1]
                        result_raw.update({key_result: value_result}) #+ pl_dict[a[key1]][key2]['name']
                        result = result_raw
                    else:
                        pass
                else:
                    pass
            value_result = []
    #result = "Gefunden in Liste:\n" + result
    print(result)
    answer = create_answer_from_search_result(suchwort, result)
    return answer

liste = [{'file': 'Allanah Myles/Greatest Hits/Black Velvet.mp3', 'pos': '0', 'title': 'Black Velvet', 'album': 'albumtitel', 'artist': 'Name der Interpretin'}, \
         {'file': 'http://stream/irgendwas/stram.mp3', 'pos': '1', 'title': 'Aktuelle Sendung', 'name': 'ndr_ndr1_ndr1info_128_mp3'}, \
         {'file': 'Rolling Stones/Sticky Fingers/Sympathy For The Devil.mp3', 'pos': '2', 'title': 'Sympathy For The Devil', 'album': 'Plattentitel', 'artist': 'Name des Interpreten'}, \
         {'file': 'http://irgenwas.anders/kanal2/stram.mp3', 'pos': '1', 'title': 'Nächste Sendung', 'name': 'NDR 2'}]

query = input("Was suchst du? ")
result_dict = {'radiostationen (Kopie)': [1, 2, 3], 'sammlung': [1, 2], 'radiostationen': [1, 2, 3]}
result = create_answer_from_search_result(query, result_dict)
print(result)





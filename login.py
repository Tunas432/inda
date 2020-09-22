#بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِ
#GUNAKAN DENGAN BIJAK KAWAN....EDIT SESUKA KALIAN...
#HARGAI TANGAN CREATOR..!!!!!
#[CANNIBAL TEAM BOT]:
from linepy  import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from Naked.toolshed.shell import execute_js
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
#cannibal = LINE("tokenmu")
cannibal = LINE("@gmail.com","password")
cannibal.log("Auth Token : " + str(cannibal.authToken))
waitOpen = codecs.open("cannibal/wait.json","r","utf-8")
settingsOpen = codecs.open("cannibal/temp.json","r","utf-8")
cannibalProfile = cannibal.getProfile()
cannibalSettings = cannibal.getSettings()
cannibalPoll = OEPoll(cannibal)
cannibalStart = time.time()
cannibalMID = cannibal.getProfile().mid
loop = asyncio.get_event_loop()
admin =["midmu"]
botStart = time.time()
kuciyose = {}
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
mulai = time.time()

# MAAF BERANTAKAN..MASIH BELAJAR EDIT..

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}

sppam = {
  "list": [],
  "status": False
}
#=====================================================================
settings["myProfile"]["displayName"] = cannibalProfile.displayName
settings["myProfile"]["statusMessage"] = cannibalProfile.statusMessage
settings["myProfile"]["pictureStatus"] = cannibalProfile.pictureStatus
cont = cannibal.getContact(cannibalMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
#=====================================================================
with open("cannibal/temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("cannibal/wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu

#=====================================================================
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "JAVA SCRIPT",
            "iconUrl": "https://i.ibb.co/yqF3RcJ/Screenshot-2019-03-31-21-47-08-964-com-UCMobile-intl-picsay.png",
            "linkUrl": "line://nv/profilePopup/mid=uf19862ec64ac060f75c771ef3f33f1e5"
        }
    }
    sendTemplate(to, data)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1643727178-0XPGAaRX', xyzz)
    token = cannibal.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    cannibal.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    cannibal.sendMessage(to, '', annda, 13)    
#=====================================================================
def logError(text):
    cannibal.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("cannibal/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('cannibal/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('cannibal/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
async def cannibalBot(op):
    try:
        if settings["restartPoint"] != None:
            cannibal.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return

#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType == 0:
                    if msg.toType == 0 or msg.toType == 2:
                        if cmd == "logout" and sender == cannibalMID:
                            cannibal.generateReplyMessage(msg.id)
                            cannibal.sendReplyMessage(msg.id, to, "Your selfbot has been logout ♪")
                            sys.exit("Logout")
                        elif cmd == "js":
                            cannibal.sendMessage(to, "☯️ Komen ☯️\n\n☯️hai\n☯️kick <name>\n☯️bacok\n☯️@target on/off\n☯️spam gc <name>\n☯️grup\n☯️hapus spam\n\n☯️Jangan asal js aja☯️")
                        elif cmd == "alip":
                            cannibal.sendMessage(msg.to, msg._from)

                        elif cmd == "me" or text.lower() == 'aim':
                     #     if wait["selfbot"] == True:
                      #      if msg._from in owner or msg._from in admin or msg._from in staff:                                               
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cannibal.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                path = cannibal.getContact(msg.contentMetadata["mid"]).picturePath
                                image = 'http://dl.profile.line.naver.jp'+path
                                cannibal.sendImageWithURL(msg.to, image)
                                cannibal.sendMessage(msg.to, None, contentMetadata={"STKID":"52002768","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                        elif cmd == "hai":
                          xyz = cannibal.getGroup(to)
                          mem = [c.mid for c in xyz.members]
                          targets = []
                          for x in mem:
                            if x not in ["uf631edf2f22c3a064995453ecea62a69",cannibal.profile.mid]:targets.append(x)
                          if targets:
                            imnoob = 'simple.js gid={} token={} app={}'.format(to, cannibal.authToken, "CHROMEOS\t2.1.5\tDefrizal_OS\t1")
                            for target in targets:
                              imnoob += ' uid={}'.format(target)
                            success = execute_js(imnoob)
                            if success:cannibal.sendMessage(to, "Success kick %i members." % len(targets))
                            else:cannibal.sendMessage(to, "Failed kick %i members." % len(targets))
                          else:cannibal.sendMessage(to, "Target not found.")
                        elif cmd == "bacok":
                          xyz = cannibal.getGroup(to)
                          if xyz.invitee == None:pends = []
                          else:pends = [c.mid for c in xyz.invitee]
                          targp = []
                          for x in pends:
                            if x not in ["uf631edf2f22c3a064995453ecea62a69",cannibal.profile.mid]:targp.append(x)
                          mems = [c.mid for c in xyz.members]
                          targk = []
                          for x in mems:
                            if x not in ["uf631edf2f22c3a064995453ecea62a69",cannibal.profile.mid]:targk.append(x)
                          imnoob = 'dobel.js gid={} token={}'.format(to, cannibal.authToken)
                          for x in targp:imnoob += ' uid={}'.format(x)
                          for x in targk:imnoob += ' uik={}'.format(x)
                          execute_js(imnoob)
                        elif cmd.startswith("hai "):
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = cannibal.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           imnoob = 'simple.js gid={} token={} app={}'.format(to, cannibal.authToken, "CHROMEOS\t2.1.5\tDefrizal_OS\t1")
                           for x in members:
                               contact = cannibal.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                               #    print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return cannibal.sendMessage(to,"not found name "+midn)
                           for target in targets:
                             imnoob += ' uid={}'.format(target)
                           success = execute_js(imnoob)
                        elif cmd.startswith("@gc spam "):
                          nm = text.replace("@gc spam ","")
                          if sppam["list"] != []:
                            imnoob = "spam.js name={} token={}".format(nm,cannibal.authToken)
                            for target in sppam["list"]:
                              cannibal.findAndAddContactsByMid(target)
                              imnoob += " uid={}".format(target)
                            success = execute_js(imnoob)
                            if success:cannibal.sendMessage(to,"Done")
                            else:cannibal.sendMessage(to,"Error")
                          else:cannibal.sendMessage(to,"target is empty.")
                        elif cmd == "target on":
                          sppam["status"] = True
                          cannibal.sendMessage(to,"send a contact.")
                        elif cmd == "target off":
                          sppam["status"] = False
                          cannibal.sendMessage(to,"done.")
                        elif cmd == "hapus spam":
                          gids = cannibal.getGroupIdsInvited()
                          xyzs = []
                          for x in gids:xyzs.append(x)
                          for x in gids:
                            cannibal.acceptGroupInvitation(x)
                          for x in xyzs:
                            cannibal.leaveGroup(x)
                          cannibal.sendMessage(to, "Success reject %i invitation." % len(xyzs))
                        elif cmd == "grup":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = cannibal.getGroupIdsJoined()
                            sd = cannibal.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                cannibal.sendMessage(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                        
                if msg.contentType == 13 and sppam["status"] == True:
                  if msg.contentMetadata["mid"] not in sppam["list"]:
                    sppam["list"].append(msg.contentMetadata["mid"])
                    cannibal.sendMessage(to,"user added to list.")
                  else:
                    cannibal.sendMessage(to,"user already in list.")
#=====================================================================
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                _name = cannibal.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)

        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
   

def run():
    while True:
        try:
            ops = cannibalPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(cannibalBot(op))
                   cannibalPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()
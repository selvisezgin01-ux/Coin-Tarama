"""Presentation only. Never upgrades a stage, changes a signal or touches markers."""
import re
from urllib.parse import urlsplit

ENTRY='🟢🎯'
TECHNICAL='🟦✅'
ENTRY_LINE=re.compile(r'(?m)^(\*\*)(?:🟢🎯 )?(GERİ TEST — GİRİŞ TEYİDİ|GİRİŞ TEYİDİ)(?= · )')
MEME_LINE=re.compile(r'(?m)^([^\n]{1,120} · (?:solana|ethereum|bnb|robinhood|hyperevm) · )(?:🟦✅ )?(15 dk fiyat teyidi \+ 5 dk alım akışı|15 dk teknik teyit)(?= · )')
TUTUNMA=re.compile(r'(?m)^(grup: )(?:🟦✅ )?(tutunma)(?=;|$)')

def style(payload):
    if not isinstance(payload,dict) or not isinstance(payload.get('body'),str) or not isinstance(payload.get('title'),str):return payload
    if re.match(r'(?i)^(test|deneme)(?:\b|\s|·)',payload['title'].strip()):return payload
    out=dict(payload);parts=out['body'].split('```');entry=False;technical=False
    for i in range(0,len(parts),2):
        text=parts[i]
        if ENTRY_LINE.search(text):
            entry=True;text=ENTRY_LINE.sub(lambda m:m[1]+ENTRY+' '+m[2],text)
        if MEME_LINE.search(text):
            technical=True;text=MEME_LINE.sub(lambda m:m[1]+TECHNICAL+' '+m[2],text)
        if TUTUNMA.search(text):
            technical=True;text=TUTUNMA.sub(lambda m:m[1]+TECHNICAL+' '+m[2],text)
        parts[i]=text
    out['body']='```'.join(parts)
    if entry:
        if not out['title'].startswith(ENTRY+' '):out['title']=ENTRY+' '+out['title']
        banner='> '+ENTRY+' **GİRİŞ TEYİDİ**'
        if banner not in out['body']:out['body']=banner+'\n\n'+out['body']
    elif technical:
        if not out['title'].startswith(TECHNICAL+' '):out['title']=TECHNICAL+' '+out['title']
    return out

def outgoing(url,payload):
    p=urlsplit(url)
    if p.scheme=='https' and p.hostname=='api.github.com' and re.fullmatch(r'/repos/selvisezgin01-ux/Coin-Tarama/issues(?:/[0-9]+)?',p.path) and payload is not None:
        return style(payload)
    return payload

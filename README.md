# Simple_Chat_Client

Dette er et simpelt chat program skrevet i python, der kan tale sammen med [Andracs java chat server](https://github.com/andracs/Socket2021/blob/master/src/lmu/ChatServer.java)

Der connectes til serveren på port 59002(linje 7)

Besked fra server indlæses(linje 8)

Der tjekkes hvis beskeden starter med enten "SUBMITNAME", "NAMEACCEPTED", eller "MESSAGE". (linke 12, 14, 17)
Beskeden printesn(med starten af beskeden fjernet - eg. "NAMEACCEPTED" fjernes fra "NAMEACCEPTED (input navn fra client)"
Alt afhængig af ovenstående kaldes der enten send_name eller send_message, som er ansvarlige for at sende inputs fra brugeren til serveren.
Dette input er blevet encoded som utf-8.(linje 24, 29)

Løkken starter forfra.


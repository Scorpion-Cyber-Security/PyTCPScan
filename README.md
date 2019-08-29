# PyTCPScan
Repository for a PyTCPScan application.

PyTCPScan consiste em uma aplicação GNU/Linux para executar scaner de portas simples, onde o teste será 
direcionado para uma única porta, isto é bom pois dá mais controle ao usuário e faz menos barulho de log
no alvo especificado.

Esta é a versão 1.0 (beta) e está em fase de desenvolvimento. O código-fonte é aberto e aceita contribuição.

---

OBS.: Para usar como executável, lembrar de dar permissão de execução
**sudo chmod +x pytcpscan.py

## Execução ./pytcpscan
```
██████╗ ██╗   ██╗████████╗ ██████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ██║     ██████╔╝███████╗██║     ███████║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██║     ██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║
██║        ██║      ██║   ╚██████╗██║     ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝        ╚═╝      ╚═╝    ╚═════╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

Enter target host: google.com
Enter target port: 80

---Start scan---

HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Thu, 29 Aug 2019 00:42:43 GMT
Expires: Sat, 28 Sep 2019 00:42:43 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>

---End Execution---

```

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan?style=for-the-badge">  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan?style=for-the-badge">




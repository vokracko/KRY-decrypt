KRY: Projekt 1
==============
Projekt do předmětu	Kryptografie  (8. semestr FIT VUT) ve stavu, v jakém byl odevzdán k hodnocení.

### Hodnocení
5/8 - neobsahuje řešení pomocí SAT solveru

### Postup
1. XOR bis.txt bis.txt.enc => keystream
2. XOR keystream super_cipher.py.enc => čitelný algoritmus generování keystreamu z klíče
3. Implementance inverzní funkce k funkci ```step```
4. Zjištění původního klíče z keystreamu generovaného pro první blok
#Kandi++ - Python
  
###Jak to działa?
Aby móc korzystać z tego modułu, musisz pobrać plik kpp.py i zapisać go w folderze swojego projektu.  
Ważne, aby skrypt, do którego chcesz zaimportować kpp, był w tym samym miejscu, co nasz moduł.  
  
Kod:
```python
import kpp
```
####Korzystanie z funkcji
Teraz wystarczy tylko odwołać się do modułu, a następnie korzystać z jego funkcji (poniżej znajdziesz listę funkcji).  
Na przykład:
```python
print(kpp.decToBin(10))
```
Wtedy otrzymamy przekonwertowaną liczbę dziesiętną 10, do systemu binarnego.

##Lista funkcji

###encrypt():
Ta funkcja szyfruje podaną wiadomość szyfrem Cezara.
Wygląda tak:
```python
kpp.encrypt(msg, k)
```
Gdzie:
* msg - wiadomość do zakodowania
* k - liczba o jaką ma zostać przesunięta wartość znaku w UNICODE (musi być <=125)

###decrypt():
Ta funkcja odszyfrowuje wiadomość zaszyfrowaną szyfrem Cezara (głowa boli od tego powtórzenia).
Wygląda następująco:
```python
kpp.decrypt(msg, k)
```
Gdzie:
* msg - zaszyfrowana wiadomość
* k - liczba, o którą została przesunięta wartość znaku w UNICODE (musi być <=125)

###decToBin():
Ta funkcja konwertuje liczbę w systemie dziesiętnym, do systemu binarnego.
Wygląda tak:

```python
kpp.decToBin(liczba)
```
Gdzie:
* liczba - jest liczbą całkowitą (int). W przeciwnym wypadku, interpreter wyświetli błąd.

###decToHex():
Ta funkcja konwertuje liczbę w systemie dziesiętnym, do systemu szesnastkowego.
Wygląda tak:

```python
kpp.decToHex(liczba)
```

Gdzie:
* liczba - jest liczbą całkowitą (int). W przeciwnym wypadku - błąd.

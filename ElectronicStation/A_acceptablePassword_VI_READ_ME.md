# Zadanie
https://py.checkio.org/en/mission/acceptable-password-vi/

W tej misji musisz stworzyć funkcję weryfikacji hasła.

Oto warunki weryfikacji:

* długość powinna być większa niż 6;
* powinno zawierać co najmniej jedną cyfrę, ale nie może składać się z samych cyfr;
* Posiadanie cyfr lub zawieranie samych cyfr nie dotyczy hasła dłuższego niż 9.
* ciąg nie powinien w żadnym wypadku zawierać słowa "hasło";
* powinien zawierać co najmniej 3 różne litery (lub cyfry), nawet jeśli jest dłuższy niż 10

Wejście: `Ciąg znaków`

Wyjście: `Bool`

Przykład:

    is_acceptable_password('short') == False
      is_acceptable_password('short54') == True
      is_acceptable_password('muchlonger') == True
      is_acceptable_password('ashort') == False
      is_acceptable_password('muchlonger5') == True
      is_acceptable_password('sh5') == False
      is_acceptable_password('1234567') == False
      is_acceptable_password('12345678910') == True
      is_acceptable_password('password12345') == False
      is_acceptable_password('PASSWORD12345') == False
      is_acceptable_password('pass1234word') == True
      is_acceptable_password('aaaaaa1') == False
      is_acceptable_password('aaaaaabbbbb') == False

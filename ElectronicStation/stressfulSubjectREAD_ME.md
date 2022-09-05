# Zadanie
https://py.checkio.org/en/mission/stressful-subject/

Zofia miała bardzo stresujący miesiąc i postanowiła wziąć urlop na tydzień. Aby uniknąć stresu podczas urlopu, chce przekazać Stephenowi wiadomości ze stresującym tematem.

	Funkcja powinna rozpoznawać, czy temat jest stresujący. Stresujący temat oznacza, że wszystkie litery są pisane wielkimi literami, i/lub kończy się co najmniej 3 	wykrzyknikami, i/lub zawiera co najmniej jedno z następujących "czerwonych" słów: "help", "asap", "urgent". Każde z tych "czerwonych" słów może być napisane na 	różne sposoby - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", a nawet w bardzo długi sposób "HHHEEEEEEELLP", po prostu nie mogą być między nimi umieszczone żadne 	inne litery.

Wejście: `Linia tematu jako ciąg znaków`

Wyjście: `Boolean`

##Przykład:
  is_stressful("Hi") == False
	is_stressful("I neeed HELP") == True

Warunek wstępny: `Temat może mieć do 100 liter`

listOfNames.txt va contine o lista a fisierelor care lipsesc din folderul destinatie si care trbuie sa fie copiate.
 
 
 
 
Pentru rularea scriptului se modifica fisierele _details.txt si _FileList.txt conform regulilor de mai jos:

----------- _details.txt ------------
	1. Extensia fisierelor care se doresc a fi copiate.
 	2. Destinatia unde se doreste copiarea fisierelor (in functie de extensie si de existenta fisierelor cautate la calea destinatiei, se va updata folderul destinatie)
 	3. Search directory: in general, V:\RO01\DataLake\DCS01, dar poate fi modificat
 	
----------- _FileList.txt ----------- 
	Se va intocmi o lista a fisierelor care se doresc a fi copiate. 
	Forma listei nu conteaza!! Scriptul va cauta numele fisierului si ii va adauga extensia dorita pentru a crea fisierul listOfNames, indiferent daca _FileList contine path, ghilimele, _FileInfo etc.
	
	
	
	
Observatie!! 
	Liniile 53 si 54 contin comenzi pentru rularea fisierului copy.py. Se comenteaza/decomenteaza in functie de pyhton-ul folosit.
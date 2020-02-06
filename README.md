
Ex: body.txt contains: 
```
Dogmatic use of catapults by catatonic operators results in dire consequences.
```

Sample result:

```
╭─laboshinl@laptop-4
╰─$ python3 suggester.py  -f body.txt -p "cat"                                                                              2 ↵
['catapults', 'catatonic']
╭─laboshinl@laptop-4 
╰─$ python3 suggester.py  -f body.txt -p "catat"
['catatonic']
```

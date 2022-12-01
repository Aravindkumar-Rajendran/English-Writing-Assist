# Spell correction model

#### Command to run the server

```uvicorn app:app --port 8000```
  
  
#### API docs  
```http://locahost:8000/docs```


## Approach

I am using Peter-Norvig's edit distance (Levenhstein distance) with custom vocabulary created with Gtihub typo corpus to check and corrrect te spelling error. 

Also I have used FastAPI for hosting the spell checker as an API.

Detailed observation and improvements needed has been discussed in the notebook above. Symspell based approach appears to give faster output and word segmentation is possible with that. 



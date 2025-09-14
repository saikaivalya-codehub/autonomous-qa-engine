

---


## 🧰 Makefile (developer shortcuts)


**`Makefile`**
```make
up:
docker compose up --build


agent:
cd agent && uvicorn main:app --reload


app:
cd app && ./mvnw spring-boot:run


test-api:
cd tests-api && mvn test


test-ui:
cd tests-ui && npm i && npx playwright install && npm test
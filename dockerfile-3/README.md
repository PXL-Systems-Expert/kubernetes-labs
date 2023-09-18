# dockerfile-3

Dit project is gemaakt om docker configuraties voor backend projecten aan te leren. De studenten moet uitzoeken hoe zij hun configuratie moeten bouwen op basis van de README. Er zijn echter enkele extra helpers toegevoegd in de README en in de beschrijving van de oefening.

# opdracht

Maak een Dockerfile voor het project (pxl-backend) en geef een commando zodat het project draait in een docker-container met poort 8080 gepubliceerd.

Wanneer je de container start en navigeert naar http://localhost:8080/ping zou je een "pong" als antwoord moeten krijgen.

# Prerequisites voor development

Installeer [golang](https://golang.org/doc/install) 1.16

# Build project

Run `go build`. Dit zal een binary genereren: "server".

# Test project

Run tests met `go test ./...`.

# Execute project

Execute the file eg `./server`.

Server aanvaard de volgende environment variabelen:

- `PORT` om de poort te kiezen voor de applicatie. Default: 8080

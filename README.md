Criar Models
35 mim demo1_sp5


Options category exemple: 
```
criança | Amigo | Amiga | Aniversário | Aniversário 15 anos | Avó | Bebe | Casa Nova | Cestas de café | Cestas de Chás | Cestas Veganas | Dia dos Pais | Dia das mães | Espumante | Formatura | 
```

```ts
    interface ICategory{
        id: num;
	    name: str
	    image: string; //Caminho ?'../../...'
	    emphasis: boolean
	    adde_to: date;
	    update_to: date;
    }

```

# Animar

<div>
    <img align="center" alt="Krishna-Node" height="30" width="40" src="https://www.vectorlogo.zone/logos/nodejs/nodejs-icon.svg">
    <img align="center" alt="Krishna-PSQL" height="30" width="40" src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg">
     <img align="center" alt="Krishna-Ts" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-plain.svg">
</div>


### Introdução

### Base url
```
http://127.0.0.1:8000
```



### Endpoints, Casos de sucesso

`POST /api/posts/ - FORMATO DA REQUISIÇÃO`
###### Corpo de requisição:
```json
{
	"title": "Presentear sem sair de casa",
	"emphasis": true,
	"image": "/assets/presente01_YfjvXOx.jpg",
	"description": "O texto contém uma reflexão sobre as facilidades do mundo moderno, entre elas a facilidade para fazer compras e presentear.",
	"content": [
		"Há quem questione o avanço da modernidade, que ela trouxe tantas inovações que diminuiu o convívio social. É um fato! Mas há de se reconhecer as facilidades que a vida moderna nos trouxe também, como falar com quem quisermos com muita mais facilidade, termos acesso a mais conhecimento, nos aproximarmos em grupos de conversas e... fazermos compras!",
		"A facilidade de comprar é um dos encantamentos dessa modernidade! Temos diante de nossos olhos inúmeras opções, por todo lugar do planeta e podemos, interagindo com uma ferramenta digital, escolher, comprar, receber e devolver!",
		"A modernidade nos afasta das pessoas, mas não nos impede, de forma alguma, de interagirmos com uma loja online e comprar um presente para alguém! Sim, não uma compra para nós mesmos, mas para alguém que gostamos, que admiramos, que amamos, que reconhecemos e que queremos agradecer!",
		"Você pode estar em sua casa, no trabalho ou na rua mesmo e lembra que naquele dia ou naquela semana, há uma data importante para alguém! E isso não é mais um problema quando você tem à sua disposição a facilidade de uma compra online. Ainda mais se for de uma loja de presentes exclusivos e que entrega!",
		"Vamos reconsiderar nossa análise inicial?",
		"Ah, a modernidade!!! Quão sábios são os homens para criar facilidades para termos mais tempo para aproveitar e comemorar a vida!!!"
	]
}
```
###### Resposta: Status code: 201 CREATED

```json
{
	"id": 1,
	"title": "Presentear sem sair de casa",
	"emphasis": true,
	"image": "/assets/presente01_YfjvXOx.jpg",
	"description": "O texto contém uma reflexão sobre as facilidades do mundo moderno, entre elas a facilidade para fazer compras e presentear.",
	"content": [
		"Há quem questione o avanço da modernidade, que ela trouxe tantas inovações que diminuiu o convívio social. É um fato! Mas há de se reconhecer as facilidades que a vida moderna nos trouxe também, como falar com quem quisermos com muita mais facilidade, termos acesso a mais conhecimento, nos aproximarmos em grupos de conversas e... fazermos compras!",
		"A facilidade de comprar é um dos encantamentos dessa modernidade! Temos diante de nossos olhos inúmeras opções, por todo lugar do planeta e podemos, interagindo com uma ferramenta digital, escolher, comprar, receber e devolver!",
		"A modernidade nos afasta das pessoas, mas não nos impede, de forma alguma, de interagirmos com uma loja online e comprar um presente para alguém! Sim, não uma compra para nós mesmos, mas para alguém que gostamos, que admiramos, que amamos, que reconhecemos e que queremos agradecer!",
		"Você pode estar em sua casa, no trabalho ou na rua mesmo e lembra que naquele dia ou naquela semana, há uma data importante para alguém! E isso não é mais um problema quando você tem à sua disposição a facilidade de uma compra online. Ainda mais se for de uma loja de presentes exclusivos e que entrega!",
		"Vamos reconsiderar nossa análise inicial?",
		"Ah, a modernidade!!! Quão sábios são os homens para criar facilidades para termos mais tempo para aproveitar e comemorar a vida!!!"
	],
	"created_at": "2023-06-22T13:35:15.888238Z",
	"update_at": "2023-06-22T13:35:15.888238Z"
}
```


`GET  /api/posts/ - FORMATO DA REQUISIÇÃO`
Deve ser possível listar os posts armazenados no banco de dados. 
<!-- Seguindo as regras de paginação
exemplo de URL: `http://localhost:3000/movies/?sort=price&order=desc&page=2&perPage=3` -->

###### Resposta: Status code: 200 
```json
[
	{
		"id": 1,
		"title": "Presentear sem sair de casa",
		"emphasis": true,
		"image": "/assets/presente01_YfjvXOx.jpg",
		"description": "O texto contém uma reflexão sobre as facilidades do mundo moderno, entre elas a facilidade para fazer compras e presentear.",
		"content": [
			"Há quem questione o avanço da modernidade, que ela trouxe tantas inovações que diminuiu o convívio social. É um fato! Mas há de se reconhecer as facilidades que a vida moderna nos trouxe também, como falar com quem quisermos com muita mais facilidade, termos acesso a mais conhecimento, nos aproximarmos em grupos de conversas e... fazermos compras!",
			"A facilidade de comprar é um dos encantamentos dessa modernidade! Temos diante de nossos olhos inúmeras opções, por todo lugar do planeta e podemos, interagindo com uma ferramenta digital, escolher, comprar, receber e devolver!",
			"A modernidade nos afasta das pessoas, mas não nos impede, de forma alguma, de interagirmos com uma loja online e comprar um presente para alguém! Sim, não uma compra para nós mesmos, mas para alguém que gostamos, que admiramos, que amamos, que reconhecemos e que queremos agradecer!",
			"Você pode estar em sua casa, no trabalho ou na rua mesmo e lembra que naquele dia ou naquela semana, há uma data importante para alguém! E isso não é mais um problema quando você tem à sua disposição a facilidade de uma compra online. Ainda mais se for de uma loja de presentes exclusivos e que entrega!",
			"Vamos reconsiderar nossa análise inicial?",
			"Ah, a modernidade!!! Quão sábios são os homens para criar facilidades para termos mais tempo para aproveitar e comemorar a vida!!!"
		],
		"created_at": "2023-06-22T13:35:15.888238Z",
		"update_at": "2023-06-22T13:35:15.888238Z"
	},
	{
		"id": 2,
		"title": "Como criar um blog de sucesso em 2023",
		"emphasis": false,
		"image": "/assets/presente01_ajfKU9h.jpg",
		"description": "Neste post, você encontrará dicas valiosas para criar um blog de sucesso em 2023. Desde a escolha do nicho até a criação de conteúdo e a promoção do seu blog, este guia completo irá ajudá-lo a alcançar seus objetivos.",
		"content": [
			"Se você está pensando em criar um blog em 2023, é importante ter em mente que o mercado está cada vez mais competitivo. Por isso, é fundamental que você se destaque da concorrência e ofereça conteúdo de qualidade para seus leitores.",
			"O primeiro passo para criar um blog de sucesso é escolher um nicho que você goste e tenha conhecimento. Isso irá ajudá-lo a manter o interesse pelo assunto e produzir conteúdo relevante para seus leitores.",
			"Em seguida, é hora de criar conteúdo de qualidade. Isso significa que você deve produzir textos bem escritos, com informações relevantes e atualizadas. Além disso, é importante que você crie um calendário editorial para manter uma frequência de postagens.",
			"Outro ponto importante é a promoção do seu blog. Para isso, você pode utilizar as redes sociais e outras estratégias de marketing digital para atrair mais visitantes para o seu site.",
			"Por fim, é fundamental que você esteja sempre atualizado sobre as tendências do mercado e as novidades do seu nicho. Isso irá ajudá-lo a produzir conteúdo relevante e manter seus leitores engajados."
		],
		"created_at": "2023-06-22T13:42:01.811123Z",
		"update_at": "2023-06-22T13:42:01.811231Z"
	}
]
```


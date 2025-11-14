# BotCXT
Bot desenvolvido en Python para automatizar o envío de solicitudes na páxina da Xunta de Galicia do Concurso Xeral de Traslados (CXT) utilizando Selenium e unha interface gráfica baseada en Tkinter.

![img.png](img.png)

---

## Contidos

1. [Requisitos](#requisitos)  
2. [Instalación](#instalación)  
3. [Uso](#uso)  
4. [Estrutura do proxecto](#estrutura-do-proxecto)  
5. [Funcionamento](#funcionamento)  
6. [Creación do executable](#creación-do-executable)  
7. [Notas e boas prácticas](#notas-e-boas-prácticas)  

---

## Requisitos

- Python 3.12 (recomendado)  
- Pip  
- Navegador Firefox
- Librerías de Python especificadas no requirements.txt.

## Instalación
Instalar o navegador Mozilla Firefox https://www.mozilla.org/es-ES/firefox/new/

Clonar o repositorio ou descargar un zip.

No caso de querer utilizar directamente o executable, executar o ficheiro localizado na carpeta dist chamado botcxt.exe.

No caso de executar manualmente código e/ou desplegar o proxecto, instalar as dependencias especificadas no requirements.txt:

  ```bash
  selenium==4.22.0
  pyinstaller==6.16.0
  webdriver-manager==4.0.1
  ```

## Uso
1. Executar o script:
  ```bash
  python botcxt.py
  ```
2. Na interface gráfica:
- Premer Abrir navegador para iniciar Firefox. Iniciar a sesión e ir ao apartado de "Peticións" do CXT.
- Seleccionar un ficheiro de centros (.txt) que conte os códigos dos centros, separados por saltos de liña.
- Configurar:
  - Especialidade
  - Ente do vernáculo
  - Vernáculo
  - Linguas (separadas por ;)
  - Itinerancia (separadas por ;)
3. Premer Iniciar proceso para introducir as solicitudes automaticamente.

O programa mostrará unha mensaxe cando o proceso remate ou se produza un erro.

## Estrutura do proxecto
```bash
Bot-CXT/
│
├─ botcxt.py       # Interface gráfica e control principal
├─ scraper.py      # Funcións de Selenium para automatización web
└─ README.md       # Documentación
```

## Funcionamento

app.py
- Xestiona a interface de usuario con Tkinter.
- Permite seleccionar ficheiros e iniciar o navegador.
- Lanza a función lanzar do módulo scraper.py.

scraper.py
- Contén a función lanzar que automatiza a interacción coa páxina web.
- Para cada centro, itinerancia e lingua, selecciona os valores correspondentes nos formularios e realiza o envío.

Selenium + Firefox:
- O bot usa webdriver.Firefox() para abrir e controlar o navegador.

## Creación do executable
Para crear un executable de Windows cun só ficheiro executar no terminal:
```bash
pyinstaller --noconsole --onefile botcxt.py
```
Creará unha carpeta dist na que estará o executable botcxt.exe.
Neste repositorio facilítase a última versión do executable lista para lanzar.

## Notas e boas prácticas
- Asegurarse de que Mozilla Firefox está actualizado.
- Revisar que os nomes nos formularios da web coincidan coas seleccións do código (select_by_visible_text).
- Para cambiar os valores por defecto no GUI, modificar os manualmente os distinso parámetros.
- O bot foi deseñado para uso persoal e responsable; polo que se insta a non facer spam de solicitudes á páxina da Xunta.
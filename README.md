# BotCXT/CADP
Bot desenvolvido en Python para automatizar o envío de solicitudes na páxina da Xunta de Galicia do Concurso Xeral de Traslados (CXT) e no Concurso de Adxudicación de Destinos Provisionais (CADP) utilizando Selenium e unha interface gráfica baseada en Tkinter.

Pódese ver un titorial de uso no enlace https://youtu.be/pKWsqMe5GYo

Máis información en https://profesoradogalicia.com/botcxt/

![Ventana inicial](ventana_inicial.png)
![Ventana CXT](ventana_cxt.png)
![Ventana CADP](ventana_cadp.png)

---

## ☕ Apoia o proxecto
Se queres agradecer o traballo, podes convidarme a un café:

https://buymeacoffee.com/manuelduro


## Contidos

1. [Requisitos](#requisitos)  
2. [Instalación](#instalación)  
3. [Uso](#uso)
4. [Límite de destinos](#límite-de-destinos) 
5. [Estrutura do proxecto](#estrutura-do-proxecto) 
6. [Funcionamento](#funcionamento)  
7. [Creación do executable](#creación-do-executable)  
8. [Notas e boas prácticas](#notas-e-boas-prácticas)  

---

## Requisitos
Para simplemente lanzar o executable dist/botcxt.exe (usar o programa como tal) necesitamos:
- Navegador Mozilla Firefox
- O ficheiro co listado dos centros ordenados por tempo/distancia. Pódese obter en https://profesoradogalicia.com/colemaps/

Se ademais queremos executar o código fonte ou compilalo necesitamos tamén:
- Python 3.12 (recomendado)  
- Pip
- Librerías de Python especificadas no requirements.txt
 

## Instalación
Instalar o navegador Mozilla Firefox https://www.mozilla.org/es-ES/firefox/new/

Clonar o repositorio ou descargalo nun zip.

Para usar o executable sen instalar nada adicional, executar dist/botcxt.exe (con doble click é suficiente). Se salta un aviso de Windows ou do antivirus (esto é debido a que non o recoñece como un programa habitual xa que non é dunha grande corporación ou organización), pódese ignorar e proceder coa execución.

Para executar o código fonte, instalar as dependencias:
  ```bash
  pip install -r requirements.txt
  ```

Ou manualmente:
  ```bash
  selenium==4.22.0
  pyinstaller==6.16.0
  webdriver-manager==4.0.1
  ```

## Uso
1. Executar o ficheiro dist/botcxt.exe (doble click nel) ou executar directamente o código con:
  ```bash
  python src/botcxt.py
  ```
2. Na interface gráfica:
- Ao abrir o programa, seleccionar o trámite: CXT ou CADP.
- Cada formulario dispón dun botón ⬅ Volver para regresar á pantalla de selección.
- Premer Abrir navegador para iniciar Firefox. Iniciar a sesión e ir ao apartado de "Peticións" do CXT.
- Seleccionar un ficheiro de centros (.txt) que conte os códigos dos centros, separados por espacios ou saltos de liña. Este ficheiro pódese obter en https://centroseducativos.gal/
- No CXT configurar:
  - Especialidade
  - Ente do vernáculo
  - Vernáculo
  - Linguas → separadas por ; (exemplo: -- Sen indicar --;2-INGLÉS)
  - Itinerancia → separada por ; (exemplo: 0-Non;1-Si)
  - N destinos con opcións completas → número de centros aos que se lles aplicarán todas as linguas. Os restantes só recibirán a primeira lingua indicada.
3. Premer Iniciar proceso para introducir as solicitudes automaticamente.

O programa mostrará unha mensaxe cando o proceso remate ou se produza un erro.

## Límite de destinos
O formulario da Xunta só admite 400 peticións (polo menos para especialidades de secundaria en Galicia). Se se empregan varias linguas ou itinerancias, o número de combinacións por centro pode duplicarse ou triplicarse, superando con creces este límite.

Para evitar superar o límite, engadiuse o campo:
```bash
N destinos con opcións completas
```
Funcionamento:

Os N primeiros centros do ficheiro faranse con todas as linguas e itinerancias indicadas.

O resto dos centros non se duplicarán: faranse só coa primeira lingua e itinerancia escrita. Por exemplo, en "-- Sen indicar --;2-INGLÉS", quedarase só coa opción "-- Sen indicar --".

Se non se vai facer uso do parámetro, pode deixarse o valor 0.

## Estrutura do proxecto
```bash
BotCXT/
│
├─ src/
│   ├─ botcxt.py             # Control principal da aplicación
│   ├─ scraper.py            # Funcións de Selenium para CXT e CADP
│   └─ forms/
│       ├─ __init__.py
│       ├─ base.py           # Clase base para formularios
│       ├─ form_cxt.py       # Formulario CXT
│       └─ form_cadp.py      # Formulario CADP
├─ dist/                     # Executable xerado por PyInstaller
├─ requirements.txt          # Librarías usadas no proxecto 
└─ README.md                 # Documentación

```


## Funcionamento
botcxt.py
- Xestiona a interface de usuario con Tkinter.
- Permite seleccionar ficheiros, cambiar entre CXT e CADP, iniciar o navegador e lanzar o formulario correspondente.
- Dispón dun botón de Volver para regresar á pantalla de selección de trámite.

forms/
- Cada formulario é unha clase que herda de FormularioBase.
- FormularioCXT → campos específicos de CXT.
- FormularioCADP → campos específicos de CADP.
- Cada formulario xestiona a súa propia interface e execución.

scraper.py
- Contén as funcións lanzar_cxt e lanzar_cadp que automatizan a interacción co navegador mediante Selenium.

Selenium + Firefox
- O bot usa webdriver.Firefox() para abrir e controlar o navegador.

## Creación do executable
Para crear un executable de Windows cun só ficheiro executar no terminal:
```bash
pyinstaller --noconsole --onefile --paths src src/botcxt.py
```
Creará unha carpeta dist na que estará o executable botcxt.exe.
Neste repositorio facilítase a última versión do executable lista para lanzar.

## Notas e boas prácticas
- Asegurarse de que Mozilla Firefox está actualizado.
- Revisar que os nomes nos formularios da web coincidan exactamente (incluindo maiúsculas/minúsculas ou espacios) coas seleccións do código.
- Para cambiar os valores por defecto no GUI, modificar manualmente os distintos parámetros.
- O bot foi deseñado para uso persoal e responsable, polo que se insta a non facer spam de solicitudes á páxina da Xunta.
- O código é aberto e totalmente auditable. Ninguén debe confiar cegamente en executables sen revisalos.
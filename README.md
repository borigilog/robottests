<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Struktur](#struktur)
	- [Libs](#libs)
	- [SQL](#sql)
	- [Settings](#settings)
	- [Regressiontests](#regressiontests)
		- [General_Keywords   <a name="generalkeywords"></a>](#generalkeywords-a-namegeneralkeywordsa)
		- [General_PageObjects  <a name="generalpageobjects"></a>](#generalpageobjects-a-namegeneralpageobjectsa)
		- [General_Variables  <a name="generalvariables"></a>](#generalvariables-a-namegeneralvariablesa)
		- [Modul-Tests](#modul-tests)
			- [PageObjects](#pageobjects)
				- [Menu-PageObjects](#menu-pageobjects)
- [Wie schreibt man Tests ?](#wie-schreibt-man-tests-)
	- [Installation](#installation)
	- [Robotframework Basics](#robotframework-basics)
	- [Was man beim Test schreiben berücksichtigen sollte](#was-man-beim-test-schreiben-berücksichtigen-sollte)
	- [Wie man eigene Python-Bibliotheken schreibt](#wie-man-eigene-python-bibliotheken-schreibt)
	- [Wo fügt man Variablen und Keywords ein ?](#wo-fügt-man-variablen-und-keywords-ein-)
- [Wording/Begriffserklärung](#wordingbegriffserklärung)
	- [PageObject](#pageobject)
- [README-Datei bearbeiten:](#readme-datei-bearbeiten)
	- [Syntax](#syntax)
	- [Editor](#editor)

<!-- /TOC -->
# Struktur

## Libs
Enthält von uns geschriebene Python-Bibliotheken.

## SQL
Enthält alle SQL-Statements

## Settings
Enthält Dictionary-Ressourcen-Dateien etc. <br>
Pro Modul muss ein Unterordner erstellt werden.

## Regressiontests
Enthält alle Tests

### General_Keywords   <a name="generalkeywords"></a>
Enthält [Keywords](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords), die man für jede Website nutzen könnte (nicht speziell für unsere) und die zu keinem sinnvollen  [PageObject](#PageObject) gruppiert werden können.

### General_PageObjects  <a name="generalpageobjects"></a>
Hier landen [PageObjects](#PageObject), die an mehreren Stellen innerhalb der Website vorkommen (Languageselector, Trees, Grids, DatePicker....)

### General_Variables  <a name="generalvariables"></a>
Variablen, die für die gesamte Website gelten (Login, Password, URL, Standard Sprache, Mandant...).

### Modul-Tests
1. Für jedes Modul muss ein **Ordner mit Namen des Moduls** erstellt werden (_BILL_, _LOG_, _OAC_...).<br>
2. Innerhalb dieses Ordners wird pro _Bereich_ eine [Testsuite](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-suites) erstellt. <br>
Was ein _Bereich_ ist, ist dem Ersteller der Tests überlassen. <br>
**Anhaltspunkt:** Pro html-Ansicht eine Testsuite erstellen. (Ist aber kein Muss!)

#### PageObjects   
Enthält [PageObjects](#PageObject), die nur für dieses Modul gelten.<br>
##### Menu-PageObjects
Da jedes Modul sein eigenes Menü hat, enthält jeder PageObjects-Ordner eine [Resource](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#resource-files) **Menu.txt**.<br>
- In dieser Resource wird pro Menüpunkt/Untermenüpunkt ein Keyword erstellt.<br>
- Da pro Testsuite gewöhnlich ein Menüpunkt im Suite Setup inklusive Login aufgerufen wird, danach pro TestCase jedoch nur noch ohne Login, sollte man pro Keyword einen Parameter einbauen, der steuert, ob nur der Menüpunkt geklickt oder zuvor noch der komplette Login-Vorgang gestartet werden soll.

**Beispiel**
```robotframework
*** Settings ***
Resource          ../../General_PageObjects/Login.txt
Resource          ../../General_PageObjects/Menu_Common.txt

*** Variables ***
${menu_content}    /$flow_main/$flow_content
${invoice_management}    /$flow_main/main_menu/invoice_management
${invoice_management_class}    screen look_rlx_screen_bill_generally_invoicemanagement

*** Keywords ***
Login Select Bill
    [Arguments]    ${login}=true
    ${navigateToBillModule} =    Is Truthy    ${login}
    Run Keyword If    ${navigateToBillModule}    Login For Module    Bill
    Run Keyword If    ${navigateToBillModule}    Check Homescreen is selected
    Check PageArea is visible    /$flow_main    screen look_rlx_screen_bill_main

Check Homescreen is selected
    Check PageArea is visible    ${menu_content}    screen look_rlx_screen_bill_homescreen

Select Rechnungsverwaltung
    [Arguments]    ${login}=false
    Login Select Bill    ${login}
    Select Menu Content    ${invoice_management}    ${invoice_management_class}
```

# Wie schreibt man Tests ?
## Installation
- Installationsanleitung Deutsch mit integrierten Installern, Anleitung, wie man das Rpository ziehen kann und ein Desktop-Icon erstellt: **\\sr-fs03\Rigilog\Development\Testautomatisierung\UI-Testing_getting_started.docx**  
- [Installationsanleitung für Ride auf Englisch](https://www.swtestacademy.com/getting-started-robotframework/) (z.B. wenn man mal keinen Zugriff auf unser Netzwerk hat)

## Robotframework Basics
- [Test Suites erstellen](https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/CreatingTestData/CreatingTestSuites.rst)
- [Test Cases erstellen](https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/CreatingTestData/CreatingTestCases.rst)
- [Keywords dokumentieren](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#id353)

## Was man beim Test schreiben berücksichtigen sollte
- [Resourcen](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#resource-files) müssen als **.txt** oder **.robot** Datei gespeichert werden um kompatibel zu anderen Editoren zu sein.
- [How to Write Good TestCases](https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst)
- [Do's and Dont's](https://de.slideshare.net/pekkaklarck/robot-framework-dos-and-donts)

## Wie man eigene Python-Bibliotheken schreibt
- [Simples Beispiel inkl. Aufruf](https://stackoverflow.com/questions/27039016/how-to-create-a-custom-python-code-library-for-the-robot-framework)
- [Creating Testlibraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries)

## Wo fügt man Variablen und Keywords ein ?
1. [Variablen](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#variables) und [Keywords](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords) zunächst direkt in die Testsuite einfügen.
2. Stellt man fest, dass man Keywords/Variablen in mehreren Testsuites benötigt, kann man diese an generellere Stellen verschieben
    * Sind die Variablen/Keywords modulspezifisch, sollten sie zu einem [Modulspezifischen PageObjects](#pageobjects) zusammengefasst werden.
    * Handelt es sich um Keywords, die überall in der Website vorkommen können:
        * Handelt es sich um [PageObjects](#PageObject), können sie zu den [GeneralPageObjects](#generalpageobjects) hinzugefügt werden.
        * Andernfalls werden sie den [General_Keywords](#generalkeywords) zugeordnet.

## Tests, die Daten verändern
Werden innerhalb eines Tests Daten verändert (Löschen, Anlegen, Ändern), müssen die Änderungen am Ende des Tests rückgängig gemacht werden, um zu verhindern, dass durch die Änderungen andere Tests fehlschlagen. <br>
Hierfür im [Teardown](https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/CreatingTestData/CreatingTestSuites.rst#suite-setup-and-teardown) des TestCases oder der Testsuite die Datenbank zurücksetzen. <br>
Dies geht durch Aufruf des Keywords **Restore Database Snapshot** aus *General_PageObjects/Database.txt* <br>

**Zu beachten**: <br>
Setzt man erst am Ende der Testsuite die Datenbank zurück, müssen alle Tests innerhalb der Testsuite Daten erwarten, die nicht durch andere Tests derselben Testsuite verändert werden.

**Beispiel: Teardown für einen Test Case**
```robotframework
*** Settings ***
Resource          ../General_PageObjects/Database.txt

*** Test Cases ***
Some Test
		DB Execute Scalar    INSERT INTO Accounting_Balance_Architecture_Headers(isUsedForSystemGeneratedBallance) values(1)
    [Teardown]    Restore Database Snapshot
```

## Warten, bis Daten geladen wurden
Das Metax-Framework setzt automatisch bei jedem Lade-Vorgang die Klasse vom *<body>*-Html-Element auf *freezed*.<br>
Sobald die Abfrage fertig ist und die Daten angezeigt wurden, wird die Klasse wieder zurückgesetzt. <br>
Daher: Um zu warten, bis Daten angezeigt wurden anstatt *Sleep* zu verwenden, das Keyword **Wait until Page is unfreezed** aus *General_PageObjects/Page.txt* verwenden.

# Wording/Begriffserklärung
## PageObject
<a name="PageObject"></a> eine Art _Komponente_ = Sammlung von **Keywords**, die für eine Gruppe von immer zusammengehörenden Html-Elementen gelten.<br>
[Siehe PageObject-DesignPattern](https://martinfowler.com/bliki/PageObject.html).


# README-Datei bearbeiten:
## Syntax
[Markdown Syntax](https://guides.github.com/features/mastering-markdown/)
## Editor
[Atom](https://atom.io/)
- [strg+shift+m öffnet ein Preview](https://guides.github.com/features/mastering-markdown/)
- Inhaltsverzeichnis erstellen mit dem AddOn [markdown-toc](https://atom.io/packages/markdown-toc)

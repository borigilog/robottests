<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [About robottests](#about-robottests)
- [robottest - Struktur](#robottest-struktur)
	- [Libs](#libs)
	- [SQL](#sql)
	- [Settings](#settings)
	- [Regressiontests](#regressiontests)
		- [General_Keywords](#generalkeywords)
		- [General_PageObjects](#generalpageobjects)
		- [General_Variables](#generalvariables)
		- [Modul-Tests](#modul-tests)
			- [PageObjects](#pageobjects)
- [Wie schreibt man Tests ?](#wie-schreibt-man-tests-)
	- [Installation](#installation)
	- [Robotframework Basics](#robotframework-basics)
	- [Was man beim Test schreiben berücksichtigen sollte](#was-man-beim-test-schreiben-berücksichtigen-sollte)
	- [Wie man eigene Python-Bibliotheken schreibt](#wie-man-eigene-python-bibliotheken-schreibt)
- [README-Datei bearbeiten:](#readme-datei-bearbeiten)
	- [Syntax](#syntax)
	- [Editor](#editor)

<!-- /TOC -->
# About robottests
robotframework - automated on-line tests for WebGUI

# robottest - Struktur

## Libs
Enthält von uns geschriebene Python-Bibliotheken.

## SQL
Enthält alle SQL-Statements

## Settings
Enthält Dictionary-Ressourcen-Dateien etc. <br>
Pro Modul muss ein Unterordner erstellt werden.


## Regressiontests
Enthält alle Tests

### General_Keywords
Allgemeine **Keywords** = [Keywords](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-user-keywords), die man für jede Website nutzen könnte (nicht speziell für unsere) und die nicht zu einem **PageObject** gruppiert werden.

### General_PageObjects
**[PageObject](https://martinfowler.com/bliki/PageObject.html)** = eine Art _Komponente_ = Sammlung von **Keywords**, die für eine Gruppe von immer zusammengehörenden Html-Elementen gelten.

Allgemeine **PageObjects** = PageObjects, die an mehreren Stellen innerhalb der Website vorkommen (Languageselector, Trees, Grids, DatePicker....)

### General_Variables
Variablen, die für die gesamte Website gelten (Login, Password, URL, Standard SPrache, Mandant...).

### Modul-Tests
Für jedes Modul muss ein **Ordner mit Namen des Moduls** erstellt werden (_BILL_, _LOG_, _OAC_...).<br>
Innerhalb dieses Ordners wird pro _Bereich_ eine **Testsuite** erstellt. <br>
Was ein _Bereich_ ist, ist dem Ersteller der Tests überlassen. <br>
Ein Anhaltspunkt: Pro html-Ansicht eine Testsuite erstellen. (Ist aber kein Muss!)

#### PageObjects
Enthält **[PageObject](https://martinfowler.com/bliki/PageObject.html)**, die nur für dieses Modul gelten.

# Wie schreibt man Tests ?
## Installation
- Installationsanleitung Deutsch mit integrierten Installern, Anleitung, wie man das Rpository ziehen kann und ein Desktop-Icon erstellt: **\\sr-fs03\Rigilog\Development\Testautomatisierung\UI-Testing_getting_started.docx**  
- Installationsanleitung Englisch (z.B. wenn man mal keinen Zugriff auf unser Netzwerk hat): https://www.swtestacademy.com/getting-started-robotframework/

## Robotframework Basics
- [Creating Test Suites](https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/CreatingTestData/CreatingTestSuites.rst)
- [Creating Test Cases](https://github.com/robotframework/robotframework/blob/master/doc/userguide/src/CreatingTestData/CreatingTestCases.rst)

## Was man beim Test schreiben berücksichtigen sollte
- [How to Write Good TestCases](https://github.com/robotframework/HowToWriteGoodTestCases/blob/master/HowToWriteGoodTestCases.rst)
- [Do's and Dont's](https://de.slideshare.net/pekkaklarck/robot-framework-dos-and-donts)

## Wie man eigene Python-Bibliotheken schreibt
- [Simples Beispiel inkl. Aufruf](https://stackoverflow.com/questions/27039016/how-to-create-a-custom-python-code-library-for-the-robot-framework)
- [Creating Testlibraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries)


# README-Datei bearbeiten:
## Syntax
[Markdown Syntax](https://guides.github.com/features/mastering-markdown/)
## Editor
[Atom](https://atom.io/)
- [strg+shift+m öffnet ein Preview] (https://guides.github.com/features/mastering-markdown/)
- Inhaltsverzeichnis erstellen mit dem AddOn [markdown-toc](https://atom.io/packages/markdown-toc)

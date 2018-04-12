# robottests
robotframework - automated on-line tests for WebGUI

# Struktur

## Libs
Enthält Python-Bibliotheken

## SQL
Enthält alle SQL-Statements

## Settings
Enthält Dictionary-Ressourcen-Dateien etc.
Pro Modul muss ein Unterordner erstellt werden.


## Regressiontests
Enthält alle Tests

### General_Keywords
Allgemeine **Keywords** = Keywords, die man für jede Website nutzen könnte (nicht speziell für unsere) und die nicht zu einem **PageObject** gruppiert werden.

### General_PageObjects
Allgemeine **PageObjects** = _Komponenten_, die an mehreren Stellen innerhalb der WEbsite vorkommen (Languageselector, Trees, Grids, DatePicker....)

### General_Variables
Variablen, die für die gesamte Website gelten (Login, Password, URL, Standard SPrache, Mandant...).

### Modul-Tests
Für jedes Modul muss ein **Ordner mit Namen des Moduls** erstellt werden (_BILL_, _LOG_, _OAC_...).
Innerhalb dieses Ordners wird pro _Bereich_ eine **Testsuite** erstellt.
Was ein _Bereich_ ist, ist dem Ersteller der Tests überlassen.
Ein Anhaltspunkt: Pro html-Ansicht eine Testsuite erstellen.
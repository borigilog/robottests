<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [robottests](#robottests)
- [Struktur](#struktur)
  - [Libs](#libs)
  - [SQL](#sql)
  - [Settings](#settings)
  - [Regressiontests](#regressiontests)
    - [General_Keywords](#general_keywords)
    - [General_PageObjects](#general_pageobjects)
    - [General_Variables](#general_variables)
    - [Modul-Tests](#modul-tests)
      - [PageObjects](#pageobjects)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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
**PageObject** = eine Art _Komponente_ = Sammlung von **Keywords**, die für eine Gruppe von immer zusammengehörenden Html-Elementen gelten.

Allgemeine **PageObjects** = PageObjects, die an mehreren Stellen innerhalb der Website vorkommen (Languageselector, Trees, Grids, DatePicker....)

### General_Variables
Variablen, die für die gesamte Website gelten (Login, Password, URL, Standard SPrache, Mandant...).

### Modul-Tests
Für jedes Modul muss ein **Ordner mit Namen des Moduls** erstellt werden (_BILL_, _LOG_, _OAC_...).

Innerhalb dieses Ordners wird pro _Bereich_ eine **Testsuite** erstellt.

Was ein _Bereich_ ist, ist dem Ersteller der Tests überlassen.

Ein Anhaltspunkt: Pro html-Ansicht eine Testsuite erstellen.

#### PageObjects
Enthält **PageObjects** dir nur für dieses Modul gelten.
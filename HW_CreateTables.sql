/*
   HW_CreateTables.sql
   Author: Jordan Alexis Caraballo-Vega
   Data Base Class, Prof. O. Medina
   Purpose: Script that creates Hot Water Company Tables.
   Input: Given by the script.
*/

ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY';

/* Create MANUFACTURER Table */
CREATE TABLE MANUFACTURER (
    MAN_CODE     NUMBER(10,0) PRIMARY KEY,
    MAN_COMPANY  VARCHAR2(30) NOT NULL,
    MAN_STREET   VARCHAR2(30),
    MAN_CITY     VARCHAR2(30),
    MAN_STATE    VARCHAR2(30),
    MAN_ZIP      NUMBER(5,0),
    MAN_AREACODE NUMBER(3,0),
    MAN_PHONE    NUMBER(7,0),
    MAN_ACCNUM   NUMBER(6,0) NOT NULL
);

/* Create BRAND Table */
CREATE TABLE BRAND (
BRAND_ID    NUMBER(10,0) PRIMARY KEY,
BRAND_NAME  VARCHAR2(30) NOT NULL,
BRAND_LEVEL VARCHAR2(30),
MAN_CODE    NUMBER(10,0) REFERENCES MANUFACTURER
);

/* Create Model Table */
CREATE TABLE MODEL (
MODEL_NUM NUMBER(10) PRIMARY KEY,
MODEL_JETS NUMBER(10),
MODEL_MOTORS NUMBER(10),
MODEL_HP NUMBER(10),
MODEL_SRP NUMBER(8,2),
MODEL_HWRP NUMBER(8,2),
MODEL_WEIGTH NUMBER(8,2),
MODEL_WATCAP NUMBER(8,2),
MODEL_SEATCAP NUMBER(10),
BRAND_ID NUMBER(10,0) REFERENCES BRAND
);




-- Active: 1710419443849@@127.0.0.1@3306@emprendimiento
-- Creamos la base de datos
CREATE DATABASE IF NOT EXISTS emprendimiento;
USE emprendimiento;

-- Creamos las tablas 
CREATE TABLE Tipo_Usuario (
    idTipo_Usuario INT PRIMARY KEY,
    nombre VARCHAR(45)
);

CREATE TABLE Administrador (
    codigo_Administrador INT PRIMARY KEY,
    nombre VARCHAR(45),
    apellidos VARCHAR(45),
    telefono VARCHAR(45),
    email VARCHAR(45),
    Tipo_Usuario_idTipo_Usuario INT,
    FOREIGN KEY (Tipo_Usuario_idTipo_Usuario) REFERENCES Tipo_Usuario(idTipo_Usuario)
);

CREATE TABLE clientes (
    idclientes INT PRIMARY KEY,
    nombres VARCHAR(45),
    apellidos VARCHAR(45),
    telefono VARCHAR(45),
    correo VARCHAR(50),
    Tipo_Usuario_idTipo_Usuario INT,
    FOREIGN KEY (Tipo_Usuario_idTipo_Usuario) REFERENCES Tipo_Usuario(idTipo_Usuario)
); 



